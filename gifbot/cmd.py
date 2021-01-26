from telegram import *
from telegram.ext import *

def startMsg(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi!')

