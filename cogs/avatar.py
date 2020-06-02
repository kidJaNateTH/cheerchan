import discord
from discord.ext import commands
from discord.utils import get


class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def avatar(self,ctx,member:discord.Member=None):
        name = ctx.author.name
        if(member == None):
            embed = discord.Embed(
                title =f"Avatar",
                description=f"{name}'s",
                colour = discord.Colour.magenta()
            )
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            othername = member.name
            embed = discord.Embed(
                title =f"Avatar",
                description=f"{othername}'s",
                colour = discord.Colour.magenta()
            )
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(avatar(bot))