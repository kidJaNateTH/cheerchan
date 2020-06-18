import discord
from discord.ext import commands
import json


class PROMOTE(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def promote(self,ctx,*,text:str):
        if ctx.guild.id == 719837288670167100:
            return
        embed = discord.Embed(
            description = f"{ctx.guild.name}, Your server has sent to <#723162497602813983> !,Everyone in my server will see it in soon",
            colour = discord.Colour.green()
        )
        await ctx.send(embed=embed)

        embed1 = discord.Embed(
            title = ctx.guild.name,
            colour = discord.Colour.green()
        )
        server_invite = await ctx.channel.create_invite(max_age = 9999)
        embed1.add_field(name="Content : ",value=text,inline=False)
        embed1.add_field(name="Server Invite : ",value=server_invite,inline=False)
        embed1.add_field(name="Server Owner : ",value=f"<@!{ctx.guild.owner.id}>",inline=False)
        embed1.add_field(name="Server Members : ",value=f"{ctx.guild.member_count} Members",inline=False)
        embed1.set_thumbnail(url=ctx.guild.icon_url)
        await self.bot.get_guild(719837288670167100).get_channel(723162497602813983).send(embed=embed1)
    
    @promote.error
    async def promote_error(self,ctx,error):
        with open('servers.json','r',encoding='utf8') as f:
            load = json.load(f)
            prefix = load[str(ctx.guild.id)]['prefix']
            if isinstance(error,commands.MissingRequiredArgument):
                await ctx.send(f"{prefix}promote <text>")
            if isinstance(error,commands.MissingPermissions):
                await ctx.send(f"You don't have permissions to do that")


def setup(bot):
    bot.add_cog(PROMOTE(bot))