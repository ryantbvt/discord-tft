import asyncio

from python_utils.logging import logging
import startup

# create logger
logger = logging.init_logger()

# start the application
logger.info("Starting application...")

if __name__ == '__main__':
    asyncio.run(startup.run_discord_bot())

logger.warning('Application stopping')