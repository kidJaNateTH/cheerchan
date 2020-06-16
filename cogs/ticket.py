import discord
from discord.ext import commands
import asyncio
import json


class TICKET(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['tic'])
    async def ticket(self,ctx):
        with open('servers.json','r',encoding='utf8') as f:
            server = json.load(f)
            try:
                if server[str(ctx.guild.id)]['ticket'] == True:
                    guild = ctx.message.guild
                    tic = await guild.create_text_channel(f"ticket-{ctx.author.name}")

                    try:
                        await tic.set_permissions(ctx.guild.default_role, send_messages=False,read_messages=False)
                        await tic.set_permissions(ctx.author, send_messages=True,read_messages=True)
                    except:
                        await ctx.send("Hmm, I think i don't have permissions")

                    await tic.send("Ticket channel create sucessful")
                    name = str(ctx.author.name).lower()
                    await ctx.send(f"Create ticket-{name} successful")
                else:
                    return await ctx.send(f"This server, {ctx.guild.name} have not enabled ticket, Please contect {ctx.guild.owner}")
            except:
                with open('servers.json','w',encoding='utf8') as f:
                    server[str(ctx.guild.id)] = {}
                    server[str(ctx.guild.id)]['Server_name'] = str(ctx.guild.name)
                    server[str(ctx.guild.id)]['ticket'] = False
                    json.dump(server, f, sort_keys=True, indent=4, ensure_ascii=False)
                    return await ctx.send(f"This server, {ctx.guild.name} have not enabled ticket, Please contact {ctx.guild.owner}")
        
    @commands.command(aliases=['ticend'])
    async def ticketend(self,ctx):
        if str(ctx.channel.name).startswith('ticket-'):
            embed = discord.Embed(
                title = f"{ctx.channel.name} will be deleted in 5 seconds",
                colour = discord.Colour.red(),
            )
            await ctx.send(embed=embed)
            await asyncio.sleep(5)
            channel = ctx.channel
            await channel.delete()
        else:
            embed = discord.Embed(
                title = f"**{ctx.channel.name}** is not ticket channel",
                colour = discord.Colour.red(),
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=['settings','option','options'])
    async def setting(self,ctx,t:str,wat:str):
        if not ctx.author.id == ctx.guild.owner.id:
            return await ctx.send(f"You're not **{ctx.guild.name}** owner")
        if t == "ticket":
            if wat == "true" or wat == "True":
                with open('servers.json','r',encoding='utf8') as f:
                    server = json.load(f)
                with open('servers.json','w',encoding='utf8') as f:
                    server[str(ctx.guild.id)]['ticket'] = True
                    json.dump(server, f, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send("Enabled ticket successful")
                    return
            if wat == "false" or wat == "False":
                with open('servers.json','r',encoding='utf8') as f:
                    server = json.load(f)
                with open('servers.json','w',encoding='utf8') as f:
                    server[str(ctx.guild.id)]['ticket'] = False
                    json.dump(server, f, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send("Disabled ticket successful")
                    return
    

def setup(bot):
    bot.add_cog(TICKET(bot))