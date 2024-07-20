''' TFT related APIs '''

import httpx
import discord

from discord.ext import commands
from python_utils.logging import logging

logger = logging.init_logger()

class TftAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='top-units')
    async def top_tft_units(self, ctx, args: str):
        logger.info('top-units command received')

        # TODO: change this to a config
        endpoint = 'http://localhost:4460/v1/tft/top-champ'

        try:
            logger.info(f'Calling endpoint: {endpoint}')

            username, tag_line = args.split('#', 1)

            payload = {
                "username": username,
                "tag_line": tag_line
            }

            async with httpx.AsyncClient() as client:
                resp = await client.post(endpoint, json=payload)
                resp.raise_for_status()

            unit_list = resp.json()
            logger.info(f'Received top 5 units for {username}')

            clean_list = []

            # re-formats the strings
            for unit in unit_list:
                _, unit_name = unit.split('_', 1)
                clean_list.append(unit_name)

            # Format list in 1 message
            embed = discord.Embed(title=f'Top 5 units used by {username}#{tag_line}', 
                                  description="\n".join(f"- {unit}" for unit in clean_list))
            await ctx.send(embed=embed)
            logger.info('Completed top-units command')

        except httpx.HTTPStatusError as http_err:
            logger.error(f'HTTP error occurred: {http_err}')  # Log HTTP errors (e.g., 404, 500)
        except httpx.RequestError as req_err:
            logger.error(f'Request exception occurred: {req_err}')  # Log other request-related errors (e.g., connection issues)
        except Exception as e:
            logger.error(f'An unexpected error occurred: {e}')  # Log any other exceptions

async def setup(bot):
    await bot.add_cog(TftAPI(bot))