from telegram.ext import *
from .cmd import start_message
from .gif import gif_inline_query
from gifbot import logger, BOT_TOKE, PORT, WEBHOOK_URL

init_logger = logger(__name__)


def main() -> None:
    updater = Updater(BOT_TOKE, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(["start", "help", "h"], start_message))
    dispatcher.add_handler(InlineQueryHandler(gif_inline_query))
    # updater.start_webhook(
    #     webhook_url=WEBHOOK_URL,
    #     port=PORT
    # )
    init_logger.info('Bot is start')
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
