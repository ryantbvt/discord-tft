''' Fetch configs '''

import os

from python_utils.logging import logging
from dotenv import load_dotenv

logger = logging.init_logger()

def fetch_tokens(run_type: str):
    '''
    Description: Fetches secret tokens

    Args:
        run_type: defines method of fetching configs

    Returns:
        secrets: list of secrets needed to run the bot
    '''
    logger.info("Running fetch_tokens")

    secrets = {
        "discord_token": None
    }

    if run_type == "container":
        logger.info("Fetching tokens from config.yaml")
        pass

    else:
        logger.info("Fetching tokens from .env")

        load_dotenv()
        DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

    logger.info("Successfully obtained token")

    secrets['discord_token'] = DISCORD_TOKEN

    logger.info("Returning secrets")
    return secrets