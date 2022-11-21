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
SESSION = "AQAXNwtVscbdz7UhDbgtuThn2qOQ4YVgW9WtAhG4jFVWqynltWD7qcBTb8_x62f7Wvegsx5RAjvFQAQnRLNqwrK47ZwfzTv_X7dZ4NRdTm83xp01mempzNuEBYPLZ7qDYoeY_d37KaLUVVN6zeQwBl9NKCN5nZBzzF2cLT_wV4gsbDN0F6CkTY8pMywe_xcaoP_73kERHKLP4nGDG95ZkTWjWmF9xhvUW9b4xtjxUETMdVebGxueb-sJuqoLqt28ARZ_GMQkLds7evBSDKDTNLEpCFxUZabWB2ybogsSCxvdCuBKo7AtERZNNiI9HR8kiqHDFjW8R-ZCiwvD-viRPL1uWPyD8QA"
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
