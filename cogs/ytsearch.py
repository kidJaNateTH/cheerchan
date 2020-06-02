import discord
from discord.ext import commands
from discord.utils import get
import urllib.parse, urllib.request, re


class ytsearch(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['yts', 'find','yt'])
    async def youtube(self,ctx, *,search):
        query_string = urllib.parse.urlencode({
           'search_query' : search
        })
        htm_content = urllib.request.urlopen(
           'http://www.youtube.com/results?'+ query_string
        )
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        result = 'http://www.youtube.com/watch?v=' + search_results[0]
        videopng = f"http://i3.ytimg.com/vi/{result[31:]}/hqdefault.jpg"
        print(videopng)

        embed = discord.Embed(
            title = "Youtube",
            colour = discord.Colour.red()
        )
        embed.add_field(name=f"{search}",value=f"[[Watch this video]]({result})",inline=True)
        embed.set_thumbnail(url=videopng)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🥰')
    @youtube.error
    async def ytsearch_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Hmm.. Something went wrong? Please try again \n`c!yt <str>`")
            await msg.add_reaction("😳")



def setup(bot):
    bot.add_cog(ytsearch(bot))