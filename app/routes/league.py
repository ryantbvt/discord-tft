''' League related APIs '''

import httpx
import discord

from discord.ext import commands
from python_utils.logging import logging

logger = logging.init_logger()

class LeagueAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='champ-rotation')
    async def champion_rotation(self, ctx):
        logger.info('champ-rotation command received')

        # TODO: change this to a config
        endpoint = 'http://localhost:4460/v1/champ-rotation'

        try:
            logger.info(f'Calling endpoint: {endpoint}')

            async with httpx.AsyncClient() as client:
                resp = await client.get(endpoint)
                resp.raise_for_status()

                champ_list = resp.json()
                logger.info(f'Received champion rotation list')
                
                # Format list in 1 message
                logger.info('Returning champ list to client')
                embed = discord.Embed(title="Free Champion Rotation", description="\n".join(f"- {champion}" for champion in champ_list))
                await ctx.send(embed=embed)
                # champ_list_str = '\n'.join(f'- {champion}' for champion in champ_list)

                # await ctx.send(champ_list_str)


        except httpx.HTTPStatusError as http_err:
            logger.error(f'HTTP error occurred: {http_err}')  # Log HTTP errors (e.g., 404, 500)
        except httpx.RequestError as req_err:
            logger.error(f'Request exception occurred: {req_err}')  # Log other request-related errors (e.g., connection issues)
        except Exception as e:
            logger.error(f'An unexpected error occurred: {e}')  # Log any other exceptions


async def setup(bot):
    await bot.add_cog(LeagueAPI(bot))