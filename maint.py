from telethon events
import asyncio
import os
from maouconfig import bot

@bot.on(events.NewMessage(pattern="/start"))
async def handler(event):
    await event.reply("Bot is alive!")

async def main():
    await bot.start(bot_token=bot_token)
    print("✅ Bot is running...")
    await bot.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}") 
