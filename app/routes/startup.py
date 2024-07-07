import discord

from discord.ext import commands
from python_utils.logging import logging
from utils import args, fetch_secrets

# Create logger
logger = logging.init_logger()

async def run_discord_bot():
    '''
    Description: Runs application

    Args: None

    Returns: None
    '''
    logger.info('Fetching tokens to start discord client')

    start_args = args.parse_args()
    secrets = fetch_secrets.fetch_tokens(start_args.source)
    
    discord_token = secrets['discord_token']
    
    logger.info('Secrets fetched')

    logger.info('Create discord client')

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix ='!', intents=intents)

    # Load cogs
    initial_extensions = [
        'routes.general',
        'routes.status'
    ]

    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            logger.info(f'Loaded extension: {extension}')
        except Exception as e:
            logger.error(f'{e}')

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running')
        logger.info('Discord bot running')

    await bot.start(discord_token)
    