# main.py
# This file initializes the bot and handles command routing.
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

API_ID = 27309741
API_HASH = "7c2cabcd8d3f982d6f790eef7262890f"
BOT_TOKEN = "7786395475:AAH7id6w1kjl4JIBzoR5ZgvBNfcftLaqSyw"
OWNER_ID = 6037958673
LOG_CHANNEL = -1002112413520

app = Client("kafka_guardian_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_text(
        "**🛡 Welcome to Kafka Guardian Bot 🛡**\n\nProtect your groups from unwanted edits, media, bots, and more.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add Me to Group", url=f"https://t.me/{(await app.get_me()).username}?startgroup=true")],
            [InlineKeyboardButton("👑 My God", user_id=OWNER_ID)],
            [InlineKeyboardButton("📘 Commands", callback_data="open_commands")]
        ])
    )

print("Kafka Guardian Bot is running...")
app.run()
