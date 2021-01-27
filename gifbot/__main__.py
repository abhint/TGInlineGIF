#!/usr/bin/env python
from telegram import *
from telegram.ext import *
from .cmd import startMsg
from .gif import  gif_inlinequery
from gifbot import BotEnv

# BOT_TOKEN = ""

def main() -> None:
    updater = Updater(BotEnv.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(["start", "help", "h"], startMsg))
    dispatcher.add_handler(InlineQueryHandler(gif_inlinequery))
    # updater.start_webhook(
    #     listen="0.0.0.0",
    #     port=8443,
    #     url_path=BOT_TOKEN
    # )
    # updater.bot.set_webhook("" + BOT_TOKEN)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
