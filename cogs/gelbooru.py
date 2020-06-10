import discord
from discord.ext import commands
import random
from pygelbooru import Gelbooru


class PIXIV(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(aliases=['gel'])
    async def gelbooru(self,ctx,*,tag:str=None):
        if not ctx.channel.is_nsfw():
            return await ctx.send(f"You must use this command in NSFW channel :warning:")
        if tag == None:
            embed = discord.Embed(
                title = "Gelbooru",
                colour = discord.Colour.red()
            )
            embed.set_thumbnail(url="https://40.media.tumblr.com/92fd16a77543e9cb658517a4d580e50c/tumblr_mrr4tbmgCQ1spvtw5o2_500.png")
            embed.add_field(name="Tag not found",value="[[All tags list]](https://gelbooru.com/index.php?page=tags&s=list)")
            await ctx.send(embed=embed)
            return
        try:
            gelbooru = Gelbooru('3d372e148458ce79ca99619c1b982720e78c5cdc347336960e63d425080de2a5', '563537')
            results = await gelbooru.search_posts(tags=[tag], exclude_tags=['hentai'])
            url = str(results[0])

            embed = discord.Embed(
                title = "Gelbooru",
                colour = discord.Colour.blurple()
            )
            embed.set_image(url=url)
            embed.set_author(name="[Get a link]",url=url)
            embed.set_footer(text=f"Depraved thoughts by {ctx.author.name}",icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "Gelbooru",
                colour = discord.Colour.red()
            )
            embed.set_thumbnail(url="https://40.media.tumblr.com/92fd16a77543e9cb658517a4d580e50c/tumblr_mrr4tbmgCQ1spvtw5o2_500.png")
            embed.add_field(name=f"Not found tag **{tag}**",value="[[All tags list]](https://gelbooru.com/index.php?page=tags&s=list)")
            
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(PIXIV(bot))