import discord
from discord.ext import commands
from discord.utils import get


class sent(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def dm(self,ctx,dm:discord.Member,*,text:str):
        user = self.bot.get_user(dm.id)
        await user.send(text)
        await ctx.send(f'"{text}" has sent! to {dm.name}')

    @commands.command()
    async def se(self,ctx,dm:discord.Member,*,text:str):
        if ctx.author.id != 546558917929598978:
            return
        user = self.bot.get_user(dm.id)
        await user.send(text)
        await ctx.send(f'"{text}" has sent! to {dm.name}')
        await ctx.channel.purge(limit=2)
    @dm.error
    async def dm_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Hmm.. Something went wrong? Please try again \n`c!dm <user> <text>`")
            await msg.add_reaction("😳")
        if isinstance(error,commands.MissingPermissions):
            msg = await ctx.send(f"Hmm.. I think you need more poppy")
            await msg.add_reaction("😢")





def setup(bot):
    bot.add_cog(sent(bot))