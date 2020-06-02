import discord
from discord.ext import commands
from discord.utils import get
import random
import reddit
import praw
import asyncio
import random

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
from PIL import ImageFilter

class memes(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['HAX','hax','Hacc','hacc'])
    async def hack(self,ctx,member:discord.Member):
        embed = discord.Embed(
            title = f":green_circle: Hacking {member.display_name}",
            colour = discord.Colour.green()
        )
        embed.add_field(name=f":orange_circle: Searching {member.name} profile",value=f"_ _",inline=True)
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        embed.clear_fields()
        embed.add_field(name=f":green_circle: Hacking {member.name}.",value=f"_ _",inline=True)
        await msg.edit(embed=embed)
        await asyncio.sleep(0.5)
        embed.clear_fields()
        embed.add_field(name=f":green_circle: Hacking {member.name}..",value=f"_ _",inline=True)
        await msg.edit(embed=embed)
        await asyncio.sleep(0.5)
        embed.clear_fields()
        embed.add_field(name=f":green_circle: Hacking {member.name}...",value=f"_ _",inline=True)
        await msg.edit(embed=embed)
        await asyncio.sleep(0.5)
        embed.clear_fields()
        embed.add_field(name=f":green_circle: Hacking {member.name}.",value=f"_ _",inline=True)
        await msg.edit(embed=embed)
        await asyncio.sleep(0.5)
        embed.clear_fields()
        embed.add_field(name=f":green_circle: Hacking {member.name}..",value=f"_ _",inline=True)
        await msg.edit(embed=embed)
        error = random.randint(1,2)
        if error == 1:
            err = True
        else:
            err = False
        if err == True:
            erro = random.randint(1,3)
            if erro == 1:
                await msg.edit(content="Metasploit error")
            if erro == 2:
                await msg.edit(content="Missing sudo error")
            if erro == 3:
                await msg.edit(content="Missing pip error")
            await asyncio.sleep(2)
            await msg.edit(content="Fixing that problems!")
            await asyncio.sleep(5)

            er = random.randint(1,5)
            if er == 1:
                email = "@yahoo.com"
            if er == 2:
                email = "@baidu.cn"
            if er == 3:
                email = "@fuyustudio.com"
            if er == 4:
                email = "@gmail.com"
            if er == 5:
                email = "@hotmail.com"
            await msg.edit(content="_ _")
            embed.clear_fields()
            embed.add_field(name=f":blue_circle: Found! {member.name}{email}",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(2)

            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}.",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}..",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}...",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}.",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}..",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}...",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)

            re = random.randint(1,5)
            password = str
            if re == 1:
                password = "KiccMyAsS1234"
            if re == 2:
                password = "Ohbabay7618912:0"
            if re == 3:
                password = "qwertyuiop"
            if re == 4:
                password = "1234kaito7890"
            if re == 5:
                password = "jojoisbest"
            embed = discord.Embed(
                title = f":green_circle: Hacked {member.display_name}",
                colour = discord.Colour.green()
            )
            embed.clear_fields()
            embed.add_field(name=f"Email: {member.name}{email}\nPassword: {password}",value=f"_ _",inline=True)
            await msg.edit(embed=embed)


        else:
            await asyncio.sleep(0.5)

            er = random.randint(1,5)
            if er == 1:
                email = "@yahoo.com"
            if er == 2:
                email = "@baidu.cn"
            if er == 3:
                email = "@fuyustudio.com"
            if er == 4:
                email = "@gmail.com"
            if er == 5:
                email = "@hotmail.com"

            embed.clear_fields()
            embed.add_field(name=f":blue_circle: Found! {member.name}{email}",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(2)

            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}.",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}..",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}...",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}.",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}..",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)
            embed.clear_fields()
            embed.add_field(name=f":purple_circle: Bypassing password {member.name}{email}...",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(0.5)

            re = random.randint(1,5)
            password = str
            if re == 1:
                password = "KiccMyAsS1234"
            if re == 2:
                password = "Ohbabay7618912:0"
            if re == 3:
                password = "qwertyuiop"
            if re == 4:
                password = "1234kaito7890"
            if re == 5:
                password = "jojoisbest"
            embed = discord.Embed(
                title = f":green_circle: Hacked {member.display_name}",
                colour = discord.Colour.green()
            )
            embed.clear_fields()
            embed.add_field(name=f"Email: {member.name}{email}\nPassword: {password}",value=f"_ _",inline=True)
            await msg.edit(embed=embed)

    @commands.command()
    async def dltv(self,ctx,member:discord.Member=None):
        ##CTX AVATAR
        image_url = ctx.author.avatar_url
        img_data = requests.get(image_url).content
        with open('ctxformeme.png', 'wb') as handler:
            handler.write(img_data)

        img = Image.open("./MEME/russian.png")
        new_size = (40,40)
        logo = Image.open("./MEME/DLTVlogo.png")
        if member == None:
            member_name = ctx.author.name
            ctx_avatar = Image.open("ctxformeme.png")
        else:
            member_name = member.name
            image_url = member.avatar_url
            img_data = requests.get(image_url).content
            with open('memberformeme.png', 'wb') as handler:
                handler.write(img_data)
            ctx_avatar = Image.open("memberformeme.png")

        ctx_avatar = ctx_avatar.resize(new_size)
        logo = logo.resize(new_size)

        img.paste(ctx_avatar,(180,65))
        img.paste(logo,(100,20))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Modern_Sans_Light.otf", 10)
        name = ImageFont.truetype("./font/TH-Chara ver 2.00.ttf", 20)
        draw.text((160, 32), f"{member_name}", (0, 0, 0), font=name)
        draw.text((170, 55), "PING : 999+", (0, 0, 0), font=font)
        img.save(f'dltvmeme{ctx.author.id}.png')
        await ctx.send(file=discord.File(f'dltvmeme{ctx.author.id}.png'))

    @commands.command()
    async def bed(self,ctx,member:discord.Member=None):
        ##MEMBER AVATAR
        if not member == None:
            image_url = member.avatar_url
            img_data = requests.get(image_url).content
            with open('memberformeme.png', 'wb') as handler:
                handler.write(img_data)

        ##CTX AVATAR
        image_url = ctx.author.avatar_url
        img_data = requests.get(image_url).content
        with open('ctxformeme.png', 'wb') as handler:
            handler.write(img_data)

        img = Image.open("./MEME/bed.png")
        new_size = (90,90)

        if member == None:
            member_avatar = Image.open("botavatar.png")
        else:
            member_avatar = Image.open("memberformeme.png")
            
        ctx_avatar = Image.open("ctxformeme.png")

        member_avatar = member_avatar.resize(new_size)
        ctx_avatar = ctx_avatar.resize(new_size)

        img.paste(member_avatar,(140,215))
        img.paste(ctx_avatar,(400,240))
        draw = ImageDraw.Draw(img)
        img.save(f'bedmeme{ctx.author.id}.png')
        await ctx.send(file=discord.File(f'bedmeme{ctx.author.id}.png'))

    @commands.command(aliases=['noyes'])
    async def yesno(self,ctx,member:discord.Member=None):
        ##MEMBER AVATAR
        if not member == None:
            member_name = member.display_name
        else:
            member_name = "Cheer Chan"
        ctx_name = ctx.author.name
        img = Image.open("./MEME/yes_no.png")
        font = ImageFont.truetype("Modern_Sans_Light.otf", 70)
        draw = ImageDraw.Draw(img)
        draw.text((500, 150), f"{member_name}", (0, 0, 0), font=font)
        draw.text((500, 600), f"{ctx_name}", (0, 0, 0), font=font)
        img.save('yes_nomeme.png')
        await ctx.send(file=discord.File("yes_nomeme.png"))
        


def setup(bot):
    bot.add_cog(memes(bot))