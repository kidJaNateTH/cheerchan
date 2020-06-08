import discord
from discord.ext import commands
import goslate
from googletrans import Translator
import asyncio
# -*- coding: utf-8 -*-


class TRANS(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(aliases=['trans'])
    async def translate(self,ctx,lang:str,*,text:str):
        gs = Translator()
        result = gs.translate(text,dest=lang,src='auto')
        print(result)
        embed = discord.Embed(
            title = "Translate",
            colour = discord.Colour.blue()
        )
        embed.set_thumbnail(url="https://www.aniaetleprogrammeur.com/wp-content/uploads/2019/02/Google_Translate_Icon.png")
        embed.add_field(name=f"Source: **{result.src}**",value=f"**`{text}`**",inline=False)
        embed.add_field(name=f"Destination: **{result.dest}**",value=f"**`{result.text}`**",inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Request by {ctx.author.display_name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def ctm(self,ctx,p:int):
        await ctx.send("Welcome to counting to million\nᵂᵃʳⁿᶦⁿᵍ ᵗʰᶦˢ ᶜᵒᵐᵐᵃⁿᵈ ᵐᵃʸ ʷᶦˡˡ ᵈᵉˢᵗʳᵒʸ ᵐʸ ᶜᵒᵐᵖᵘᵗᵉʳ")
        if ctx.author.id != 546558917929598978:
            return await ctx.send("Nope")
        t = 1
        ending ={}
        while t <= p:
            if t == 1:
                ending = "st"
            if t == 2:
                ending = "nd"
            if t == 3:
                ending = "rd"
            if t >= 4:
                ending = "th"
            await ctx.send(f"{t}{ending}")
            t = t + 1
            await asyncio.sleep(0.5)

            



def setup(bot):
    bot.add_cog(TRANS(bot))