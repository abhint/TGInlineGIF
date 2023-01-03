from telegram.ext import *
from .cmd import start_command
from .gif import gif_inline_query
from gifbot import logger, BOT_TOKE, WEBHOOK_URL, PORT

init_logger = logger(__name__)


def main() -> None:
    application = Application.builder().token(BOT_TOKE).build()
    application.add_handler(CommandHandler(["start", "help", "h"], start_command))
    application.add_handler(InlineQueryHandler(gif_inline_query))
    application.run_webhook(
        port=PORT,
        webhook_url=WEBHOOK_URL,
    )
    # application.run_webhook(
    #     webhook_url=WEBHOOK_URL,
    #     port=PORT,
    #     # url_path=BOT_TOKE,
    #     # webhook_url=f'{WEBHOOK_URL}/{BOT_TOKE}',
    # )
    init_logger.info('Bot is start')


if __name__ == '__main__':
    main()
