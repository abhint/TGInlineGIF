from telegram.ext import *
from .cmd import start_message
from .gif import gif_inline_query
from gifbot import logger, BOT_TOKE

init_logger = logger(__name__)


def main() -> None:
    updater = Updater(BOT_TOKE, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(["start", "help", "h"], start_message))
    dispatcher.add_handler(InlineQueryHandler(gif_inline_query))
    init_logger.info('Bot is Online!')
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
