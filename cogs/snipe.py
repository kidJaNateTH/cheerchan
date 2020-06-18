import discord
from discord.ext import commands
import json


class SNIPE(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_message_delete(self,message):
        if message.author.bot or str(message.content).startswith("c!"):
            return
        try:
            with open('servers.json','r',encoding='utf8') as f:
                server = json.load(f)
                if server[str(message.guild.id)]['snipe'] == True:
                    with open('servers.json','w',encoding='utf8') as f:
                        server[str(message.guild.id)]['snipe_text'] = str(message.content)
                        server[str(message.guild.id)]['sniper_url'] = str(message.author.avatar_url)
                        server[str(message.guild.id)]['sniper_name'] = str(message.author)
                        json.dump(server,f, sort_keys=True, indent=4, ensure_ascii=False)
                else:
                    return
        except:
            with open('servers.json','r',encoding='utf8') as f:
                server = json.load(f)
            with open('servers.json','w',encoding='utf8') as f:
                server[str(message.guild.id)]['snipe'] = False
                server[str(message.guild.id)]['snipe_text'] = False
                server[str(message.guild.id)]['sniper_url'] = False
                server[str(message.guild.id)]['sniper_name'] = False
                json.dump(server,f, sort_keys=True, indent=4, ensure_ascii=False)
                return await message.channel.send("Something went wrong, Please try again")


    @commands.command()
    async def snipe(self,ctx):
        with open('servers.json','r',encoding='utf8') as f:
            server = json.load(f)
            if server[str(ctx.guild.id)]['snipe_text'] == False or server[str(ctx.guild.id)]['snipe'] == False or server[str(ctx.guild.id)]['sniper_url'] == False or server[str(ctx.guild.id)]['sniper_name'] == False:
                if server[str(ctx.guild.id)]['snipe'] == False:
                    return await ctx.send(f"This server not enabled snipe yet, Please contact **{ctx.guild.owner.name}**")
                return await ctx.send("Have nothing to snipe")
            else:
                name = server[str(ctx.guild.id)]['sniper_name']
                content = server[str(ctx.guild.id)]['snipe_text']
                avatar = server[str(ctx.guild.id)]['sniper_url']
                embed = discord.Embed(
                    #title = f"{name}",
                    colour = discord.Colour.green(),
                    description = content
                )
                embed.set_author(name=name,url="",icon_url=avatar)
                await ctx.send(embed=embed)
                
            

def setup(bot):
    bot.add_cog(SNIPE(bot))