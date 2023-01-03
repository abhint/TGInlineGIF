from telegram import *
from gifbot import KEY
from .fetch_gif import Fetch

gif = Fetch(key=KEY)


async def gif_inline_query(update: Update, _) -> None:
    query = update.inline_query.query
    if query == "":
        await update.inline_query.answer(gif.get_gif())
    else:
        await update.inline_query.answer(gif.get_gif(query))
