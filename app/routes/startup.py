import os
import discord

from python_utils.logging import logging
from utils import args
from dotenv import load_dotenv

# Create logger
logger = logging.init_logger()

def run_discord_bot():
    '''
    Description: Runs application

    Args: None

    Returns: None
    '''
    logger.info('Fetching tokens to start discord client')

    start_args = args.parse_args()
    
    secrets = fetch_tokens(start_args.source)
    discord_token = secrets['discord_token']
    
    logger.info('Secrets fetched')

    logger.info('Create discord client')

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    client.run(discord_token)
    

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
        TOKEN = os.getenv('TOKEN')

    logger.info("Successfully obtained token")

    secrets['discord_token'] = TOKEN

    logger.info("Returning secrets")
    return secrets