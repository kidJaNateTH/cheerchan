import discord
from discord.ext import commands
import json
import asyncio


class owner(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.is_owner()
    @commands.command()
    async def give(self,ctx,member:discord.Member,t:str,amout:int):
        if member.bot:
            return
        with open('users.json', 'r',encoding='utf8') as f:
            users = json.load(f)
        with open('users.json', 'w',encoding='utf8') as f:
            if t == "premium":
                if amout == 1:
                    users[str(member.id)]['premium'] = True
                    await ctx.send(f"I give premium to {member.name}")

                    embed = discord.Embed(
                        title = f"{member.name} has bought Cheer Chan premium!",
                        description = f"With <@!{ctx.author.id}> giveaways",
                        colour = discord.Colour.gold()
                    )
                    embed.set_thumbnail(url=member.avatar_url)
                    await self.bot.get_guild(719837288670167100).get_channel(721257084640952351).send(embed=embed)
                if amout == 0:
                    users[str(member.id)]['premium'] = False
                    await ctx.send(f"I disabled premium to {member.name}")
            if t == 'coins':
                users[str(member.id)]['coins'] = amout
                await ctx.send(f"I set {member.name}'s coins to {amout}")
            if t == 'lvl':
                users[str(member.id)]['lvl'] = amout
                await ctx.send(f"I set {member.name}'s levels to {amout}")
            if t == 'exp':
                users[str(member.id)]['exp'] = amout
                await ctx.send(f"I set {member.name}'s exp to {amout}")
            json.dump(users, f, sort_keys=True, indent=4, ensure_ascii=False)

    @commands.is_owner()
    @commands.command()
    async def userstatus(self,ctx,t:str=None):
        if t == None:
            try:
                with open('users.json', 'r',encoding='utf8') as f:
                    users = json.load(f)
                    user = json.dumps(users,indent=4,ensure_ascii=False)
                    embed = discord.Embed(
                        title = "Users.json Status",
                        description = user,
                        colour = discord.Colour.red()
                    )
                    user = self.bot.get_user(ctx.author.id)
                    await user.send(embed=embed)
            except:
                try:
                    user = self.bot.get_user(ctx.author.id)
                    await user.send(file=discord.File(f.name))
                    await ctx.send(f"I has send {f.name} to your DM check it out!")
                except:
                    await ctx.send(f"{f.name} size is more than 8mb")
        if not t == None:
            try:
                with open('users.json', 'r',encoding='utf8') as f:
                    users = json.load(f)
                    u = users[t]
                    name = users[t]['username']
                    user = json.dumps(u,indent=4,ensure_ascii=False)
                    username = json.dumps(name,indent=4,ensure_ascii=False)
                    embed = discord.Embed(
                        title = f"{username} Status",
                        description = user,
                        colour = discord.Colour.red()
                    )
                    user = self.bot.get_user(ctx.author.id)
                    await user.send(embed=embed)
                    await ctx.send(f"I has send {f.name} to your DM check it out!")
            except:
                try:
                    user = self.bot.get_user(ctx.author.id)
                    await user.send(file=discord.File(f.name))
                    await ctx.send(f"I has send {f.name} to your DM check it out!")
                except:
                    await ctx.send(f"{f.name} size is more than 8mb")
        
    @commands.is_owner()
    @commands.command()
    async def serverstatus(self,ctx,t:str=None):
        if t == None:
            with open('servers.json', 'r',encoding='utf8') as f:
                try:
                    users = json.load(f)
                    user = json.dumps(users,indent=4,ensure_ascii=False)
                    embed = discord.Embed(
                        title = "Servers.json Status",
                        description = user,
                        colour = discord.Colour.red()
                    )
                    user = self.bot.get_user(ctx.author.id)
                    await user.send(embed=embed)
                    await ctx.send(f"I has send {f.name} to your DM check it out!")
                except:
                    try:
                        user = self.bot.get_user(ctx.author.id)
                        await user.send(file=discord.File(f.name))
                        await ctx.send(f"I has send {f.name} to your DM check it out!")
                    except:
                        await ctx.send(f"{f.name} size is more than 8mb")
        if not t == None:
            try:
                with open('servers.json', 'r',encoding='utf8') as f:
                    users = json.load(f)
                    u = users[t]
                    name = users[t]['Server_name']
                    user = json.dumps(u,indent=4,ensure_ascii=False)
                    username = json.dumps(name,indent=4,ensure_ascii=False)
                    embed = discord.Embed(
                        title = f"{username} Status",
                        description = user,
                        colour = discord.Colour.red()
                    )
                    user = self.bot.get_user(ctx.author.id)
                    await user.send(embed=embed)
                    await ctx.send(f"I has send {f.name} to your DM check it out!")
            except:
                try:
                    user = self.bot.get_user(ctx.author.id)
                    await user.send(file=discord.File(f.name))
                    await ctx.send(f"I has send {f.name} to your DM check it out!")
                except:
                    await ctx.send(f"{f.name} size is more than 8mb")

    @commands.is_owner()
    @commands.command()
    async def servers(self,ctx):
        emoji=discord.utils.get(self.bot.emojis,name="loading")
        embed1= discord.Embed(
            title = f":mag: Finding... {emoji}",
            colour = discord.Colour.orange()
        )
        msg = await ctx.send(embed=embed1)
        await msg.add_reaction(emoji)
        await asyncio.sleep(2)
        embed = discord.Embed(
            title = "Servers with Cheer Chan",
            colour = discord.Colour.blue()
        )
        for i in self.bot.guilds:
            print(i)
            embed.add_field(name=i,value="_ _",inline=False)
        await msg.edit(embed=embed)
        await msg.clear_reaction(emoji)



def setup(bot):
    bot.add_cog(owner(bot))