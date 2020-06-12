import discord
from discord.ext import commands
from discord.utils import get
import time
import random


class fight(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def fight(self,ctx,enemy:discord.Member):
        if(enemy.id == ctx.author.id):
            return await ctx.send("PEW~!, You're suicide")
        if(enemy.id == 711510162183159838):
            return await ctx.send("Yay~ I won becuz i'm committee")
        await ctx.message.delete()
        p1icon = ctx.author.avatar_url
        p2icon = enemy.avatar_url
        p1 = ctx.author.name
        p2 = enemy.name
        firstem = discord.Embed(
            colour = discord.Color.red(),
            title = "Fight is coming",
        )
        sec = discord.Embed(
            colour = discord.Color.orange(),
            title =f"{p1} _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
        )
        VS = discord.Embed(
            colour = discord.Color.green(),
            title =f" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ VS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
        )
        thi = discord.Embed(
            colour = discord.Color.blue(),
            title =f"{p2} _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
        )
        sec.set_thumbnail(url=p1icon)
        thi.set_thumbnail(url=p2icon)
        await ctx.send(embed=firstem)
        await ctx.send(embed=sec)
        await ctx.send(embed=VS)
        await ctx.send(embed=thi)
        msg = await ctx.send("Punching")
        time.sleep(0.4)
        whowin = random.randint(0,2)
        if(whowin == 2):
            win = discord.Embed(
                title = ctx.author.name,
                description = f"Yay!~{ctx.author.name} is won!",
                colour = discord.Colour.blue()
            )
            win.set_thumbnail(url=ctx.author.avatar_url)
            win.set_footer(icon_url=enemy.avatar_url,text="OOF")
            await msg.edit(embed=win)
        else:
            win = discord.Embed(
                title = enemy.name,
                description = f"Yay!~{enemy.name} is won!",
                colour = discord.Colour.blue()
            )
            win.set_thumbnail(url=enemy.avatar_url)
            win.set_footer(icon_url=ctx.author.avatar_url,text="OOF")
            await msg.edit(embed=win)
    @fight.error
    async def fight_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = "ERROR",
                color = discord.Colour.red()
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/711570460487450687/720820208545169438/cheerchan_sad.png")
            embed.add_field(name="Hmm.. Something went wrong? Please try again \nc!fight <user>",value="_ _",inline=True)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("😳")


def setup(bot):
    bot.add_cog(fight(bot))