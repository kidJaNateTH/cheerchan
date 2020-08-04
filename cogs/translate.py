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

    @translate.error
    async def trans_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed1 = discord.Embed(
                title = "ERROR",
                color = discord.Colour.red()
            )
            embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/711570460487450687/720820208545169438/cheerchan_sad.png")
            embed1.add_field(name="Missing Required Argument\nc!translate <Destination lang> <text>",value="_ _",inline=True)
            msg = await ctx.send(embed=embed1)
            await msg.add_reaction("😳")

            #await ctx.send("Missing Required Argument\nc!translate `<Destination lang>` `<text>`")
            embed = discord.Embed(
                title = "All languages support",
                colour = discord.Colour.blue()
            )
            from googletrans import LANGUAGES
            embed.set_thumbnail(url="https://www.aniaetleprogrammeur.com/wp-content/uploads/2019/02/Google_Translate_Icon.png")
            for lang in LANGUAGES:
                embed.add_field(name=f"{lang} - {LANGUAGES[lang]}",value="_ _",inline=True)
            embed.set_author(name="See more",url="https://meta.wikimedia.org/wiki/Template:List_of_language_names_ordered_by_code",icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Wikimedia_Community_Logo_optimized.svg/20px-Wikimedia_Community_Logo_optimized.svg.png")
            await ctx.send(embed=embed)

    """DO NOT USE THIS COMMAND I JUST TOLD YOU
    @commands.command()
    async def ctm(self,ctx,p:int):
        if ctx.author.id != 546558917929598978:
            return await ctx.send("Nope")
        await ctx.send(f"Welcome to counting to million on **{ctx.channel.name}** channel\nᵂᵃʳⁿᶦⁿᵍ ᵗʰᶦˢ ᶜᵒᵐᵐᵃⁿᵈ ᵐᵃʸ ʷᶦˡˡ ᵈᵉˢᵗʳᵒʸ ᵐʸ ᶜᵒᵐᵖᵘᵗᵉʳ")
        
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
            """

            



def setup(bot):
    bot.add_cog(TRANS(bot))
