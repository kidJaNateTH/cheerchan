import discord
from discord.ext import commands
import json


class MUTE(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.has_permissions(administrator=True)
    @commands.command()
    async def mute(self,ctx,member:discord.Member):
        try:
            try:
                if ctx.guild.id == 719837288670167100:
                    muted = discord.utils.get(ctx.message.author.guild.roles,name="mute")
                    await member.add_roles(muted)

                    channels = 0

                    for i in channel:
                        channels += 1

                    embed = discord.Embed(
                        title = f"PEW, Successfully muted {member.name}",
                        colour = discord.Colour.red(),
                        description = f"{channels} Channels"
                    )
                    await self.bot.get_guild(719837288670167100).get_channel(721257084640952351).send(embed=embed)
                    return
                muted = discord.utils.get(ctx.message.author.guild.roles,name="mute")
                await member.add_roles(muted)
                embed = discord.Embed(
                    title = f"PEW, Successfully muted {member.name}",
                    colour = discord.Colour.red()
                )
                await ctx.send(embed=embed)
            except:
                if ctx.guild.id == 719837288670167100:
                    muted = await ctx.guild.create_role(name="mute")
                    channel = ctx.guild.text_channels

                    channels = 0

                    for i in channel:
                        channels += 1
                        await i.set_permissions(muted, send_messages=False)
                    await member.add_roles(muted)
                    embed = discord.Embed(
                        title = f"PEW, Successfully muted {member.name}",
                        colour = discord.Colour.red(),
                        description = f"{channels} Channels"
                    )
                    await self.bot.get_guild(719837288670167100).get_channel(721257084640952351).send(embed=embed)
                    return
                muted = await ctx.guild.create_role(name="mute")
                channel = ctx.guild.text_channels
                for i in channel:
                    await i.set_permissions(muted, send_messages=False)
                await member.add_roles(muted)
                embed = discord.Embed(
                    title = f"PEW, Successfully muted {member.name}",
                    colour = discord.Colour.red()
                )
                await ctx.send(embed=embed)
        except:
            return await ctx.send("I think i don't have permissions to do that")

    @mute.error
    async def mute_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            embed = discord.Embed(
                title = "ERROR",
                color = discord.Colour.red()
            )
            embed.add_field(name="I think i don't have permissions to do that",value="_ _",inline=True)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("😳")
        if isinstance(error,commands.MissingRequiredArgument):
            with open('servers.json','r',encoding='utf8') as f:
                re = json.load(f)
                prefix = re[str(ctx.guild.id)]['prefix']
            embed = discord.Embed(
                title = "ERROR",
                color = discord.Colour.red()
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/711570460487450687/720820208545169438/cheerchan_sad.png")
            embed.add_field(name=f"Hmm.. Something went wrong? Please try again \n{prefix}mute <user>",value="_ _",inline=True)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("😳")
        
        


def setup(bot):
    bot.add_cog(MUTE(bot))