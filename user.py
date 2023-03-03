from pyrogram import Client

from config import APP_ID, API_HASH, SESSION_STRING

userbot = Client(
    name="userbot",
    session_string=SESSION_STRING,
    api_id=APP_ID,
    api_hash=API_HASH
)