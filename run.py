import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
TOKEN = 'NzExNTEwMTYyMTgzMTU5ODM4.XuN-tg.KvclgEGztUyTiZEAbBnygxhgA58'
client = commands.Bot(command_prefix = 'c!')


@client.event
async def on_ready():
    client.remove_command('help')
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

@client.command()
async def aboutme(ctx):
    embed = discord.Embed(
        title = "Welcome, Everyone",
        colour = discord.Colour.blue()
    )
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name="⭐ Cheer Chan",value="Cheer Chan is discord bot",inline=False)
    embed.add_field(name="⭐ Character",value="● Tall: 158cm\n● Weight: 52.4kg\n● To dress: Sleepwear\n● Favorite colour: Green,Pink\n● Habit: Lazy, Like to sleep, Always late\n● Hobbies: Sleeping, Drawing",inline=False)
    embed.add_field(name="⭐ Server",value="If you found any bugs or glitchs, Please let we knows in \n<#719837289177546798>     ↤ \nOr you have any questions you can ask in \n<#719846537899016293> ↤",inline=False)
    embed.add_field(name="⭐ Invite me",value="[[Click this]](https://discord.com/api/oauth2/authorize?client_id=711510162183159838&permissions=8&scope=bot)",inline=False)
    embed.add_field(name="⭐ Website",value="https://www.cheerchan.xyz",inline=False)
    embed.add_field(name="⭐ Server invite link",value="https://discord.gg/MVwkZt7",inline=False)
    await ctx.send(embed=embed)
client.run(TOKEN)