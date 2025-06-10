import os

import asyncpg
from dotenv import load_dotenv

load_dotenv()


class TorrentRepository:
    def __init__(self):
        self.connection = None
        self.db_config = {
            'host': os.getenv('POSTGRES_HOST', 'localhost'),
            'database': os.getenv('POSTGRES_DB', 'rutracker'),
            'user': os.getenv('POSTGRES_USER', 'postgres'),
            'password': os.getenv('POSTGRES_PASSWORD', 'postgres'),
            'port': os.getenv('POSTGRES_PORT', '5432')
        }

    async def __aenter__(self):
        """Establish a connection to the database when entering the context."""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close the database connection when exiting the context."""
        await self.close()

    async def connect(self):
        """Establish a connection to the database."""
        self.connection = await asyncpg.connect(
                host=self.db_config['host'],
                database=self.db_config['database'],
                user=self.db_config['user'],
                password=self.db_config['password'],
                port=self.db_config['port'])

    async def close(self):
        """Close the database connection."""
        if self.connection:
            await self.connection.close()

    async def search_by_torrent_name_and_category(self, torrent_name, category, subcategory):
        """
        Search for torrents where the name contains the given text, and matches the specified category and subcategory.
        :param torrent_name: The text to search for in the torrent name.
        :param category: The category to filter by.
        :param subcategory: The subcategory to filter by.
        :return: A list of matching torrents.
        """
        query = f"""
        SELECT * FROM torrents
        WHERE torrent ILIKE '%{torrent_name}%'
        AND category = '%{category}%'
        AND subcategory = '%{subcategory}%';
        """
        return await self.connection.fetch(query, f'%{torrent_name}%', category, subcategory)

    async def search_with_category_and_subcategory(self, category, subcategory, torrent_name):
        """
        Search for torrents that match the specified category, subcategory, and optional text in the name.
        :param category: The category to filter by.
        :param subcategory: The subcategory to filter by.
        :param torrent_name: Optional text to search for in the torrent name.
        :return: A list of matching torrents.
        """
        query = f"""
        SELECT * FROM torrents
        WHERE category = '%{category}%'
        AND subcategory = '%{subcategory}%'
        AND torrent ILIKE '%{torrent_name}%';
        """
        return await self.connection.fetch(query, category, subcategory, torrent_name)

    async def search_by_torrent_name(self, torrent_name):
        """
        Search for torrents that match the specified torrent name.
        :param torrent_name: The name of the torrent to search for.
        :return: A list of matching torrents.
        """
        query = f"""
        SELECT * FROM torrents
        WHERE torrent ILIKE '%{torrent_name}%';
        """
        return await self.connection.fetch(query)

    async def create_table(self):
        """
        Create the 'torrents' table with GIN index on 'torrent' column for full-text search
        and indexes on 'category' and 'subcategory' columns.
        """
        query = """
        CREATE TABLE IF NOT EXISTS torrents (
            id SERIAL PRIMARY KEY,
            category TEXT,
            subcategory TEXT,
            torrent TEXT,
            magnet_link TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        -- Create GIN index on 'torrent' column for full-text search
        CREATE INDEX IF NOT EXISTS idx_torrent_gin ON torrents USING GIN (to_tsvector('english', torrent));

        -- Create indexes on 'category' and 'subcategory' columns
        CREATE INDEX IF NOT EXISTS idx_category ON torrents (category);
        CREATE INDEX IF NOT EXISTS idx_subcategory ON torrents (subcategory);
        """
        await self.connection.execute(query)

    async def insert_batch(self, data, chunk_size=1000):
        """
        Insert a batch of data into the 'torrents' table in chunks.
        :param data: A list of tuples, where each tuple contains (category, subcategory, torrent, magnet_link).
        :param chunk_size: The number of records to insert in each chunk (default: 1000).
        """
        if data:
            async with self.connection.transaction():
                for i in range(0, len(data), chunk_size):
                    chunk = data[i:i + chunk_size]
                    await self.connection.executemany(
                        """INSERT INTO torrents 
                           (category, subcategory, torrent, magnet_link) 
                           VALUES ($1, $2, $3, $4)""",
                        chunk
                    )

#TODO: для отладки - убить
if __name__ == '__main__':
    import asyncio

    async def main():
        async with TorrentRepository() as repo:
            torrents = await repo.search_by_torrent_name("Chemical")

            print("!!! torrents: ", torrents)

    asyncio.run(main())