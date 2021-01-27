from uuid import uuid4
from telegram.ext import CallbackContext
from telegram import *
from .fetch_gif import gif


def gif_inlinequery(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    if query == "":
        update.inline_query.answer(gif.DEFAULT_GIF)
    else:
        update.inline_query.answer(gif.search_gif(query))
