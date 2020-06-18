import discord
from discord.ext import commands


class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        ctx = guild.system_channel
        emoji=discord.utils.get(self.bot.emojis,name="yellow_sparksidk")
        embed = discord.Embed(
            colour = discord.Colour.green(),
            title = f"Hi, {guild.name}",
            description = f"{emoji}Thank you for invite me to {guild.name} server!{emoji}\nYou can read the instructions and commands by typing __c!help__\nIf you have questions about the use of Cheer Chan, You can ask at\nCheer Chan Support server : https://discord.gg/MVwkZt7 \n\n\nThank you ❤ - Cheer Chan"
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        ctx = guild.system_channel
        embed = discord.Embed(
            colour = discord.Colour.light_grey(),
            title = f"Good bye, {guild.name}",
            description = f"Bye, I hope you will invite me later"
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(welcome(bot))