import re

id_pattern = re.compile(r'^-?\d+$')

def is_enabled(value, default=True):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# -------------------------
# Bot credentials
# -------------------------
API_ID = 34874438
API_HASH = "65ee39d736fb5e345b8e5af3651b3e63"
BOT_TOKEN = "8312925524:AAFvdcUPsfbB1q8NJjq6YxFWzUTPpwYH3LU"
SESSION = "Media_search"

# -------------------------
# Admins
# -------------------------
ADMINS = [1466559542]  # Your Telegram ID

# -------------------------
# Channels & Groups
# -------------------------
CHANNELS = [-1002908058571]  # Channels bot will listen to
CHNL_LNK = "https://t.me/tamilmoviesdownloadtorrent"
FILE_STORE_CHANNEL = [-1003404536256]  # Where bot stores files
GRP_LNK = "https://t.me/+s4wwf5daeWRmOGJl"  # Support group link

# -------------------------
# Logging
# -------------------------
LOG_CHANNEL = -1003462534811  # Bot logs activities here

# -------------------------
# Request & Support
# -------------------------
REQST_CHANNEL = -1003188863036  # Requests channel
SUPPORT_CHAT = "https://t.me/+s4wwf5daeWRmOGJl"
TUTORIAL = "https://t.me/howtodownloadtlink/11"

# -------------------------
# Shortlink
# -------------------------
SHORTLINK_URL = "nowshort.com"
SHORTLINK_API = "db1a78fe2ca155e01d4212b4efee308e5fbacadc"

# -------------------------
# Bot settings
# -------------------------
CACHE_TIME = 300
USE_CAPTION_FILTER = True
CUSTOM_FILE_CAPTION = "Media Search Bot"

# -------------------------
# Optional features
# -------------------------
AUTO_DELETE = True
SINGLE_BUTTON = True
IMDB = False
SPELL_CHECK_REPLY = True

# -------------------------
# MongoDB
# -------------------------
DATABASE_URI = "mongodb+srv://ajayneymar14_db_user:sAf60CbCxOW0nUll@cluster0.tuasfws.mongodb.net/?appName=Cluster0"
DATABASE_NAME = "ajayneymar14_db_user"
COLLECTION_NAME = "Telegram_files"

# -------------------------
# Languages & Qualities
# -------------------------
LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada", "gujarati", "marathi", "punjabi"]
QUALITIES = ["360P", "480P", "720P", "1080P", "1440P", "2160P"]

# -------------------------
# Log message summary
# -------------------------
LOG_STR = f"""
Bot Configurations:
- IMDB Results: {"Enabled" if IMDB else "Disabled"}
- Single Button: {"Enabled" if SINGLE_BUTTON else "Disabled"}
- Auto Delete: {"Enabled" if AUTO_DELETE else "Disabled"}
- Spell Check Reply: {"Enabled" if SPELL_CHECK_REPLY else "Disabled"}
- Custom Caption: {CUSTOM_FILE_CAPTION}
"""
