import discord
from discord.ext import commands
from discord.utils import get


class brainout(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['create','c'])
    async def createroom(self,ctx,name:str):
        guild = ctx.message.guild
        await guild.create_text_channel(name)
        msg = await ctx.send("Your room has been created")
        await msg.add_reaction("😘")
    @createroom.error
    async def createroom_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Hmm.. Something went wrong? Please try again \n`c!create <str>`")
            await msg.add_reaction("😳")
        if isinstance(error, commands.MissingPermissions):
            msg = await ctx.send(f"Hmm.. I think you need more puppy")
            await msg.add_reaction("😳")


        




def setup(bot):
    bot.add_cog(brainout(bot))