import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

load_dotenv()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message):
    await message.answer("Hello! I'm your bot. Send /help for commands.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
