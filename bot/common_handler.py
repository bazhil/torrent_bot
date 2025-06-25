from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "👋 Welcome to Torrent Search Bot!\n\n"
        "You can search torrents:\n"
        "1. Simple search: just type your query\n"
        "Available commands:\n"
        "/start - Show this message\n"
        "/help - Show help\n"
        "/search - Search torrents\n"
    )
    await message.answer(welcome_text)

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "ℹ️ How to use this bot:\n\n"
        "1. Simple search:\n"
        "   Just type what you're looking for and bot will search in all categories\n\n"
        "2. Targeted search:\n"
        "   - Use /search command\n"
        "   - Then enter your search query\n\n"
        "The bot will show you the first 10 results."
    )
    await message.answer(help_text)