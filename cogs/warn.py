import discord
from discord.ext import commands
import json


class WARN(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def warn(self,ctx,member:discord.Member,*,reason=None):
        if member.bot:
            return
        if reason == None:
            reason = "No reason"
        
        count = 0
        with open('servers.json','r',encoding='utf8') as f:
            w = json.load(f)
            try:
                count = w[str(ctx.guild.id)]['warn'][str(member.id)]['count']
            except:
                pass
        with open('servers.json','w',encoding='utf8') as f:
            w[str(ctx.guild.id)]['warn'][str(member.id)] = {}
            w[str(ctx.guild.id)]['warn'][str(member.id)]['name'] = str(member.name)
            
            try:
                print("+1")
                w[str(ctx.guild.id)]['warn'][str(member.id)]['count'] = count + 1
            except:
                print("0")
                w[str(ctx.guild.id)]['warn'][str(member.id)]['count'] = 0
            json.dump(w, f, sort_keys=True, indent=4, ensure_ascii=False)
            embed = discord.Embed(
                title = f"OOF, {member} has been warned",
                description = f"{reason}",
                colour = discord.Colour.red()
            )
            embed.add_field(name=f"{count} Warning(s)",value="_ _",inline=False)
            embed.set_footer(text=f"Warned by {ctx.author.name}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)

        return

            


def setup(bot):
    bot.add_cog(WARN(bot))