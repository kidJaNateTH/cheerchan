import discord
from discord.ext import commands
from discord.utils import get


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot=bot





def setup(bot):
    bot.add_cog(ping(bot))