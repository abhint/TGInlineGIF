from telegram import *
from telegram.ext import *

from gifbot import gifBot
from gifbot import Msg

bot = gifBot.Bot  # GET


def startMsg(update: Update, context: CallbackContext) -> None:
    bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=Msg.WL_GIF,
        duration=1.47,
        width=376,
        height=200,
        caption=f"Hi <b>{update.effective_chat.username}</b>{Msg.START}",
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(Msg.keyboard),
    )
