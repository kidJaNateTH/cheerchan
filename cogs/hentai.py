import discord
from discord.ext import commands
from discord.utils import get
import random
from random import Random
import string


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def hentai(self,ctx,amount:int):
        if not ctx.channel.is_nsfw():
            return await ctx.send(f"You must use this command in NSFW channel :warning:")
        link1 = 'https://img1.gelbooru.com/thumbnails/d6/b7/thumbnail_d6b7a1a06c8a51a1f274f9b051da50cb.jpg'
        link2 = 'https://img1.gelbooru.com/thumbnails/d9/b0/thumbnail_d9b06e03762a8e2c5cb7240c5c8d1a69.jpg'
        link3 = 'https://img1.gelbooru.com/thumbnails/78/7c/thumbnail_787c228c0be8eb8d0e738d678c45a701.jpg'
        link4 = 'https://img1.gelbooru.com/thumbnails/2a/7f/thumbnail_2a7f2e93ad06cc48e6d4ec922c625ce1.jpg'
        link5 = 'https://img1.gelbooru.com/thumbnails/52/fd/thumbnail_52fd03dde5352d5106931d65ba9c6721.jpg'
        link6 = 'https://img1.gelbooru.com/thumbnails/94/74/thumbnail_9474b29b20b2b4c271a3b7549ed4f51c.jpg'
        link7 = 'https://img1.gelbooru.com/thumbnails/e5/e6/thumbnail_e5e6a148c8dc8f38b7902bcabcd82286.jpg'
        link8 = 'https://img1.gelbooru.com/thumbnails/2a/90/thumbnail_2a9082de7a7ad7adbbc2dde30c71d56a.jpg'
        link9 = 'https://img1.gelbooru.com/thumbnails/03/e4/thumbnail_03e4413a7f465a27977ed8bc997c5ae0.jpg'
        link10 = 'https://img1.gelbooru.com/thumbnails/2c/21/thumbnail_2c214354eac9c4104243bcda240f0569.jpg'
        link11 = 'https://img1.gelbooru.com/thumbnails/f5/88/thumbnail_f5889ad9f407baf85890dc9527b67e7f.jpg'
        link12 = 'https://img1.gelbooru.com/thumbnails/8c/84/thumbnail_8c8483174cede1ebeacc118a69f6886f.jpg'
        link13 = 'https://img1.gelbooru.com/thumbnails/d7/05/thumbnail_d705621d2049938ee87319f41c4acc68.jpg'
        link14 = 'https://img1.gelbooru.com/thumbnails/8a/e3/thumbnail_8ae3929ce3ff1d20b6b1b021fb2a9655.jpg'
        link15 = 'https://img1.gelbooru.com/thumbnails/d2/f5/thumbnail_d2f51ef62821d2466a5c2b4250ee3b4a.jpg'
        link16 = 'https://img1.gelbooru.com/thumbnails/87/54/thumbnail_8754f7848c038ef6f53ac986728f09fc.jpg'
        link17 = 'https://img1.gelbooru.com/thumbnails/73/b7/thumbnail_73b7087a272d25931c258b743ff1d36e.jpg'
        link18 = 'https://img1.gelbooru.com/thumbnails/c6/8a/thumbnail_c68ac5fb818b108d1b14bfe132f13bfc.jpg'
        link19 = 'https://img1.gelbooru.com/thumbnails/c4/27/thumbnail_c42743e2e8372ee78d625571918a73d9.jpg'
        link20 = 'https://img1.gelbooru.com/thumbnails/d0/a5/thumbnail_d0a57f849758d81907cc1a75ebf82a31.jpg'
        link21 = 'https://img1.gelbooru.com/thumbnails/69/92/thumbnail_6992e21043e11d525cca5de8301c0e46.jpg'
        link22 = 'https://img1.gelbooru.com/thumbnails/cc/24/thumbnail_cc24c584ae26e2262b55f257704c7976.jpg'
        link23 = 'https://img1.gelbooru.com/thumbnails/eb/1f/thumbnail_eb1f71bb00a99a2b574fc65112fedd0b.jpg'
        link24 = 'https://img1.gelbooru.com/thumbnails/2b/6b/thumbnail_2b6bec6da1e1d74367919eb3dc8e8575.jpg'
        link25 = 'https://img1.gelbooru.com/thumbnails/0e/8c/thumbnail_0e8c1e1b80f778e5847d28c140b8d007.jpg'
        link26 = 'https://img1.gelbooru.com/thumbnails/13/fd/thumbnail_13fd8a453befb306c4e7b6dce43a25ce.jpg'
        link27 = 'https://img1.gelbooru.com/thumbnails/80/21/thumbnail_8021056d7d54973cd0aa852c4a5fc99d.jpg'
        link28 = 'https://img1.gelbooru.com/thumbnails/98/fd/thumbnail_98fdbd61779aebf45cfcc340c36c91d3.jpg'
        link29 = 'https://img1.gelbooru.com/thumbnails/72/14/thumbnail_72140096038af2f477699a76dbcfe308.jpg'
        if 20 <= amount:
                return await ctx.send("Hoi! It's too much for me, I hate ~~Hentai~~ because you")
        limit = 0
        while(amount>limit):
            randomimage = random.randint(1,29)
            
            embed = discord.Embed(
                colour = discord.Colour.green()
            )
            if(randomimage==1):
                embed.set_image(url=link1)
            if(randomimage==2):
                embed.set_image(url=link2)
            if(randomimage==3):
                embed.set_image(url=link3)
            if(randomimage==4):
                embed.set_image(url=link4)
            if(randomimage==5):
                embed.set_image(url=link5)
            if(randomimage==6):
                embed.set_image(url=link6)
            if(randomimage==7):
                embed.set_image(url=link7)
            if(randomimage==8):
                embed.set_image(url=link8)
            if(randomimage==9):
                embed.set_image(url=link9)
            if(randomimage==10):
                embed.set_image(url=link10)
            if(randomimage==11):
                embed.set_image(url=link11)
            if(randomimage==12):
                embed.set_image(url=link12)
            if(randomimage==13):
                embed.set_image(url=link13)
            if(randomimage==14):
                embed.set_image(url=link14)
            if(randomimage==15):
                embed.set_image(url=link15)
            if(randomimage==16):
                embed.set_image(url=link16)
            if(randomimage==17):
                embed.set_image(url=link17)
            if(randomimage==18):
                embed.set_image(url=link18)
            if(randomimage==19):
                embed.set_image(url=link19)
            if(randomimage==20):
                embed.set_image(url=link20)
            if(randomimage==21):
                embed.set_image(url=link21)
            if(randomimage==22):
                embed.set_image(url=link22)
            if(randomimage==23):
                embed.set_image(url=link23)
            if(randomimage==24):
                embed.set_image(url=link24)
            if(randomimage==25):
                embed.set_image(url=link25)
            if(randomimage==26):
                embed.set_image(url=link26)
            if(randomimage==27):
                embed.set_image(url=link27)
            if(randomimage==28):
                embed.set_image(url=link28)
            if(randomimage==29):
                embed.set_image(url=link29)
            embed.set_footer(text='Power by Gelbooru')
            await ctx.send(embed=embed)
            limit = limit +1

    @hentai.error
    async def hentai_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(f"Hmm.. Something went wrong? Please try again \n`c!hentai <int>`")
            await msg.add_reaction("😳")



def setup(bot):
    bot.add_cog(ping(bot))