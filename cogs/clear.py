import discord
from discord.ext import commands
from discord.utils import get


class clear(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount:int):
        if(amount <= 0):
            return await ctx.send(f"Hmm... {ctx.author.name}, I think i can't delete {amount} messages, I need more poppy")
        await ctx.channel.purge(limit=amount+1)
    @clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Hmm.. Something went wrong? Please try again \n`c!clear <int>`")
            await msg.add_reaction("😳")
        if isinstance(error,commands.MissingPermissions):
            msg = await ctx.send(f"Hmm.. I think you not have permissions to do that")
            await msg.add_reaction("😢")
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        if(member.id == 711510162183159838):
            return await ctx.send("Uh.. Thanks, But i don't need to ban myself")
        await member.ban(reason=reason)
        embed = discord.Embed(
            title = 'OOF',
            colour = discord.Colour.red(),
            description = f"{member.name} has got banned\n{reason}"
        )
        embed.set_footer(icon_url=member.avatar_url,text=member.name)
        await ctx.send(embed=embed)
    @ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Hmm.. Something went wrong? Please try again \n`c!ban <user>`")
            await msg.add_reaction("😳")
        if isinstance(error,commands.MissingPermissions):
            msg = await ctx.send(f"Hmm.. I think you need more poppy")
            await msg.add_reaction("😢")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        if(member.id == 711510162183159838):
            return await ctx.send("Uh.. Thanks, But i don't need to kick myself")
        await member.kick(reason=reason)
        embed = discord.Embed(
            title = 'OOF',
            colour = discord.Colour.orange(),
            description = f"{member.name} has got kicked\n{reason}"
        )
        embed.set_footer(icon_url=member.avatar_url,text=member.name)
        await ctx.send(embed=embed)
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Hmm.. Something went wrong? Please try again \n`c!kick <user>`")
            await msg.add_reaction("😳")
        if isinstance(error,commands.MissingPermissions):
            msg = await ctx.send(f"Hmm.. I think you not have permissions to do that")
            await msg.add_reaction("😢")


def setup(bot):
    bot.add_cog(clear(bot))