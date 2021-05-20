"""
Copyright 2021 ABHIJITH N T
"""
import logging, os
from telegram import *
from telegram.ext import *
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


class BotEnv():
    ENV = bool(os.environ.get('ENV', False))
    try:
        if ENV:
            TOKEN = os.environ.get('BOT_TOKEN')
            WEBHOOK = os.environ.get('WEBHOOK')
            PORT = int(os.environ.get("PORT", "1234"))
        else:
            from sample_config import config
            TOKEN = config.BOT_TOKEN
    except KeyError:
        logger.error('One or more configuration values are missing exiting now.')
        exit(1)
class gifBot:
    Bot = Bot(BotEnv.TOKEN)

class Msg:
    START = " 😅\nYou can use me in InLine mode and search for available GIFS.\n"
    WL_GIF = "https://media.tenor.com/images/baebd65d376f80120d6d008139f76a16/tenor.gif"
    keyboard = [
        [
            InlineKeyboardButton(
                text = "Search Inline",
                switch_inline_query_current_chat = ""
                )
            ],
            [
                InlineKeyboardButton(
                text = "📚 Source",
                url = "https://github.com/AbhijithNT/TGInlineGIF/"
                )
            ]
        ]


