import discord
from discord.ext import commands
import json


class BAD(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_message(self,message):
        bad = str(message.content).lower()
        try:
            with open('badword.json','r',encoding='utf8') as f:
                w = json.load(f)
                word = w[str(message.guild.id)]['list']
                for i in word:
                    if i in bad:
                        await message.delete()
                        await message.channel.send(f"You're using bad word, <@!{message.author.id}>")
        except:
            return

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def badword(self,ctx,way:str,word:str=None):
        if way == "add":
            if word == None:
                embed = discord.Embed(
                    title = "badword add <your bad word>"
                )
                return await ctx.send(embed=embed)
            with open('badword.json','r',encoding='utf8') as f:
                w = json.load(f)
                wordd = w[str(ctx.guild.id)]['list']
            with open('badword.json','w',encoding='utf8') as f:
                w[str(ctx.guild.id)]['list'][str(word).lower()] = str(word).lower()
                json.dump(w, f, sort_keys=True, indent=4, ensure_ascii=False)
                embed = discord.Embed(
                    title = f"Successfully added {word} in bad word list",
                    colour = discord.Colour.blue()
                )
                for i in wordd:
                    embed.add_field(name=f"{i}",value="_ _",inline=False)
                await ctx.send(embed=embed)
        if way == "remove":
            if word == None:
                embed = discord.Embed(
                    title = "badword remove <your bad word>"
                )
                return await ctx.send(embed=embed)
            with open('badword.json','r',encoding='utf8') as f:
                w = json.load(f)
            with open('badword.json','w',encoding='utf8') as f:
                try:
                    w[str(ctx.guild.id)]['list'].pop(str(word).lower())
                    json.dump(w, f, sort_keys=True, indent=4, ensure_ascii=False)
                except:
                    return await ctx.send(f"{word} Not found")
            with open('badword.json','r',encoding='utf8') as f:
                w = json.load(f)
                wordd = w[str(ctx.guild.id)]['list']
                embed = discord.Embed(
                    title = f"Successfully removed {word} in bad word list",
                    colour = discord.Colour.blue()
                )
                for i in wordd:
                    embed.add_field(name=f"{i}",value="_ _",inline=False)
                await ctx.send(embed=embed)
        if way == "list":
            with open('badword.json','r',encoding='utf8') as f:
                w = json.load(f)
                wordd = w[str(ctx.guild.id)]['list']
                embed = discord.Embed(
                    title = f"Bad word list",
                    colour = discord.Colour.blue()
                )
                for i in wordd:
                    embed.add_field(name=f"{i}",value="_ _",inline=False)
                await ctx.send(embed=embed)
        if way == "clear":
            with open('badword.json','r',encoding='utf8') as f:
                w = json.load(f)
                wordd = w[str(ctx.guild.id)]['list']

                
            with open('badword.json','w',encoding='utf8') as f:
                try:
                    w[str(ctx.guild.id)]['list'].pop('list')
                    json.dump(w, f, sort_keys=True, indent=4, ensure_ascii=False)
                    embed = discord.Embed(
                        title = f"Bad word list",
                        colour = discord.Colour.blue()
                    )
                    await ctx.send(embed=embed)
                except:
                    return await ctx.send(f"{word} Not found")
            
        


def setup(bot):
    bot.add_cog(BAD(bot))