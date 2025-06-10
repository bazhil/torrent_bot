# -*- coding: utf-8 -*-
import os
import json
import time
import asyncio
from dotenv import load_dotenv
from typing import Dict, List, Optional, Tuple
from tqdm import tqdm
from torrent_repository import TorrentRepository


class AsyncRutrackerParser:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Path configuration
        self.torrent_folder_path = os.getenv('TORRENT_FOLDER_PATH', 'L:\\rutracker-torrents\\')
        self.torrent_archive = os.path.abspath(os.path.dirname(self.torrent_folder_path))

        # Internal variables
        self.service_cat: Dict[str, List[str]] = {}
        self.serv_ar: List[str] = []
        self.total_files = 0
        self.processed_files = 0
        self.total_records = 0

    async def generate_cat_dict(self) -> Dict[str, List[str]]:
        """
        Builds a dictionary of categories, subcategories and files where they can be found.
        Returns dictionary with categories and their corresponding files.
        """
        print("⏳ Generating category dictionary...")
        in_str = ''
        tree = os.walk(self.torrent_archive)

        for root, dirs, files in tree:
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    if file == 'category_info.csv':
                        with open(file_path, 'r', encoding='utf-8') as cat_info:
                            for line in cat_info:
                                if line not in self.serv_ar:
                                    self.serv_ar.append(line)

        in_str = ''.join(self.serv_ar)
        in_list = [[s.strip('"') for s in item.split(';')] for item in
                   list(filter(lambda x: x != '', in_str.split('\n')))]

        for i in range(len(in_list)):
            n = 1
            if (i < len(in_list) - 1):
                n = int(in_list[i + 1][0]) - int(in_list[i][0])
                self.service_cat[in_list[i][1]] = [
                    f"category_{int(in_list[i][0]) + j}.csv" for j in range(n)
                ]

        with open('service_cat.json', 'w', encoding='utf-8') as c:
            json.dump(self.service_cat, c, ensure_ascii=False, indent=2)

        print("✅ Category dictionary generated")
        return self.service_cat

    def _count_total_files(self) -> None:
        """Count total files to process for progress tracking"""
        self.total_files = 0
        tree = os.walk(self.torrent_archive)
        for root, dirs, files in tree:
            for file in files:
                if file.endswith('.csv'):
                    for value in self.service_cat.values():
                        if file in value:
                            self.total_files += 1

    async def _process_csv_file(self, root: str, file: str) -> List[Tuple[str, str, str, str]]:
        """Process a single CSV file and return data for insertion"""
        file_path = os.path.join(root, file)
        data = []
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            for line in csv_file:
                parts = line.split(';')
                if len(parts) >= 6:
                    forum_name = parts[1].replace('"', '')
                    distribution_hash = parts[3].replace('"', '')
                    torrent_name = parts[4].replace('"', '')
                    magnet_link = 'magnet:?xt=urn:btih:' + distribution_hash

                    # Find the category for this file
                    for category, files in self.service_cat.items():
                        if file in files:
                            data.append((category, forum_name, torrent_name, magnet_link))
                            break

        self.processed_files += 1
        self.total_records += len(data)
        return data

    async def find_categories(self):
        """Reads archive files and yields chunks of data for insertion"""
        print("🔍 Starting to process files...")
        self._count_total_files()

        tasks = []
        tree = os.walk(self.torrent_archive)
        for root, dirs, files in tree:
            for file in files:
                if file.endswith('.csv'):
                    for value in self.service_cat.values():
                        if str(file) in value:
                            tasks.append(self._process_csv_file(root, file))

        # Process files with progress tracking
        with tqdm(total=self.total_files, desc="🌐 Processing files") as pbar:
            for future in asyncio.as_completed(tasks):
                file_data = await future

                yield file_data
                pbar.update(1)
                # pbar.set_postfix({
                #     'records': self.total_records
                # })

    async def process_chunks(self):
        """Process chunks of data and insert them into the database using TorrentRepository"""
        async with TorrentRepository() as repo:
            # Ensure the table exists
            await repo.create_table()

            # Process chunks from find_categories
            async for chunk in self.find_categories():
                await repo.insert_batch(chunk)

    async def run(self) -> None:
        """Main execution method"""
        start_time = time.time()

        try:
            await self.generate_cat_dict()
            await self.process_chunks()

            # Print statistics
            elapsed = time.time() - start_time
            print(f'⏱️ Total time elapsed: {elapsed:.2f} seconds')
        except Exception as e:
            print(f"❌ Error occurred: {e}")


if __name__ == '__main__':
    asyncio.run(AsyncRutrackerParser().run())