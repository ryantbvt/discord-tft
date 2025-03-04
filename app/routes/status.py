''' DEPRECATED: Functions to fetch riot status pages '''

import requests

from discord.ext import commands
from python_utils.logging import logging
from utils import args, fetch_secrets

logger = logging.init_logger()

# load configs
start_args = args.parse_args()
secrets = fetch_secrets.fetch_tokens(start_args.source)

RIOT_TOKEN = secrets['riot_token']
RIOT_URL = secrets['riot_url']

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tft-status')
    async def tft_status(self, ctx):
        logger.info('tft-status command received')

        endpoint = RIOT_URL + '/tft/status/v1/platform-data'

        try:
            logger.info(f'Calling endpoint: {endpoint}')
            resp = requests.get(endpoint, headers={
                'X-Riot-Token': RIOT_TOKEN
            })
            resp.raise_for_status()

        except requests.exceptions.HTTPError as http_err:
            logger.error(f'HTTP error occurred: {http_err}')  # Log HTTP errors (e.g., 404, 500)
        except requests.exceptions.RequestException as req_err:
            logger.error(f'Request exception occurred: {req_err}')  # Log other request-related errors (e.g., connection issues)
        except Exception as e:
            logger.error(f'An unexpected error occurred: {e}')  # Log any other exceptions
            return

        status_info = resp.json()

        if len(status_info['maintenances']) == 0:
            await ctx.send('All servers are funtional')
        
        else:
            await ctx.send('Servers in maintenance')

        logger.info('Completed tft-status command')

    @commands.command(name='lol-status')
    async def lol_status(self, ctx):
        logger.info('lol-status command received')

        endpoint = RIOT_URL + '/lol/status/v4/platform-data'

        try:
            logger.info(f'Calling endpoint: {endpoint}')
            resp = requests.get(endpoint, headers={
                'X-Riot-Token': RIOT_TOKEN
            })
            resp.raise_for_status()

        except requests.exceptions.HTTPError as http_err:
            logger.error(f'HTTP error occurred: {http_err}')  # Log HTTP errors (e.g., 404, 500)
        except requests.exceptions.RequestException as req_err:
            logger.error(f'Request exception occurred: {req_err}')  # Log other request-related errors (e.g., connection issues)
        except Exception as e:
            logger.error(f'An unexpected error occurred: {e}')  # Log any other exceptions
            return

        status_info = resp.json()

        if len(status_info['maintenances']) == 0:
            await ctx.send('All servers are funtional')
        
        else:
            await ctx.send('Servers in maintenance')

        logger.info('Completed lol-status command')

async def setup(bot):
    await bot.add_cog(Status(bot))