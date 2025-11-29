from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "24720814"))
API_HASH = getenv("API_HASH", "0c6bf0f5cfd7bdcce6f607d15f9896e6")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "7738449961"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://rarebit100_db_user:<db_password>@krish.vkgjvmb.mongodb.net/?appName=Krish")
MUST_JOIN = getenv("MUST_JOIN", "ITSZSHUKLA")
START_IMG = getenv("START_IMG", "https://files.catbox.moe/520y6h.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "rarebit_gamers")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "KRISH_KAPOOR_SPAM")
