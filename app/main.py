from python_utils.logging import logging
from routes import startup

# create logger
logger = logging.init_logger()

# start the application
logger.info("Starting application...")

startup.run_discord_bot()

logger.warn('Application stopping')