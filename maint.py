from telethon events
import asyncio
import os
from maouconfig import bot
import speedtest

@bot.on(events.NewMessage(from_users=my_id, pattern="^/start$"))
async def handler(event):
    await event.reply("Bot is alive!")

@bot.on(events.NewMessage(from_users=my_id, pattern=r"^/ispeed$"))
async def check_internet_speed(event):
    msg = await event.reply("📡 Testing connection speed... Please wait.")

    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download()
        upload_speed = st.upload()
        ping = st.results.ping

        # Convert to Mbps
        download_mbps = download_speed / 1_000_000
        upload_mbps = upload_speed / 1_000_000

        result = (
            f"📶 **Connection Speed Test Results**\n\n"
            f"📥 Download: `{download_mbps:.2f} Mbps`\n"
            f"📤 Upload: `{upload_mbps:.2f} Mbps`\n"
            f"📡 Ping: `{ping:.2f} ms`"
        )
        await msg.edit(result)

    except Exception as e:
        await msg.edit(f"❌ Failed to check speed:\n`{str(e)}`")
        
async def main():
    await bot.start(bot_token=bot_token)
    print("✅ Bot is running...")
    await bot.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}") 
