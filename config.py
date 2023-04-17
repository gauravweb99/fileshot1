#(©)CodeXBotz

import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get(
  "TG_BOT_TOKEN", "5913605784:AAGN_lfvKjS9V4_qWPBvUgU_YM9DUg_FFTE")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "17850184"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a9607d2b34098b079b6365db3131fd6e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", " -1001712307513"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1230839024"))

#Port
PORT = os.environ.get("PORT", None)

#Database
DB_URI = os.environ.get(
  "DATABASE_URL",
  "mongodb+srv://manju:1234@cluster0.s6qpf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot6")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001344341956"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get(
  "START_MESSAGE",
  "👋 Hello {first}\nI can store private files in Specified Channel and other users can access it from special link."
)
try:
  ADMINS = []
  for x in (os.environ.get("ADMINS", "5863383503").split()):
    ADMINS.append(int(x))
except ValueError:
  raise Exception("Your Admins list does not contain valid integers.")

#Force sub message
FORCE_MSG = os.environ.get(
  "FORCE_SUB_MESSAGE",
  "👋 Hello {first}\n<b>😓 You need to join in my Channel/Group to use me\n😋 Kindly Please join Channel</b>"
)

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT',
                                         "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
  DISABLE_CHANNEL_BUTTON = True
else:
  DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = ""

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
  level=logging.INFO,
  format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
  datefmt='%d-%b-%y %H:%M:%S',
  handlers=[
    RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
    logging.StreamHandler()
  ])
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
  return logging.getLogger(name)
