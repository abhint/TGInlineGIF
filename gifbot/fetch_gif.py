import requests
import json
from telegram import *
from uuid import uuid4

URL = "https://api.tenor.com/v1/search?q="
KEY = "TJM4IZHZNUZ1"
LIMIT = 50


class gif:
    DEFAULT_GIF = []
    default_r = requests.get(url=f"{URL}Malayalam&key={KEY}&limit={LIMIT}")
    default_gifs = json.loads(default_r.content)
    for i in range(0, int(default_gifs["next"])):
        DEFAULT_GIF.append(
            InlineQueryResultGif(
                id=uuid4(),
                gif_width=default_gifs["results"][i]["media"][0]["mediumgif"]["dims"][
                    0
                ],
                gif_height=default_gifs["results"][i]["media"][0]["mediumgif"]["dims"][
                    1
                ],
                gif_url=default_gifs["results"][i]["media"][0]["mediumgif"]["url"],
                thumb_url=default_gifs["results"][i]["media"][0]["mediumgif"]["url"],
            )
        )

    def search_gif(search_query):
        SEARCH_GIF = []
        response = requests.get(url=f"{URL}{search_query}&key={KEY}&limit={LIMIT}")
        gifs = json.loads(response.content)
        for i in range(0, int(gifs["next"])):
            SEARCH_GIF.append(
                InlineQueryResultGif(
                    id=uuid4(),
                    gif_width=gifs["results"][i]["media"][0]["mediumgif"]["dims"][0],
                    gif_height=gifs["results"][i]["media"][0]["mediumgif"]["dims"][1],
                    gif_url=gifs["results"][i]["media"][0]["mediumgif"]["url"],
                    thumb_url=gifs["results"][i]["media"][0]["mediumgif"]["url"],
                )
            )
        return SEARCH_GIF
