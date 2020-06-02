import discord
from discord.ext import commands
from discord.utils import get


class help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command(aliases=['h'])
    async def help(self,ctx,care:str=None):
        embed = discord.Embed(
            title = 'Help',
            colour = discord.Colour.green()
        )
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Request by {ctx.author.name}')
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/711510162183159838/4e3641a9a8e90a3ad5c3e6e8336833ad.webp?size=2048')
        embed.add_field(name=":firecracker: Fun command!",value="`c!dice` `c!fight` `c!say` `c!avatar` `c!yt` `c!info` `c!emoji`",inline=True)
        embed.add_field(name=":computer: Manage Server!",value="`c!create` `c!clear` `c!ban` `c!dm`",inline=True)
        embed.add_field(name=":diamonds: Currency!",value="`c!slot`",inline=True)
        embed.add_field(name=":crossed_swords: Levels!",value="`c!profile`",inline=True)
        embed.add_field(name=":warning: NSFW!",value="`c!hentai`",inline=True)
        embed.add_field(name=":microbe: Covid19!",value="`c!corona`",inline=True)
        if ctx.author.id == 546558917929598978 or ctx.author.id == 507827170261991464:
            embed.add_field(name=":minidisc: Secret commands!",value="`c!snipe`",inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))