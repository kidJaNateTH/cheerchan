import discord
from discord.ext import commands
from discord.utils import get


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def ping(self,ctx):
        msg = await ctx.send("Pinging...")
        await msg.edit(content = f":ping_pong: Pong!~ {round(self.bot.latency * 1000)}ms.")





def setup(bot):
    bot.add_cog(ping(bot))