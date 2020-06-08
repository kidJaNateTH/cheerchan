import discord
from discord.ext import commands
from discord.utils import get
import random
import asyncio

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def dice(self,ctx):
        result = random.randint(1,6)
        embed = discord.Embed(
            colour = discord.Color.blue()
        )
        embed.set_author(name='Rolling a dice! ⚀')
        await asyncio.sleep(0.1)
        msg = await ctx.send(embed=embed)
        
        embed.set_author(name='Rolling a dice! ⚅')
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed)

        embed.set_author(name='Rolling a dice! ⚂')
        await asyncio.sleep(0.3)
        await msg.edit(embed=embed)
        
        embed.set_author(name='Rolling a dice! ⚁')
        await asyncio.sleep(0.4)
        await msg.edit(embed=embed)

        if result == 1:
            dicebox = "⚀"
        if result == 2:
            dicebox = "⚁"
        if result == 3:
            dicebox = "⚂"
        if result == 4:
            dicebox = "⚃"
        if result == 5:
            dicebox = "⚃"
        if result == 6:
            dicebox = "⚅"

        embed.set_author(name=f'Rolling a dice! {dicebox}')
        embed.add_field(name=f":game_die: The values are {result}",value='_ _',inline=False)
        await asyncio.sleep(0.1)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(dice(bot))