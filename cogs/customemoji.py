import discord
from discord.ext import commands
from discord.utils import get


class customemoji(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command(aliases=['emo'])
    async def emoji(self,ctx,e:str):
        await ctx.message.delete()
        await ctx.send(file=discord.File(e+'.png'))
    @emoji.error
    async def emoji_error(self,ctx,error):
        if(error,commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = "Emoji list",
                description = "Emoji not found 404",
                colour = discord.Colour.blue()
            )
            embed.add_field(name="thinking",value="_ _",inline=False)
            embed.add_field(name="thonk",value="_ _",inline=False)
            embed.add_field(name="shooter",value="_ _",inline=False)
            embed.set_footer(text=error)
            await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(customemoji(bot))