import discord
from discord.ext import commands
from discord.utils import get
import random
import asyncio

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
from PIL import ImageFilter

#gif
import imageio as imo
from glob import glob

import os

class memes(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['HAX','hax','Hacc','hacc','haX'])
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
                embed.clear_fields()
                embed.add_field(name=f":red_circle: Metasploit error",value=f"_ _",inline=True)
                await msg.edit(embed=embed)
            if erro == 2:
                embed.clear_fields()
                embed.add_field(name=f":red_circle: Missing sudo error",value=f"_ _",inline=True)
                await msg.edit(embed=embed)
            if erro == 3:
                embed.clear_fields()
                embed.add_field(name=f":red_circle: Missing pip error",value=f"_ _",inline=True)
                await msg.edit(embed=embed)
            await asyncio.sleep(2)
            embed.clear_fields()
            embed.add_field(name=f":orange_circle: Fixing that problems",value=f"_ _",inline=True)
            await msg.edit(embed=embed)
            await asyncio.sleep(5)

            er = random.randint(1,7)
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
            if er == 6:
                email = "@jalernพร.com"
            if er == 7:
                email = "@watpahuapong.com"
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

            re = random.randint(1,7)
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
            if re == 6:
                password = "nou123456"
            if re == 7:
                password = "imcoolyouknow"
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
            embed.add_field(name=f"Email: `{member.name}{email}`\nPassword: `{password}`",value=f"_ _",inline=True)
            embed.set_thumbnail(url=member.avatar_url)
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
        os.remove(f'dltvmeme{ctx.author.id}.png')
        os.remove('ctxformeme.png')

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
        os.remove(f'bedmeme{ctx.author.id}.png')
        os.remove('ctxformeme.png')

    @commands.command(aliases=['noyes'])
    async def yesno(self,ctx,member:discord.Member=None,member2:discord.Member=None):
        if member2 != None:
            ctx_name = member2.name
            member2_name = member.name

            

            img = Image.open("./MEME/yes_no.png")
            font = ImageFont.truetype("Modern_Sans_Light.otf", 70)
            draw = ImageDraw.Draw(img)

            w, h = draw.textsize(member2_name)
            w2, h2 = draw.textsize(ctx_name)

            W, H = (1140,1200)

            W2, H2 = (1140,300)


            draw.text(((W-w)/2,(H-h)/2), f"{ctx_name}", (0, 0, 0), font=font)
            draw.text(((W2-w2)/2,(H2-h2)/2), f"{member2_name}", (0, 0, 0), font=font)
            img.save(f'yes_nomeme{ctx.author.id}.png')
            await ctx.send(file=discord.File(f"yes_nomeme{ctx.author.id}.png"))
            os.remove(f"yes_nomeme{ctx.author.id}.png")
            return
        
        
        
        
        
        ##MEMBER AVATAR
        if not member == None:
            member_name = member.display_name
        else:
            member_name = "Cheer Chan"
        ctx_name = ctx.author.name
        img = Image.open("./MEME/yes_no.png")
        font = ImageFont.truetype("Modern_Sans_Light.otf", 70)
        draw = ImageDraw.Draw(img)



        w, h = draw.textsize(member_name)

        W, H = (1130,1200)

        W2, H2 = (1250,300)



        draw.text(((W-w)/2,(H-h)/2), f"{member_name}", (0, 0, 0), font=font)
        draw.text(((W2-w)/2,(H2-h)/2), f"{ctx_name}", (0, 0, 0), font=font)
        img.save(f'yes_nomeme{ctx.author.id}.png')
        await ctx.send(file=discord.File(f"yes_nomeme{ctx.author.id}.png"))
        os.remove(f"yes_nomeme{ctx.author.id}.png")
        
    @commands.command()
    async def salt(self,ctx,member:discord.Member=None):
        member = ctx.author if not member else member
        print("1")
        image_url = member.avatar_url
        img_data = requests.get(image_url).content
        with open('ctxformeme.png', 'wb') as handler:
            handler.write(img_data)
        img = Image.open("ctxformeme.png")
        s = Image.open("./resources/salt.png")
        new_size = (700,700)
        avatar = (1000,1000)
        s = s.resize(new_size)
        img = img.resize(avatar)
        s = s.rotate(-135)
        img.paste(s,(-180,-180),s)
        img.save(f'saltmeme{member.id}01.png')
        #await ctx.send(file=discord.File(f'saltmeme{ctx.author.id}01.png'))


        print("2")
        img = Image.open("ctxformeme.png")
        s = Image.open("./resources/salt.png")
        new_size = (700,700)
        avatar = (1000,1000)
        s = s.resize(new_size)
        img = img.resize(avatar)
        s = s.rotate(-135)
        img.paste(s,(-100,-140),s)
        img.save(f'saltmeme{member.id}02.png')
        #await ctx.send(file=discord.File(f'saltmeme{ctx.author.id}.png'))


        print("3")
        img = Image.open("ctxformeme.png")
        s = Image.open("./resources/salt.png")
        new_size = (700,700)
        avatar = (1000,1000)
        s = s.resize(new_size)
        img = img.resize(avatar)
        s = s.rotate(-135)
        img.paste(s,(-230,-160),s)
        img.save(f'saltmeme{member.id}03.png')
        #await ctx.send(file=discord.File(f'saltmeme{ctx.author.id}.png'))

        print("converting")
        chuefilerupphap = glob(f'saltmeme{member.id}*.png')
        ruamrupphap = [imo.imread(r) for r in chuefilerupphap]
        imo.mimwrite(f'saltmeme{member.id}.gif',ruamrupphap,fps=30)
        await ctx.send(file=discord.File(f'saltmeme{member.id}.gif'))

        os.remove(f'saltmeme{member.id}.gif')
        os.remove('ctxformeme.png')
        os.remove(f'saltmeme{member.id}03.png')
        os.remove(f'saltmeme{member.id}02.png')
        os.remove(f'saltmeme{member.id}01.png')

    @commands.command()
    async def wanted(self,ctx,member:discord.Member=None):
        member = ctx.author if not member else member
        image_url = member.avatar_url
        img_data = requests.get(image_url).content
        with open(f'ctxformeme{member.id}.png', 'wb') as handler:
            handler.write(img_data)
        img = Image.open(f"ctxformeme{member.id}.png")
        s = Image.open("./MEME/wanted.png")
        new_size = (240,240)
        img = img.resize(new_size)
        s.paste(img,(90,130))

        font = ImageFont.truetype("./font/Nashville-z8w0.ttf", 110)
        draw = ImageDraw.Draw(s)
        member_name = member.name
        w, h = draw.textsize(member_name)

        W, H = (130,850)

        draw.text(((W-w)/2,(H-h)/2), f"{member_name}", (0, 0, 0), font=font)

        s.save(f'wanted{member.id}.png')
        await ctx.send(file=discord.File(f'wanted{member.id}.png'))
        os.remove(f'wanted{member.id}.png')
def setup(bot):
    bot.add_cog(memes(bot))