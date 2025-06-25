import logging
from aiogram import Router, types
from aiogram.filters import Command
from torrent_repository import TorrentRepository


router = Router()
logger = logging.getLogger(__name__)



@router.message(Command("search"))
async def simple_search(message: types.Message):
    search_query = message.text
    if not search_query or len(search_query) < 3:
        await message.answer("Search query should be at least 3 characters long")
        return

    try:
        async with TorrentRepository() as repo:
            torrents = await repo.search_by_torrent_name(search_query)

        if not torrents:
            await message.answer("No torrents found matching your query")
            return

        response = []
        for idx, torrent in enumerate(torrents[:10]):
            response.append(
                f"{idx})\n"
                f"Category: {torrent.get("category")}\n"
                f"Subcategory: {torrent.get('subcategory')}\n"
                f"Name: {torrent.get("torrent")}\n"
                f"Magnet link: {torrent.get("magnet_link")}\n\n"
            )

        await message.answer(
            f"🔎 Results for '{search_query}':\n\n" +
            "\n\n".join(response)
        )

    except Exception as e:
        logger.error(f"Search error: {e}", exc_info=True)
        await message.answer("An error occurred during search. Please try again.")
