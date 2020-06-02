import discord
from discord.ext import commands
from discord.utils import get
import json
import requests
import asyncio
import random


class money(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def money(self,ctx,member:discord.Member=None):
        member = ctx.author if not member else member
        with open ("users.json","r") as f:
            mon = json.load(f)
            author_id = str(ctx.author.id)
            mon[author_id] = {}
            mone = mon[author_id]['nus'] = 0
            member_id = str(member.id)
            if mone == None or mone == 0:
                await ctx.send("You got starter pack\n2000 nus")
            else:
                await ctx.send(f"You have {mone} nus")
    @commands.command()
    async def slot(self,ctx):
        embed=discord.Embed(title="            Slot",color=ctx.author.color)
        embed.add_field(name="_ _",value=":tangerine: :watermelon: :hot_pepper:",inline=True)
        msg=await ctx.send(embed=embed)
        embed.clear_fields()
        await asyncio.sleep(0.2)

        embed.add_field(name="_ _",value=":cherries: :green_apple: :watermelon:",inline=True)
        await msg.edit(embed=embed)
        embed.clear_fields()
        await asyncio.sleep(0.2)

        embed.add_field(name="_ _",value=":green_apple: :watermelon: :hot_pepper:",inline=True)
        await msg.edit(embed=embed)
        embed.clear_fields()
        await asyncio.sleep(0.2)

        embed.add_field(name="_ _",value=":cherries: :cherries: :green_apple:",inline=True)
        await msg.edit(embed=embed)
        embed.clear_fields()
        await asyncio.sleep(0.2)

        embed.add_field(name="_ _",value=":cherries: :green_apple: :watermelon:",inline=True)
        await msg.edit(embed=embed)
        embed.clear_fields()
        await asyncio.sleep(0.5)

        embed.add_field(name="_ _",value=":cherries: :green_apple: :watermelon:",inline=True)
        await msg.edit(embed=embed)
        embed.clear_fields()
        await asyncio.sleep(0.2)

        embed.add_field(name="_ _",value=":green_apple: :watermelon: :hot_pepper:",inline=True)
        await msg.edit(embed=embed)
        embed.clear_fields()
        await asyncio.sleep(0.2)

        embed.add_field(name="_ _",value=":cherries: :cherries: :green_apple:",inline=True)
        await msg.edit(embed=embed)
        embed.clear_fields()
        await asyncio.sleep(0.2)

        num = random.randint(1,5)
        if num == 1:
            slot = discord.Embed(
                title = "Fail",
                colour = discord.Colour.red()
            )
            slot.add_field(name="_ _",value=":cherries: :green_apple: :watermelon:",inline=True)
            await msg.edit(embed=slot)
        if num == 2:
            slot = discord.Embed(
                title = "Success",
                colour = discord.Colour.green()
            )
            slot.add_field(name="_ _",value=":cherries: :cherries: :cherries:",inline=True)
            await msg.edit(embed=slot)
        if num == 3:
            slot = discord.Embed(
                title = "Fail",
                colour = discord.Colour.red()
            )
            slot.add_field(name="_ _",value=":green_apple: :green_apple: :watermelon:",inline=True)
            await msg.edit(embed=slot)
        if num == 4:
            slot = discord.Embed(
                title = "Success",
                colour = discord.Colour.green()
            )
            slot.add_field(name="_ _",value=":watermelon: :watermelon: :watermelon:",inline=True)
            await msg.edit(embed=slot)
        if num == 5:
            slot = discord.Embed(
                title = "Fail",
                colour = discord.Colour.red()
            )
            slot.add_field(name="_ _",value=":watermelon: :green_apple: :green_apple:",inline=True)
            await msg.edit(embed=slot)

    @commands.command()
    async def corona(self,ctx,lang:str=None):
        msg = await ctx.send("Please wait...")
        url = 'https://covid19.th-stat.com/api/open/today'
        try:
            r=requests.get(url)
            if lang == None or lang == 'th':
                if r.ok:
                    embed = discord.Embed(
                        title = 'Covid 19 ในประเทศไทย',
                        colour = discord.Colour.green()
                    )
                    j=json.loads(r.text)
                    embed.add_field(name="ข้อมูลวันที่",value=j['UpdateDate'],inline=False)
                    embed.add_field(name="ติดเซื้อสะสม: ",value=j['Confirmed'],inline=False)
                    embed.add_field(name="หายแล้ว: ",value=j['Recovered'],inline=False)
                    embed.add_field(name="รักษาตัวอยู่ในโรงพยาบาล: ",value=j['Hospitalized'],inline=False)
                    embed.add_field(name="เสียชีวิต: ",value=j['Deaths'],inline=False)
                    embed.set_footer(icon_url="https://ddc.moph.go.th/viralpneumonia/img/footer-logo.png",text="ขอบคุณข้อมูลจาก กรมควบคุมโรค")
                    await msg.edit(content="_ _",embed=embed)
            if lang == 'en':
                if r.ok:
                    embed = discord.Embed(
                        title = 'Situation in Thailand',
                        colour = discord.Colour.blue()
                    )
                    j=json.loads(r.text)
                    embed.add_field(name="Date",value=j['UpdateDate'],inline=False)
                    embed.add_field(name="Total infections",value=j['Confirmed'],inline=False)
                    embed.add_field(name="Confirmed cases",value=j['Recovered'],inline=False)
                    embed.add_field(name="Total hospitalized",value=j['Hospitalized'],inline=False)
                    embed.add_field(name="Total deaths",value=j['Deaths'],inline=False)
                    embed.set_footer(icon_url="https://ddc.moph.go.th/viralpneumonia/img/footer-logo.png",text="Thanks for the data from the Department of Disease Control.")
                    await msg.edit(content="_ _",embed=embed)
        except:
            await msg.edit(content="Something went wrong")
    @corona.error
    async def corona_error(self,ctx,error):
        embed = discord.Embed(
            title = "Error result",
            description = error,
            colour = discord.Colour.red()
        )
        await ctx.send(embed=embed)

    

def setup(bot):
    bot.add_cog(money(bot))