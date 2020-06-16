import discord
from discord.ext import commands
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import json

class PROFILE(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(aliases=['pf'])
    async def profile(self,ctx,member:discord.Member=None):
        member = ctx.author if not member else member
        if member.bot:
            return
        
        with open('users.json','r',encoding="utf8") as f:
            users = json.load(f)
            if users[str(member.id)]['premium'] == True:
                if not users[str(member.id)]['customBG'] == False:
                    msg = await ctx.send("Managing something")
                    image_url = member.avatar_url
                    img_data = requests.get(image_url).content

                    BG_url = users[str(member.id)]['customBG']
                    BG_data = requests.get(BG_url).content
                    with open(f'BG{member.id}.png', 'wb') as handler:
                        handler.write(BG_data)

                    with open(f'ctxformeme{member.id}.png', 'wb') as handler:
                        handler.write(img_data)
                    img = Image.open("./infoBG/bg1.png")
                    BG = Image.open(f'BG{member.id}.png')
                    bgsize = (2000,687)
                    BG = BG.resize(bgsize)
                    img.paste(BG,(0,0))
                    new_size = (512,512)
                    logo = Image.open(f"ctxformeme{member.id}.png")
                    logo = logo.resize(new_size)
                    img.paste(logo,(90,80))
                    draw = ImageDraw.Draw(img)

                    font = ImageFont.truetype("Modern_Sans_Light.otf", 160)



                    member_name = member.name
                    name_size = len(member_name)
                    print(name_size)
                    name = ImageFont.truetype("./font/TH-Chara ver 2.00.ttf", 220 // name_size * 6)
                    level = ImageFont.truetype("Fitamint Script.ttf", 300)

                    if str(member.status) == "online":
                        online = Image.open("./resources/online.png")
                        online = online.resize((128,128))
                        img.paste(online,(500,500))

                    if str(member.status) == "idle":
                        online = Image.open("./resources/idle.png")
                        online = online.resize((128,128))
                        img.paste(online,(500,500))

                    if str(member.status) == "dnd":
                        online = Image.open("./resources/dnd.png")
                        online = online.resize((128,128))
                        img.paste(online,(500,500))

                    if str(member.status) == "offline":
                        online = Image.open("./resources/offline.png")
                        online = online.resize((128,128))
                        img.paste(online,(500,500))

                    draw.text((620, 20 + name_size * 5), f"{member.name}", (users[str(member.id)]['textR'], users[str(member.id)]['textG'], users[str(member.id)]['textB']), font=name)

                    with open('users.json','r',encoding="utf8") as f:
                        users = json.load(f)
                        draw.text((830 , 260), f"{users[str(member.id)]['coins']}", (users[str(member.id)]['textR'], users[str(member.id)]['textG'], users[str(member.id)]['textB']), font=font)
                        draw.text((830 , 440), f"{users[str(member.id)]['exp']} exp", (users[str(member.id)]['textR'], users[str(member.id)]['textG'], users[str(member.id)]['textB']), font=font)
                        draw.text((1600 , 320), f"{users[str(member.id)]['lvl']}", (users[str(member.id)]['textR'], users[str(member.id)]['textG'], users[str(member.id)]['textB']), font=level)
                        if users[str(member.id)]['premium'] == True:
                            crown = Image.open('./resources/crown.png')
                            crown = crown.rotate(20)
                            crown = crown.resize((200,150))
                            img.paste(crown,(-20,-20),crown)
                            print(f"{member} have premium")
                    img.save(f'profile{member.id}.png')
                    await ctx.send(file=discord.File(f'profile{member.id}.png'))
                    await msg.delete()
                    os.remove(f'profile{member.id}.png')
                    os.remove(f'ctxformeme{member.id}.png')
                    os.remove(f'BG{member.id}.png')
                    return




        msg = await ctx.send("Managing something")
        image_url = member.avatar_url
        img_data = requests.get(image_url).content
        with open(f'ctxformeme{member.id}.png', 'wb') as handler:
            handler.write(img_data)
        img = Image.open("./infoBG/bg1.png")
        new_size = (512,512)
        logo = Image.open(f"ctxformeme{member.id}.png")
        logo = logo.resize(new_size)
        img.paste(logo,(90,80))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype("Modern_Sans_Light.otf", 160)

        member_name = member.name
        name_size = len(member_name)
        print(name_size)
        name = ImageFont.truetype("./font/TH-Chara ver 2.00.ttf", 220 // name_size * 6)
        level = ImageFont.truetype("Fitamint Script.ttf", 300)

        if str(member.status) == "online":
            online = Image.open("./resources/online.png")
            online = online.resize((128,128))
            img.paste(online,(500,500))

        if str(member.status) == "idle":
            online = Image.open("./resources/idle.png")
            online = online.resize((128,128))
            img.paste(online,(500,500))

        if str(member.status) == "dnd":
            online = Image.open("./resources/dnd.png")
            online = online.resize((128,128))
            img.paste(online,(500,500))

        if str(member.status) == "offline":
            online = Image.open("./resources/offline.png")
            online = online.resize((128,128))
            img.paste(online,(500,500))

        

        with open('users.json','r',encoding="utf8") as f:
            users = json.load(f)
            draw.text((830 , 260), f"{users[str(member.id)]['coins']}", (255, 255, 255), font=font)
            draw.text((830 , 440), f"{users[str(member.id)]['exp']} exp", (255, 255, 255), font=font)
            draw.text((1600 , 320), f"{users[str(member.id)]['lvl']}", (255, 255, 255), font=level)
            if users[str(member.id)]['premium'] == True:
                crown = Image.open('./resources/crown.png')
                crown = crown.rotate(20)
                crown = crown.resize((200,150))
                img.paste(crown,(-20,-20),crown)
                draw.text((620, 20 + name_size * 5), f"{member.name}", (users[str(member.id)]['textR'], users[str(member.id)]['textG'], users[str(member.id)]['textB']), font=name)
                print(f"{member} have premium")
            else:
                draw.text((620, 20 + name_size * 5), f"{member.name}", (255, 255, 255), font=name)
        img.save(f'profile{member.id}.png')
        await ctx.send(file=discord.File(f'profile{member.id}.png'))
        await msg.delete()
        os.remove(f'profile{member.id}.png')
        os.remove(f'ctxformeme{member.id}.png')

    @commands.command(aliases=['custompf','cuspf','customPF'])
    async def customprofile(self,ctx,t:str,url=None,g=None,b=None):
        
        if t == "bg" or t == "BG" or t == "background":
            if url == None:
                embed = discord.Embed(
                    title = "Missing background URL",
                    colour = discord.Colour.red(),
                    description = "Example : c!cuspf bg https://cdn.discordapp.com/attachments/711570460487450687/722309933231767589/bg2.png"

                )
                embed.set_image(url="https://cdn.discordapp.com/attachments/711570460487450687/722309933231767589/bg2.png")
                return await ctx.send(embed=embed)
            if url == "none" or url == "false":
                embed = discord.Embed(
                    title = "Successfully cleared custom BG",
                    colour = discord.Colour.green()
                )

                try:
                    with open('users.json','r',encoding="utf8") as f:
                        users = json.load(f)
                    with open('users.json','w',encoding="utf8") as f:
                        users[str(ctx.author.id)]['customBG'] = False
                        json.dump(users, f, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send(embed=embed)
                except:
                    await ctx.send("Something went wrong, Please try again")

                return
            with open('users.json','r',encoding="utf8") as f:
                users = json.load(f)
                if users[str(ctx.author.id)]['premium'] == False:
                    return await ctx.send("You're not have Cheer Chan premium yet")
                else:
                    try:
                        with open('users.json','w',encoding="utf8") as f:
                            embed = discord.Embed(
                                title = "Custom profile",
                                colour = discord.Colour.gold()
                            )
                            embed.add_field(name="The recommend size is `2000 * 687`",value=f"Image URL {url}\nPreview",inline=True)
                            embed.set_image(url=url)
                            users[str(ctx.author.id)]['customBG'] = url
                            await ctx.send(embed=embed)
                            
                            json.dump(users,f,sort_keys=True, indent=4, ensure_ascii=False)
                    except:
                        await ctx.send("Something went wrong pls try again")
        if t == "text":
            if url == None or g == None or b == None:
                embed = discord.Embed(
                    title = "Missing RGB Colors",
                    colour = discord.Colour.red(),
                    description = "Example : c!cuspf text 255 255 255"

                )
                return await ctx.send(embed=embed)
            try:
                if ',' in str(url) or ',' in str(g) or ',' in str(b):
                    return await ctx.send("Something error, please check your RGB colours, must not have `,`")
                with open('users.json','r',encoding="utf8") as f:
                    users = json.load(f)
                with open('users.json','w',encoding="utf8") as f:
                    
                    users[str(ctx.author.id)]['textR'] = int(url)
                    users[str(ctx.author.id)]['textG'] = int(g)
                    users[str(ctx.author.id)]['textB'] = int(b)
                    embed = discord.Embed(
                        title = f"Set text color to {url},{g},{b}",
                        description = "↤ Your colors",
                        colour = discord.Colour.from_rgb(int(url),int(g),int(b))
                    )
                    json.dump(users, f, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send(embed=embed)
                    
            except:
                await ctx.send("Something error, please check your RGB colours, must not have `,`")
        if not t == "bg" or t == "BG" or t == "background" or t == "text":
            if t == "text":
                return
            embed = discord.Embed(
                title = f"{t} Not found",
                description = "🎀 BG `Change backgound image`\n✨ text `Change text color (RGB)`",
                colour = discord.Colour.red()
            )
            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(PROFILE(bot))