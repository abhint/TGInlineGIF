"""
Copyright 2021 ABHIJITH N T
"""
import logging, os
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


class Bot():
    ENV = bool(os.environ.get('ENV', False))
    try:
        if ENV:
            TOKEN = os.environ.get('BOT_TOKEN')
        else:
            from sample_config import config
            TOKEN = config.BOT_TOKEN
    except KeyError:
        logger.error('One or more configuration values are missing exiting now.')
        exit(1)
