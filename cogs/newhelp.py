import discord
from discord.ext import commands
from discord.utils import get
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from discord import Embed


class newhelp(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def help(self,ctx,t:str=None):
        if(t == "premium" or t == "Premium"):
            embed = discord.Embed(
                title = "Cheer Chan premium!",
                colour = discord.Color.from_rgb(255, 247, 0)
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/711570460487450687/721929129112502322/crown.png")
            embed.add_field(name=":thinking: What can Premium do? ",value="Customize your profile! 💎 \nGet the supporter role in my server 🎉 \n[[Cheer Chan Support server]](https://discord.gg/MVwkZt7) ↤ 🎀 \nUse external emojis from other server 🍕 \n\nAnd supporting us who work hard 😊 ",inline=False)

            embed.add_field(name="🎨 How can I buy Premium?",value="Type `c!premium` :white_heart:\nClick at `[Click here]` :white_heart:\nExecute payment :white_heart:\nType `c!premium @you verify [PAYID] [PayerID]` :white_heart:\nIf you have any questions or problems pls [contact](https://discord.gg/MVwkZt7) us :white_heart:\nP.S. If you are afraid you can buy premium on your private server :heart:",inline=False)
            
            embed.add_field(name="✨ Can I have Premium for free?",value="In the [Cheer Chan Support](https://discord.gg/MVwkZt7)server, there are Premium giveaways for free! :money_with_wings:",inline=False)
            
            await ctx.send(embed=embed)
            return
        embeds = [
            Embed(title=":firecracker: Fun command!", description="`c!dice` Rolling a dice\n`c!fight` Fight with your enemy\n`c!say` Use cheer chan to say something\n`c!avatar` Show your avatar\n`c!yt` Search youtube videos\n`c!emoji` use Cheer chan emoji\n`c!teach` Teach Cheer Chan", color=0x115599),
            Embed(title=":computer: Manage Server!", description="`c!create` Create the channel\n`c!clear` Clear the messages\n`c!ban` Ban...? Yes.. Ban\n`c!dm` Send direct message to someone\n`c!serverinfo` See the server info\n`c!ticket` Create a ticket in this server\n`c!snipe` See the deleted messages in the server", color=0x5599ff),
            Embed(title=":diamonds: Minigames!", description="`c!slot` UH..Slot", color=0x191638),
            Embed(title=":jigsaw: Other commands!", description="`c!translate` Translate the languages", color=0x191638),
            
            Embed(title=":crossed_swords: Levels!", description="`c!profile` See ur profile", color=0x191638),

            Embed(title=":crown: Premium!", description="`c!customprofile` Custom your profile\n`c!premium` buy a premium or send it to someone\n`c!emoji` use external emojis from other server", color=0x191638),

            Embed(title=":warning: NSFW!", description="`c!hentai` Random hentai pictures\n`c!gelbooru` Get gelbooru picture by tag", color=0x191638),
            Embed(title=":eyes: Memes!", description="`c!dltv` \n`c!bed` \n`c!yesno` \n`c!hack` \n`c!salt` \n`c!wanted`", color=0x191638),
            Embed(title=":microbe: Covid19!", description="`c!corona`", color=0x191638)
        ]
        secembeds = [
            Embed(title=":firecracker: Fun command!", description="`c!dice` Rolling a dice\n`c!fight` Fight with your enemy\n`c!say` Use cheer chan to say something\n`c!avatar` Show your avatar\n`c!yt` Search youtube videos\n`c!emoji` use Cheer chan emoji\n`c!teach` Teach Cheer Chan", color=0x115599),
            Embed(title=":computer: Manage Server!", description="`c!create` Create the channel\n`c!clear` Clear the messages\n`c!ban` Ban...? Yes.. Ban\n`c!dm` Send direct message to someone\n`c!serverinfo` See the server info\n`c!ticket` Create a ticket in this server\n`c!snipe` See the deleted messages in the server", color=0x5599ff),
            Embed(title=":diamonds: Minigames!", description="`c!slot` UH..Slot", color=0x191638),
            Embed(title=":crossed_swords: Levels!", description="`c!profile` See ur profile", color=0x191638),
            
            Embed(title=":crown: Premium!", description="`c!customprofile` Custom your profile\n`c!premium` buy a premium or send it to someone\n`c!emoji` use external emojis from other server", color=0x191638),
            
            Embed(title=":warning: NSFW!", description="`c!hentai` Random hentai pictures\n`c!gelbooru` Get gelbooru picture by tag", color=0x191638),
            Embed(title=":eyes: Memes!", description="`c!dltv` \n`c!bed` \n`c!yesno` \n`c!hack` \n`c!salt` \n`c!wanted`", color=0x191638),
            Embed(title=":microbe: Covid19!", description="`c!corona`", color=0x191638),
            Embed(title=":minidisc: Secret commands!", description="`c!give`\n`c!serverstatus`\n`c!userstatus`\n`c!servers`", color=0x191638)
        ]
        if ctx.author.id == 546558917929598978:
            paginator = BotEmbedPaginator(ctx, secembeds)
            await paginator.run()
        else:
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()



def setup(bot):
    bot.add_cog(newhelp(bot))