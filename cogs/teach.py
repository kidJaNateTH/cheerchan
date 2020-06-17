import discord
from discord.ext import commands
import json


class TEACH(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def teach(self,ctx,way:str,ff=None,t:str = None):
        if way == "add":
            ff = str(ff).replace("_"," ")
            t = str(t).replace("_"," ")
            try:
                if str(ff).startswith("c!") or str(t).startswith("c!"):
                    return await ctx.send("I know what are you doing")
                with open('teached.json','r',encoding='utf8') as f:
                    chat = json.load(f)

                with open('teached.json','w',encoding='utf8') as f:
                    chat[str(ctx.guild.id)]['words'][str(ff)] = {}
                    chat[str(ctx.guild.id)]['words'][str(ff)]['answer'] = str(t)
                    chat[str(ctx.guild.id)]['words'][str(ff)]['teacher'] = str(ctx.author)
                    json.dump(chat, f, sort_keys=True, indent=4, ensure_ascii=False)

                embed = discord.Embed(
                    title = "You're teached Cheer Chan",
                    description = f"If you says\n```{ff}``` \nCheer Chan will says\n```{t}```",
                    colour = discord.Colour.green()
                )
                await ctx.send(embed=embed)

            except:
                with open('teached.json','w',encoding='utf8') as f:
                    chat[str(ctx.guild.id)] = {}
                    chat[str(ctx.guild.id)]['server_name'] = str(ctx.guild.name)
                    chat[str(ctx.guild.id)]['words'] = {}
                    chat[str(ctx.guild.id)]['words'][str(ff)] = {}
                    chat[str(ctx.guild.id)]['words'][str(ff)]['answer'] = str(t)
                    chat[str(ctx.guild.id)]['words'][str(ff)]['teacher'] = str(ctx.author)
                    json.dump(chat, f, sort_keys=True, indent=4, ensure_ascii=False)

                    embed = discord.Embed(
                        title = "You're teached Cheer Chan",
                        description = f"If you says\n```{ff}``` \nCheer Chan will says\n```{t}```",
                        colour = discord.Colour.green()
                    )
                    await ctx.send(embed=embed)
        if way == "clear":
            try:
                with open('teached.json','r',encoding='utf8') as f:
                    chat = json.load(f)

                with open('teached.json','w',encoding='utf8') as f:
                    chat[str(ctx.guild.id)]['words']= {}
                    json.dump(chat, f, sort_keys=True, indent=4, ensure_ascii=False)
                    embed = discord.Embed(
                        title = f"Successfully clear all knowledges in **{ctx.guild.name}**",
                        colour = discord.Colour.orange()
                    )
                    await ctx.send(embed=embed)
            except:
                return
        if way == "list":
            embed = discord.Embed(
                title  = f"All knowledges in **{ctx.guild.name}**",
                colour = discord.Colour.from_rgb(252, 3, 182)
            )
            with open('teached.json','r',encoding='utf8') as f:
                teach = json.load(f)
                for i in teach[str(ctx.guild.id)]['words']:
                    embed.add_field(name=i,value="_ _",inline=False)
                await ctx.send(embed=embed)

    @teach.error
    async def teach_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            emoji=discord.utils.get(self.bot.emojis,name="yellow_sparksidk")
            embed = discord.Embed(
                title = f"{emoji}Missing required argument{emoji}",
                colour = discord.Colour.red(),
                description = "How to use!\nc!teach add <Question> <Answer> | Add a knowledge to Cheer Chan\nc!teach clear | Clear all knowledges\nc!teach list | List all knowledges\n**_** = Spacebar, Use it if you need to spacebar"
            )
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return
        try:
            with open('teached.json','r',encoding='utf8') as f:
                chat = json.load(f)
                try:
                    if message.content != chat[str(message.guild.id)]['words'][message.content]:
                        try:
                            answer = chat[str(message.guild.id)]['words'][message.content]['answer']
                            await message.channel.send(answer)
                        except:
                            return
                except:
                    return
        except:
            return

def setup(bot):
    bot.add_cog(TEACH(bot))