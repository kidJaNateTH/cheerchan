import discord
from discord.ext import commands,tasks
from discord.utils import get
from discord.ext.commands import Bot
from discord import opus
from discord import User
from discord.ext.tasks import loop
from discord.ext.commands import Bot, guild_only
from itertools import cycle

import os
import json
import asyncio
import requests

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from discord import Embed
TOKEN = 'NzExNTEwMTYyMTgzMTU5ODM4.XsErog.yVawoQK3VswcrS4OG_5lMlmgOp4'
client = commands.Bot(command_prefix = 'c!')


@client.event
async def on_ready():
    client.remove_command('help')
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    servers = str(len(client.guilds))
    #await client.change_presence(status=discord.Status.online, activity=discord.Game(f"c!help | {servers} Servers"))
    
    await client.change_presence(activity=discord.Streaming(name=f"c!help | {servers} Servers",url="https://www.twitch.tv/kidjanateth"))

    client.load_extension('cogs.ping')
    client.load_extension('cogs.dice')
    client.load_extension('cogs.brainout')
    client.load_extension('cogs.say')
    client.load_extension('cogs.fight')
    client.load_extension('cogs.ytsearch')
    client.load_extension('cogs.avatar')
    client.load_extension('cogs.clear')
    client.load_extension('cogs.hentai')
    client.load_extension('cogs.memepic')
    client.load_extension('cogs.sent')
    client.load_extension('cogs.customemoji')
    client.load_extension('cogs.money')
    client.load_extension('cogs.newhelp')
    client.load_extension('cogs.memes')
    client.load_extension('cogs.music')
    client.load_extension('cogs.translate')
    client.load_extension('cogs.server')
    
    client.load_extension('cogs.gelbooru')
    client.loop.create_task(change_status())

async def change_status():
    while True:
        
        servers = str(len(client.guilds))
        print(f"Update server count, {servers} Servers")
        #await client.change_presence(status=discord.Status.online, activity=discord.Game(f"c!help | {servers} Servers"))
        await client.change_presence(activity=discord.Streaming(name=f"c!help | {servers} Servers",url="https://www.twitch.tv/kidjanateth"))
        await asyncio.sleep(10)




@client.event
async def on_message_delete(message):
    p = False
    if p == True:
        #await message.channel.send(message.guild.id)
        if message.author.bot or message.author.id == 546558917929598978:
            print(f"Returned {message.author} message")
            return
        embed = discord.Embed(
            title = f":smirk: {message.author}",
            colour = discord.Colour.dark_blue()
        )
        embed.add_field(name=f"**{message.content}**",value="_ _",inline=True)
        embed.set_footer(text=f"Bad {message.author.name} has deleted their sins")
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    

@client.command()
async def level(ctx,member:discord.Member=None):
    member = ctx.author if not member else member
    member_id = str(member.id)

    if not member_id in users:
        await ctx.send("Member doesn't a level")
    else:
        embed = discord.Embed(
            color = member.color,
            timestamp = ctx.message.created_at
        )
        embed.set_author(name=f"Level - {member}",icon_url=client.user.avatar_url)
        embed.add_field(name="Level",value=users[member_id]['level'])
        embed.add_field(name="XP",value=users[member_id]['exp'])
        await ctx.send(embed=embed)

with open ("users.json",encoding='utf8') as f:
        users = json.load(f)
    
async def save_users():
    await client.wait_until_ready()
    while not client.is_closed():
        with open("users.json","w") as f:
            json.dump(users,f,indent=4)

        await asyncio.sleep(5)

@client.command(aliases=['rank','pf'])
async def profile(ctx,member:discord.Member=None):
    member = ctx.author if not member else member
    if member.bot:
        return await ctx.send("It's just bot...")

    image_url = member.avatar_url
    member_id = str(member.id)
    img_data = requests.get(image_url).content
    with open('useravatar.png', 'wb') as handler:
        handler.write(img_data)
    if member.id == 546558917929598978:
        o = random.randint(1,5)
        print(o)
        if o == 1:
            img = Image.open("./infoBG/EXC/exc1.png")
        if o == 2:
            img = Image.open("./infoBG/EXC/exc2.png")
        if o == 3:
            img = Image.open("./infoBG/EXC/exc3.png")
        if o == 4:
            img = Image.open("./infoBG/EXC/exc4.png")
        if o == 5:
            img = Image.open("./infoBG/EXC/exc5.png")
        user_avatar = Image.open("useravatar.png")
        new_size = (500,500)
        user_avatar = user_avatar.resize(new_size)
        img.paste(user_avatar,(100,90))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fitamint Script.ttf", 200)
        if member.name == "NateTH":
            textname = ImageFont.truetype("./infoBG/America.ttf", 300)

        u = users[member_id]['level']

        draw.text((1640, 350), f"{u}", (255, 255, 255), font=font)
        draw.text((670, 200), member.name, (128, 255, 253), font=textname)
        img.save('userprofile.png')
        await ctx.send(file=discord.File("userprofile.png"))
        return
    i = users[member_id]['level']
    if i >= 1 and i <= 4:
        img = Image.open("./infoBG/bg1.png")
        user_avatar = Image.open("useravatar.png")
        new_size = (500,500)
        user_avatar = user_avatar.resize(new_size)
        img.paste(user_avatar,(100,90))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fitamint Script.ttf", 200)
        if member.id == 507827170261991464:
            textname = ImageFont.truetype("./infoBG/NateTH.ttf", 300)
        else:
            textname = ImageFont.truetype("Modern_Sans_Light.otf", 100)
        draw.text((1640, 350), f"{i}", (255, 255, 255), font=font)
        draw.text((750, 275), member.name, (255, 255, 255), font=textname)
        img.save('userprofile.png')
        return await ctx.send(file=discord.File("userprofile.png"))
    if i >= 5 and i <= 6:
        img = Image.open("./infoBG/bg2.png")
        user_avatar = Image.open("useravatar.png")
        new_size = (500,500)
        user_avatar = user_avatar.resize(new_size)
        img.paste(user_avatar,(100,90))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fitamint Script.ttf", 200)
        if member.id == 507827170261991464:
            textname = ImageFont.truetype("./infoBG/NateTH.ttf", 300)
        else:
            textname = ImageFont.truetype("Modern_Sans_Light.otf", 100)
        draw.text((1640, 350), f"{i}", (255, 255, 255), font=font)
        draw.text((750, 275), member.name, (255, 255, 255), font=textname)
        img.save('userprofile.png')
        return await ctx.send(file=discord.File("userprofile.png"))
    if i >= 7 and i <= 8:
        img = Image.open("./infoBG/bg3.png")
        user_avatar = Image.open("useravatar.png")
        new_size = (500,500)
        user_avatar = user_avatar.resize(new_size)
        img.paste(user_avatar,(100,90))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fitamint Script.ttf", 200)
        if member.id == 507827170261991464:
            textname = ImageFont.truetype("./infoBG/NateTH.ttf", 300)
        else:
            textname = ImageFont.truetype("Modern_Sans_Light.otf", 100)
        draw.text((1640, 350), f"{i}", (255, 255, 255), font=font)
        draw.text((750, 275), member.name, (255, 255, 255), font=textname)
        img.save('userprofile.png')
        return await ctx.send(file=discord.File("userprofile.png"))
    if i >= 9 and i <= 10:
        img = Image.open("./infoBG/bg4.png")
        user_avatar = Image.open("useravatar.png")
        new_size = (500,500)
        user_avatar = user_avatar.resize(new_size)
        img.paste(user_avatar,(100,90))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fitamint Script.ttf", 200)
        if member.id == 507827170261991464:
            textname = ImageFont.truetype("./infoBG/NateTH.ttf", 300)
        else:
            textname = ImageFont.truetype("Modern_Sans_Light.otf", 100)
        draw.text((1640, 350), f"{i}", (255, 255, 255), font=font)
        draw.text((750, 275), member.name, (255, 255, 255), font=textname)
        img.save('userprofile.png')
        return await ctx.send(file=discord.File("userprofile.png"))
    if i >= 11 and i <= 14:
        img = Image.open("./infoBG/bg5.png")
        user_avatar = Image.open("useravatar.png")
        new_size = (500,500)
        user_avatar = user_avatar.resize(new_size)
        img.paste(user_avatar,(100,90))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fitamint Script.ttf", 200)
        if member.id == 507827170261991464:
            textname = ImageFont.truetype("./infoBG/NateTH.ttf", 300)
        else:
            textname = ImageFont.truetype("Modern_Sans_Light.otf", 100)
        draw.text((1640, 350), f"{i}", (255, 255, 255), font=font)
        draw.text((750, 275), member.name, (255, 255, 255), font=textname)
        img.save('userprofile.png')
        return await ctx.send(file=discord.File("userprofile.png"))
    if i >= 15:
        img = Image.open("./infoBG/bg6.png")
        user_avatar = Image.open("useravatar.png")
        new_size = (500,500)
        user_avatar = user_avatar.resize(new_size)
        img.paste(user_avatar,(100,90))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fitamint Script.ttf", 200)
        if member.id == 507827170261991464:
            textname = ImageFont.truetype("./infoBG/NateTH.ttf", 300)
        else:
            textname = ImageFont.truetype("Modern_Sans_Light.otf", 100)
        draw.text((1640, 350), f"{i}", (255, 255, 255), font=font)
        draw.text((750, 275), member.name, (255, 255, 255), font=textname)
        img.save('userprofile.png')
        return await ctx.send(file=discord.File("userprofile.png"))
@profile.error
async def pf_error(ctx,error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f"ERROR... See the console\n`{error}`")
def lvl_up(author_id):
    cur_xp = users[author_id]['exp']
    cur_lvl = users[author_id]['level']
    if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
        users[author_id]['level'] += 1
        return True
    else:
        return False

@client.event
async def on_member_join(member):
    mid = member.id
    server_name = member.guild.name
    ctx = client.get_user(mid)
    await ctx.send(f"Hi! **{member.name}**, Welcome to **{server_name}**!\nDon't forget to join Cheer Chan Support server\nhttps://discord.gg/yMHdQkE")

@client.event
async def on_message(message):

    #SENT DM MESSAGE#####################################
    if message.author.id == client.user.id:
        return
    if message.author != message.author.bot:
        if not message.guild:
            print(f"{message.author} DM to cheer chan")
            if message.content == "c!help":
                ctx = client.get_user(message.author.id)
                await ctx.send("Please type in server")
            #if message.content == 'hi' or message.content == 'Hi' or message.content == 'Hoi' or message.content == 'hoi':
            #    user = client.get_user(message.author.id)
            #    return await user.send(f"Hi {message.author.name}")
            embed = discord.Embed(
                title = message.author.mention,
                colour = discord.Colour.green()
            )
            embed.set_footer(icon_url=client.user.avatar_url,text=f"c!dm <@!{message.author.id}>")
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.add_field(name=f"User mention: ",value=message.author.mention,inline=False)
            embed.add_field(name=f"Username: ",value=message.author,inline=False)
            embed.add_field(name=f"User ID: ",value=message.author.id,inline=False)
            embed.add_field(name=f"Content: ",value=message.content,inline=False)
            #CTTS
            await client.get_guild(719837288670167100).get_channel(719837289349644390).send(embed=embed)
            #OSUFG
            #return await client.get_guild(690410179157557298).get_channel(715552977443749958).send(embed=embed)






    #give XP
    if message.author == client.user:
        return
    author_id = str(message.author.id)
    if message.author != message.author.bot:
        if not message.guild:
            return
        else:
            if not message.author.bot:
                if not author_id in users:
                    users[author_id] = {}
                    users[author_id]['level'] = 1
                    users[author_id]['exp'] = 0
                users[author_id]['exp'] += 1
                    
                #json.dump(f,users)
    try:
        if lvl_up(author_id):
            ctx = client.get_channel(message.channel.id)
            dm = client.get_user(message.author.id)
            #await dm.send(f"{message.author.mention} is now level {users[author_id]['level']}")
            if users[author_id]['level'] == 5:
                await ctx.send(f"{message.author.mention}, You're unlocked tier 1 profile background!, type `c!profile`")
            if users[author_id]['level'] == 7:
                await ctx.send(f"{message.author.mention}, You're unlocked tier 2 profile background!, type `c!profile`")
            if users[author_id]['level'] == 9:
                await ctx.send(f"{message.author.mention}, You're unlocked tier 3 profile background!, type `c!profile`")
            if users[author_id]['level'] == 11:
                await ctx.send(f"{message.author.mention}, You're unlocked tier 4 profile background!, type `c!profile`")
            if users[author_id]['level'] == 15:
                await ctx.send(f"{message.author.mention}, You're unlocked tier 5 profile background!, type `c!profile`")
    except:
        print("can't send level up")
    ###############################

    #snipe
    file = open("snipe.cheerchan","a",encoding='utf-8')
    msg = message.author.name+": "+message.content+"\n"
    file.write(msg)
        
    if message.content == 'c!snipe':
        if message.author.id == 546558917929598978 or message.author.id == 507827170261991464 or message.author.id == 508473794994896896:
            user = client.get_user(message.author.id)
            channel = client.get_channel(message.channel.id)
            try:
                size = os.stat("snipe.cheerchan")
                if size.st_size >= 8000000:
                    await channel.send(f"Detail: `snipe.cheerchan`\nSize: `{size.st_size} Bytes`")
                    os.remove("snipe.cheerchan")
                    return await channel.send("OOF i think snipe file is over 8Mbs, I will delete it now")
            except:
                return await channel.send("Not found snipe file...")
            await channel.send("I has send `snipe.cheerchan` to your DM\nCheck it out")
            await channel.send(f"Detail: `snipe.cheerchan`\nSize: `{size.st_size} Bytes`")
            await user.send(file=discord.File("snipe.cheerchan"))
        else:
            channel = client.get_channel(message.channel.id)
            await channel.send("nub, You're not my Owner")
            user = client.get_user(546558917929598978)
            await user.send(f"{message.author} trying to use snipe command")
    ###############################
            




    
    await client.process_commands(message)

client.run(TOKEN)