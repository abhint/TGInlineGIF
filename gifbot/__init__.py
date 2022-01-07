"""
Copyright 2021 ABHIJITH N T
"""
import logging
import os
from dotenv import load_dotenv
from telegram import *

load_dotenv()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logging.getLogger('telegram').setLevel(logging.WARNING)


def logger(logs) -> logging.Logger:
    return logging.getLogger(logs)


# tenor key
KEY = os.environ.get('TENOR_KEY', "TJM4IZHZNUZ1")

# Telegram requirements

BOT_TOKE = os.environ.get('BOT_TOKEN')

START = "You can use me in inline mode and search for available GIFS."
WL_GIF = "https://telesco.pe/AbhijithNT/1427"
MSG_KEYBOARD = [
    [
        InlineKeyboardButton(
            text="Search Inline",
            switch_inline_query_current_chat=" "
        )
    ],
    [
        InlineKeyboardButton(
            text="📚 Source",
            url="https://github.com/abhint/TGInlineGIF"
        )
    ]
]
