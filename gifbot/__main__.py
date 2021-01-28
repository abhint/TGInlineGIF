#!/usr/bin/env python
import os
from telegram import *
from telegram.ext import *
from .cmd import startMsg
from .gif import  gif_inlinequery
from gifbot import BotEnv, logger

# BOT_TOKEN = ""
# "https://mallugifbotcyberbad.herokuapp.com/"

def main() -> None:
    updater = Updater(BotEnv.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(["start", "help", "h"], startMsg))
    dispatcher.add_handler(InlineQueryHandler(gif_inlinequery))
    if BotEnv.ENV:
        logger.info("START WEBHOOKs")
        updater.start_webhook(
            listen="0.0.0.0",
            port=BotEnv.PORT,
            url_path=BotEnv.TOKEN
        )
        updater.bot.set_webhook(url=BotEnv.WEBHOOK + BotEnv.TOKEN)
    else:
        updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
