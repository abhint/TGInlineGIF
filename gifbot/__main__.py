from telegram.ext import *
from .cmd import start_message
from .gif import gif_inline_query
from gifbot import logger, BOT_TOKE, PORT, WEBHOOK_URL

init_logger = logger(__name__)


def main() -> None:
    updater = Updater(BOT_TOKE, use_context=True)
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
