import discord
from discord.ext import commands
import json


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
    async def jsonstatus(self,ctx,t:str=None):
        if t == None:
            with open('users.json', 'r',encoding='utf8') as f:
                users = json.load(f)
                user = json.dumps(users,indent=4,ensure_ascii=False)
                embed = discord.Embed(
                    title = "Users.json Status",
                    description = user,
                    colour = discord.Colour.red()
                )
                await ctx.send(embed=embed)
        if not t == None:
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
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(owner(bot))