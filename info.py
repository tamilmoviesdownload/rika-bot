import re
from os import environ

id_pattern = re.compile(r'^-?\d+$')

def is_enabled(value, default=True):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot credentials
API_ID = int(environ.get('API_ID', '34874438'))
API_HASH = environ.get('API_HASH', '65ee39d736fb5e345b8e5af3651b3e63')
BOT_TOKEN = environ.get('BOT_TOKEN', '8312925524:AAFvdcUPsfbB1q8NJjq6YxFWzUTPpwYH3LU')
SESSION = environ.get('SESSION', 'Media_search')

# Admins
ADMINS = [int(admin) for admin in environ.get('ADMINS', '1466559542').split()]

# Channels
CHANNELS = [int(ch) for ch in environ.get('CHANNELS', '-1002908058571').split()]
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/tamilmoviesdownloadtorrent')
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '-1003404536256').split()]
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+s4wwf5daeWRmOGJl')

# Logging
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003462534811'))

# Request & support
REQST_CHANNEL = int(environ.get('reqst_channel', '-1003188863036'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+s4wwf5daeWRmOGJl')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/howtodownloadtlink/11')

# Shortlink
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'nowshort.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'db1a78fe2ca155e01d4212b4efee308e5fbacadc')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', 'True'))
CUSTOM_FILE_CAPTION = environ.get('CUSTOM_FILE_CAPTION', "Media Search Bot")

# Optional features
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', 'True'))
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', 'True'))
IMDB = is_enabled(environ.get('IMDB', 'False'))
SPELL_CHECK_REPLY = is_enabled(environ.get('SPELL_CHECK_REPLY', 'True'))

# MongoDB
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Moviebotz:Moviebotz@cluster0.lx3flpa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "tomandjerry")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Languages & qualities
LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada", "gujarati", "marathi", "punjabi"]
QUALITIES = ["360P", "480P", "720P", "1080P", "1440P", "2160P"]

# Log message summary
LOG_STR = f"""
Bot Configurations:
- IMDB Results: {"Enabled" if IMDB else "Disabled"}
- Single Button: {"Enabled" if SINGLE_BUTTON else "Disabled"}
- Auto Delete: {"Enabled" if AUTO_DELETE else "Disabled"}
- Spell Check Reply: {"Enabled" if SPELL_CHECK_REPLY else "Disabled"}
- Custom Caption: {CUSTOM_FILE_CAPTION}
"""
