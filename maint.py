from telethon import TelegramClient, events
import asyncio
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
bot_token = os.environ.get("bot_token")

bot = TelegramClient("bot", API_ID, API_HASH)

@bot.on(events.NewMessage(pattern="/start"))
async def handler(event):
    await event.reply("Bot is alive!")

async def main():
    await bot.start(bot_token=bot_token)
    print("✅ Bot is running...")
    await bot.run_until_disconnected()

asyncio.run(main())
