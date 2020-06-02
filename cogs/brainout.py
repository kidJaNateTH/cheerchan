import discord
from discord.ext import commands
from discord.utils import get


class brainout(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['create','c'])
    async def createroom(self,ctx,name:str):
        guild = ctx.message.guild
        await guild.create_text_channel(name)
        msg = await ctx.send("Your room has been created")
        await msg.add_reaction("😘")
    @createroom.error
    async def createroom_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Hmm.. Something went wrong? Please try again \n`c!create <str>`")
            await msg.add_reaction("😳")
        if isinstance(error, commands.MissingPermissions):
            msg = await ctx.send(f"Hmm.. I think you need more puppy")
            await msg.add_reaction("😳")

    @commands.command(aliases=['cha'])
    async def challenge(self,ctx,page:str):
        if(page == '1'):
            embed = discord.Embed(
                colour = discord.Color.red(),
                title = "Challenge 1: Drink",
                description = "Hint: There is two kind of drinks here, can you find out all? ( w--e--e--n--i-e ; w---r )"
            )
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Request by {ctx.author.name}")
            embed.set_image(url='https://cdn.discordapp.com/attachments/644400369056612373/665117873470963730/bo1.png')
            await ctx.send(embed=embed)
        if(page == '2'):
            embed = discord.Embed(
                colour = discord.Color.red(),
                title = "Challenge 2: Time",
                description = "In this case, you have to type the formula. (Hint: Don't believe what you look, what time is it? c--re-tt--e[type a math symbol here][type a time here [][]:[][] )"
            )
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Request by {ctx.author.name}")
            embed.set_image(url='https://cdn.discordapp.com/attachments/644400369056612373/666244416398426122/bo2.png')
            await ctx.send(embed=embed)
        if(page == '3'):
            embed = discord.Embed(
                colour = discord.Color.red(),
                title = "Challenge 3: Numbers",
                description = "Type ??=[numbers here] (Hint: Try to find the rules of it, 1+2+3 is the first...)"
            )
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Request by {ctx.author.name}")
            embed.set_image(url='https://cdn.discordapp.com/attachments/644400369056612373/669508588355715114/bo3.png')
            await ctx.send(embed=embed)

        




def setup(bot):
    bot.add_cog(brainout(bot))