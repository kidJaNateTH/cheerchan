import discord
from discord.ext import commands


class message(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_message(self,message):
        if "OwO" in message.content:
            await message.channel.send("I know that")


def setup(bot):
    bot.add_cog(message(bot))