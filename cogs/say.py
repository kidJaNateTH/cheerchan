import discord
from discord.ext import commands
from discord.utils import get


class say(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def steal(self,ctx,member:discord.Member):
        await ctx.send(member.avatar_url)
    @commands.command()
    async def say(self,ctx,*,msg):
        if(ctx.author.id == 546558917929598978):
            await ctx.message.delete()
            name = ctx.author.name
            text = "{}" .format(msg)
            embed = discord.Embed(
                title = f'Cheer Chan is say something',
                description = text
            )
            embed.set_footer(icon_url='https://cdn.discordapp.com/avatars/711510162183159838/4e3641a9a8e90a3ad5c3e6e8336833ad.webp?size=1024',text=f"Request by Cheer Chan (I'm not bot anymore)")
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            name = ctx.author.name
            text = "{}" .format(msg)
            embed = discord.Embed(
                title = f'{name} is say something',
                description = text
            )
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Request by {ctx.author.name}')
            await ctx.send(embed=embed)

    @say.error
    async def say_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = "ERROR",
                color = discord.Colour.red()
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/711570460487450687/720820208545169438/cheerchan_sad.png")
            embed.add_field(name="Hmm.. Something went wrong? Please try again \nc!say <str>",value="_ _",inline=True)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("😳")

def setup(bot):
    bot.add_cog(say(bot))