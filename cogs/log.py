import discord
from discord.ext import commands
import random


class log(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_guild_join(self,guild):

        i = random.randint(1,3)
        if i == 1:
            embed = discord.Embed(
                title = f"I have joined to {guild.name}",
                description = f"Server name : {guild.name}\nServer owner : <@!{guild.owner.id}> `({guild.owner.name})`\nMembers : {guild.member_count}\nCreated at : {guild.created_at}\n",
                colour = discord.Colour.from_rgb(255, 28, 229)
            )
        if i == 2:
            embed = discord.Embed(
                title = f"I have joined to {guild.name}",
                description = f"Server name : {guild.name}\nServer owner : <@!{guild.owner.id}> `({guild.owner.name})`\nMembers : {guild.member_count}\nCreated at : {guild.created_at}\n",
                colour = discord.Colour.from_rgb(31, 255, 248)
            )
        if i == 3:
            embed = discord.Embed(
                title = f"I have joined to {guild.name}",
                description = f"Server name : {guild.name}\nServer owner : <@!{guild.owner.id}> `({guild.owner.name})`\nMembers : {guild.member_count}\nCreated at : {guild.created_at}\n",
                colour = discord.Colour.from_rgb(31, 255, 42)
            )

        servers = str(len(self.bot.guilds))
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=f"{servers} Servers!")
        await self.bot.get_guild(719837288670167100).get_channel(721257084640952351).send(embed=embed)


def setup(bot):
    bot.add_cog(log(bot))