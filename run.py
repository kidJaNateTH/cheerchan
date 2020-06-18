import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext.tasks import loop
import json

with open('token.json','r') as f:
    to = json.load(f)
    token = to['token']

TOKEN = token

def get_prefix(client,message):
    with open('servers.json','r',encoding='utf8') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]['prefix']

client = commands.Bot(command_prefix = get_prefix)

import asyncio
import json

@client.command()
async def prefix(ctx,new):
    if not ctx.message.author.guild_permissions.administrator:
        return await ctx.send("You're not have permissions to do that")
    try:
        with open('servers.json','r',encoding='utf8') as f:
            prefixes = json.load(f)
        with open('servers.json','w',encoding='utf8') as f:
            prefixes[str(ctx.guild.id)]['prefix'] = str(new)
            json.dump(prefixes, f, sort_keys=True, indent=4, ensure_ascii=False)

            await ctx.send(f"Prefix changed to {new}")
    except:
        with open('servers.json','r',encoding='utf8') as f:
            prefixes = json.load(f)
        with open('servers.json','w',encoding='utf8') as f:
            prefixes[str(ctx.guild.id)] = {}
            prefixes[str(ctx.guild.id)]['Server_name'] = str(ctx.guild.name)
            prefixes[str(ctx.guild.id)]['ticket'] = False
            prefixes[str(ctx.guild.id)]['snipe'] = False
            prefixes[str(ctx.guild.id)]['snipe_text'] = False
            prefixes[str(ctx.guild.id)]['sniper_url'] = False
            prefixes[str(ctx.guild.id)]['sniper_name'] = False
            prefixes[str(ctx.guild.id)]['prefix'] = str(new)
            json.dump(prefixes, f, sort_keys=True, indent=4, ensure_ascii=False)

            await ctx.send(f"Prefix changed to {new}")

@client.event
async def on_ready():
    
    servers = str(len(client.guilds))


    #fixing bugs
    #await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"Adding Features | {servers} Servers"))

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
    client.load_extension('cogs.ticket')
    client.load_extension('cogs.on_message')
    client.load_extension('cogs.snipe')
    client.load_extension('cogs.teach')
    client.load_extension('cogs.log')
    client.load_extension('cogs.welcome')
    client.load_extension('cogs.mute')

    
    oldserver = str(len(client.guilds))
    while True:
        servers = str(len(client.guilds))
        if not oldserver == servers:
            print(f"Server have changed, {servers} Servers")
            oldserver = servers
        

        #Fixing bugs
        #await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"Adding Features | {servers} Servers"))
        
        
        await client.change_presence(activity=discord.Streaming(name=f"c!help | {servers} Servers", url="https://www.twitch.tv/kidjanateth"))
        await asyncio.sleep(5)
@client.event
async def on_guild_join(guild):
    print(f"Cheer Chan have joined to {guild}")
    with open("servers.json","r",encoding="utf8") as f:
        server = json.load(f)
    with open("servers.json","w",encoding="utf8") as f:
        server[str(guild.id)] = {}
        server[str(guild.id)]['Server_name'] = str(guild.name)
        server[str(guild.id)]['ticket'] = False
        server[str(guild.id)]['snipe'] = False
        server[str(guild.id)]['snipe_text'] = False
        server[str(guild.id)]['sniper_url'] = False
        server[str(guild.id)]['sniper_name'] = False
        server[str(guild.id)]['prefix'] = "c!"
        json.dump(server, f, sort_keys=True, indent=4, ensure_ascii=False)
    

@client.event
async def on_guild_remove(guild):
    with open('servers.json','r',encoding='utf8') as f:
        pre = json.load(f)
    pre.pop(str(guild.id))
    with open('servers.json','w',encoding='utf8') as f:
        json.dump(pre,f,sort_keys=True, indent=4, ensure_ascii=False)

@client.event
async def on_message(message):
    if message.content == "<@!711510162183159838>":
        
        with open('servers.json','r',encoding='utf8') as f:
            pre = json.load(f)
            pref = pre[str(message.guild.id)]['prefix']
            emoji=discord.utils.get(client.emojis,name="yellow_sparksidk")
            embed=discord.Embed(
                description = f"{emoji} Prefix in this server `{pref}`\n{emoji} Help command `{pref}help`",
                colour = discord.Colour.green()
            )
            await message.channel.send(embed=embed)
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