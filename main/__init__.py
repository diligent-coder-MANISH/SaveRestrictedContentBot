#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 4805297
API_HASH = "cef82fd6ab4198c068dc0efd8d7b195d"
BOT_TOKEN = "5518882176:AAEKuV3tpnpTbjSFdKKTybaprvS2Fjdx0N8"
SESSION = "AQCi_rsBfzo7wh8O5KAa5J8wVr3WrMLjpCBG7hJHeh0KgZdGC0vkzAIWE0jxBr8eR4WvyT06Ea0K6ke-ijfwHmHwqmsSKhX68-XVyxyy6eAZxYpBLI9efRqwco_ttTdqdOlp-NyJM0XLAdXKVMijl9qs3nPO4qmmm0i3kDi0CuCHF968e8QsPS6EJ589tFk690aFIeUXl9zAyyncIKOy0m43GodgSCP6B78bw68e9wsUk9rqztAPpY6EpvK0RJHmWqy5ZRYCOraDOz9-pb8yT7yFvHK9Kc4-RlfOHf4OmkrxBH4XaudhPLqsgKlg-RA3yu04rVTWW2AvaXEJOwdvYIK9WPyD8QA"
FORCESUB = "savecontbot"
AUTH = 1492943857

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
