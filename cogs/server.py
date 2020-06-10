import discord
from discord.ext import commands


class SERVER(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['servinfo','server'])
    async def serverinfo(self,ctx):
        server = ctx.guild
        server_name = server.name
        server_id = server.id
        server_owner = server.owner.name
        icon_url = ctx.guild.icon_url
        x = server.members
        embed = discord.Embed(
            title = server_name,
            colour = discord.Colour.green()
        )
        embed.set_thumbnail(url=icon_url)
        embed.add_field(name="Server name",value=server_name,inline=True)
        embed.add_field(name="Server id",value=server_id,inline=True)
        embed.add_field(name="Owner",value=server_owner,inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(SERVER(bot))