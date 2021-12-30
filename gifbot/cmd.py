from telegram import *
from telegram.ext import *
from gifbot import START, WL_GIF, MSG_KEYBOARD


def start_message(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=f"Hi <b>{update.effective_chat.first_name}</b> 😅"
             f"\n{START}"
             f"\n\n{WL_GIF}",
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(MSG_KEYBOARD)
    )
