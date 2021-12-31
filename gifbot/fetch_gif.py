from typing import Union, Any, Dict

import requests
from telegram import *
from uuid import uuid4
from gifbot import logger


class Fetch:
    """
    :param key: tenor api key
    :param limit: tenor result limit
    """

    def __init__(self, key: str = None, limit: int = 10):
        self.key = key
        self.limit = limit
        self.session = requests.Session()
        self.logger = logger(__name__)

    def _requests(self, keyword: str):
        """
        :param keyword: search
        :return: get tenor result
        """
        key = self.key
        limit = self.limit
        url = 'https://api.tenor.com/v1/search?q=%s&key=%s&limit=%d' % (keyword, key, limit)
        try:
            results = self.session.get(
                url=url
            ).json()
            return results
        except ConnectionError as err:
            self.logger.warning(f'{err}')
            return dict()

    @staticmethod
    def _inline_query(width: int,
                      height: int,
                      gif_url: str,
                      thumb_url: str,
                      title: str) -> InlineQueryResultGif:
        """
        :param width: tenor gif width
        :param height: tenor gif height
        :param gif_url: tenor gif url
        :param thumb_url: gif thumb url
        :param title: gif title
        :return: InlineQueryResultGif
        """
        return InlineQueryResultGif(
            id=str(uuid4()),
            gif_width=width,
            gif_height=height,
            gif_url=gif_url,
            thumb_url=thumb_url,
            title=title,
        )

    def get_gif(self, keyword: str = 'Malayalam') -> list:
        """

        :param keyword: search
        :return: InlineQueryResultGif list
        """
        inline_result: Union[Dict[Any, Any], Any] = []
        results: Union[Dict[Any, Any], Any] = self._requests(keyword)
        if results is False:
            return inline_result
        for result in results.get('results'):
            media = result.get('media')[0].get('mediumgif')
            url = media.get('url')
            width = int(media.get('dims')[0])
            height = int(media.get('dims')[1])
            thumb_url = media.get('url')
            title = result.get('content_description')

            inline_result.append(
                self._inline_query(
                    width=width,
                    height=height,
                    title=title,
                    thumb_url=thumb_url,
                    gif_url=url,

                )
            )
        return inline_result
