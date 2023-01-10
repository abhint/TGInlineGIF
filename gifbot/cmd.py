from telegram import *
from telegram.ext import *
from gifbot import START, WL_GIF, MSG_KEYBOARD


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=f"Hi <b>{update.effective_chat.first_name}</b> 😅"
             f"\n{START}"
             f"\n\n{WL_GIF}",
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup(MSG_KEYBOARD)
    )
