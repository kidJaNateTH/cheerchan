import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext.tasks import loop
TOKEN = 'NzExNTEwMTYyMTgzMTU5ODM4.XuN-tg.KvclgEGztUyTiZEAbBnygxhgA58'
client = commands.Bot(command_prefix = 'c!')
import asyncio
import json


@client.event
async def on_ready():
    servers = str(len(client.guilds))
    await client.change_presence(activity=discord.Streaming(name=f"c!help | {servers} Servers", url="https://www.twitch.tv/kidjanateth"))
    client.remove_command('help')
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    #client.load_extension('cogs.avatar')
    client.load_extension('cogs.brainout')
    client.load_extension('cogs.clear')
    client.load_extension('cogs.customemoji')
    client.load_extension('cogs.dice')
    client.load_extension('cogs.fight')
    client.load_extension('cogs.gelbooru')
    client.load_extension('cogs.hentai')
    client.load_extension('cogs.memes')
    client.load_extension('cogs.money')
    client.load_extension('cogs.music')
    client.load_extension('cogs.newhelp')
    client.load_extension('cogs.ping')
    client.load_extension('cogs.say')
    client.load_extension('cogs.sent')
    client.load_extension('cogs.server')
    client.load_extension('cogs.translate')
    client.load_extension('cogs.ytsearch')
    client.load_extension('cogs.profile')
    client.load_extension('cogs.owner')
    client.load_extension('cogs.premium')
    oldserver = str(len(client.guilds))
    while True:
        servers = str(len(client.guilds))
        if not oldserver == servers:
            print(f"Server have changed, {servers} Servers")
            oldserver = servers
        
        
        await client.change_presence(activity=discord.Streaming(name=f"c!help | {servers} Servers", url="https://www.twitch.tv/kidjanateth"))
        await asyncio.sleep(5)


@client.event
async def on_message(message):
    lvl = {}
    exp = {}
    if message.author.bot:
        return
    with open('users.json','r',encoding="utf8") as f:
        users = json.load(f)
        try:
            exp = users[str(message.author.id)]['exp']
            lvl = users[str(message.author.id)]['lvl']
        except:
            with open('users.json', 'w',encoding="utf8") as f:
                users[str(message.author.id)] = {}
                users[str(message.author.id)]['username'] = str(message.author)
                users[str(message.author.id)]['exp'] = 0
                users[str(message.author.id)]['lvl'] = 0
                users[str(message.author.id)]['coins'] = 0
                users[str(message.author.id)]['premium'] = False
                users[str(message.author.id)]['customBG'] = False
                users[str(message.author.id)]['textR'] = 255
                users[str(message.author.id)]['textG'] = 255
                users[str(message.author.id)]['textB'] = 255
                
                json.dump(users, f, sort_keys=True, indent=4, ensure_ascii=False)
                exp = users[str(message.author.id)]['exp']
    with open('users.json', 'w',encoding="utf8") as f:
        users[str(message.author.id)]['exp'] = exp = exp + 1
        exp = users[str(message.author.id)]['exp']
        lvl_start = users[str(message.author.id)]['lvl']
        lvl_end = exp ** (1.5/4)
        if lvl_start < lvl_end:
            users[str(message.author.id)]['lvl'] = users[str(message.author.id)]['lvl'] + 1

            if users[str(message.author.id)]['lvl'] == 1:
                users[str(message.author.id)]['lvl'] = 1
            else:
                print("ok")
                #await message.channel.send(f"OwO {message.author.mention} You just advanced to level {users[str(message.author.id)]['lvl']}!")


        json.dump(users, f, sort_keys=True, indent=4, ensure_ascii=False)


    #SENT DM MESSAGE#####################################
    if message.author.id == client.user.id:
        return
    if message.author != message.author.bot:
        if not message.guild:
            print(f"{message.author} DM to Cheer Chan")
            if message.content == "d!help":
                ctx = client.get_user(message.author.id)
                await ctx.send("Please type in server")
            #if message.content == 'hi' or message.content == 'Hi' or message.content == 'Hoi' or message.content == 'hoi':
            #    user = client.get_user(message.author.id)
            #    return await user.send(f"Hi {message.author.name}")
            embed = discord.Embed(
                title = message.author.mention,
                colour = discord.Colour.dark_blue()
            )
            embed.set_footer(icon_url=client.user.avatar_url,text=f"c!dm {message.author.id}")
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.add_field(name=f"User mention: ",value=message.author.mention,inline=False)
            embed.add_field(name=f"Username: ",value=message.author,inline=False)
            embed.add_field(name=f"User ID: ",value=message.author.id,inline=False)
            embed.add_field(name=f"Content: ",value=message.content,inline=False)
            await client.get_guild(719837288670167100).get_channel(719837289349644390).send(embed=embed)

    
    await client.process_commands(message)
client.run(TOKEN)