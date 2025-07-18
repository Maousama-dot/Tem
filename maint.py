import os
from telethon import TelegramClient, events

# Optional: Load from .env in local testing (Render doesn't need this)
load_dotenv()

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("Hello! I’m alive and running on Render!")

print("Bot is running...")
bot.run_until_disconnected()
