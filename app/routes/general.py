''' General API commands irrelevant to the core functions of the bot '''

import discord

from discord.ext import commands
from python_utils.logging import logging

logger = logging.init_logger()

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx):
        logger.info('hello command recieved')
        await ctx.send('Hello world!')

async def setup(bot):
    await bot.add_cog(General(bot))