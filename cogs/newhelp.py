import discord
from discord.ext import commands
from discord.utils import get
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from discord import Embed
import json


class newhelp(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def help(self,ctx,t:str=None):
        if(t == "premium" or t == "Premium"):
            with open("servers.json","r",encoding="utf8") as f:
                server = json.load(f)
                prefix = server[str(ctx.guild.id)]['prefix']
            embed = discord.Embed(
                title = "Cheer Chan premium!",
                colour = discord.Color.from_rgb(255, 247, 0)
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/711570460487450687/721929129112502322/crown.png")
            embed.add_field(name=":thinking: What can Premium do? ",value="Customize your profile! 💎 \nGet the supporter role in my server 🎉 \n[[Cheer Chan Support server]](https://discord.gg/MVwkZt7) ↤ 🎀 \nUse external emojis from other server 🍕 \n\nAnd supporting us who work hard 😊 ",inline=False)

            embed.add_field(name="🎨 How can I buy Premium?",value=f"Type `{prefix}premium` :white_heart:\nClick at `[Click here]` :white_heart:\nExecute payment :white_heart:\nType `{prefix}premium @you verify [PAYID] [PayerID]` :white_heart:\nIf you have any questions or problems pls [contact](https://discord.gg/MVwkZt7) us :white_heart:\nP.S. If you are afraid you can buy premium on your private server :heart:",inline=False)
            
            embed.add_field(name="✨ Can I have Premium for free?",value="In the [Cheer Chan Support](https://discord.gg/MVwkZt7) server, there are Premium giveaways for free! :money_with_wings:",inline=False)
            
            await ctx.send(embed=embed)
            return

        with open("servers.json","r",encoding="utf8") as f:
            server = json.load(f)
            prefix = server[str(ctx.guild.id)]['prefix']
            embeds = [
                Embed(title=":firecracker: Fun command!", description=f"`{prefix}dice` Rolling a dice\n`{prefix}fight` Fight with your enemy\n`{prefix}say` Use cheer chan to say something\n`{prefix}avatar` Show your avatar\n`{prefix}yt` Search youtube videos\n`{prefix}emoji` use Cheer chan emoji\n`{prefix}teach` Teach Cheer Chan", color=0x115599),
                Embed(title=":computer: Manage Server!", description=f"`{prefix}create` Create the channel\n`{prefix}clear` Clear the messages\n`{prefix}ban` Ban...? Yes.. Ban\n`{prefix}dm` Send direct message to someone\n`{prefix}serverinfo` See the server info\n`{prefix}ticket` Create a ticket in this server\n`{prefix}snipe` See the deleted messages in the server\n`{prefix}prefix` Change Cheer Chan's prefix\n`{prefix}setting` Settings the server\n`{prefix}mute` Mute someone\n`{prefix}unmute` Unmute someone\n`{prefix}warn` Warn someone\n`{prefix}promote` Promote your servers!", color=0x5599ff),
                
                Embed(title=":gear: Server Settings!", description=f"`{prefix}serverinfo` See the server info\n`{prefix}prefix` Change Cheer Chan's prefix\n`{prefix}setting` Settings the server", color=0x5599ff), 
                
                
                Embed(title=":diamonds: Minigames!", description=f"`{prefix}slot` UH..Slot", color=0x191638),
                Embed(title=":jigsaw: Other commands!", description=f"`{prefix}translate` Translate the languages", color=0x191638),
                
                Embed(title=":crossed_swords: Levels!", description=f"`{prefix}profile` See ur profile", color=0x191638),

                Embed(title=":crown: Premium!", description=f"`{prefix}customprofile` Custom your profile\n`{prefix}premium` buy a premium or send it to someone\n`{prefix}emoji` use external emojis from other server", color=0x191638),

                Embed(title=":warning: NSFW!", description=f"`{prefix}hentai` Random hentai pictures\n`{prefix}gelbooru` Get gelbooru picture by tag", color=0x191638),
                Embed(title=":eyes: Memes!", description=f"`{prefix}dltv` \n`{prefix}bed` \n`{prefix}yesno` \n`{prefix}hack` \n`{prefix}salt` \n`{prefix}wanted`", color=0x191638),
                Embed(title=":microbe: Covid19!", description=f"`{prefix}corona`", color=0x191638)
            ]
            secembeds = [
                Embed(title=":firecracker: Fun command!", description=f"`{prefix}dice` Rolling a dice\n`{prefix}fight` Fight with your enemy\n`{prefix}say` Use cheer chan to say something\n`{prefix}avatar` Show your avatar\n`{prefix}yt` Search youtube videos\n`{prefix}emoji` use Cheer chan emoji\n`{prefix}teach` Teach Cheer Chan", color=0x115599),
                Embed(title=":computer: Manage Server!", description=f"`{prefix}create` Create the channel\n`{prefix}clear` Clear the messages\n`{prefix}ban` Ban...? Yes.. Ban\n`{prefix}dm` Send direct message to someone\n`{prefix}ticket` Create a ticket in this server\n`{prefix}snipe` See the deleted messages in the server\n`{prefix}mute` Mute someone\n`{prefix}unmute` Unmute someone\n`{prefix}warn` Warn someone\n`{prefix}promote` Promote your servers!", color=0x5599ff),
                
                Embed(title=":gear: Server Settings!", description=f"`{prefix}serverinfo` See the server info\n`{prefix}prefix` Change Cheer Chan's prefix\n`{prefix}setting` Settings the server", color=0x5599ff), 

                Embed(title=":diamonds: Minigames!", description=f"`{prefix}slot` UH..Slot", color=0x191638),
                Embed(title=":crossed_swords: Levels!", description=f"`{prefix}profile` See ur profile", color=0x191638),
                
                Embed(title=":crown: Premium!", description=f"`{prefix}customprofile` Custom your profile\n`{prefix}premium` buy a premium or send it to someone\n`{prefix}emoji` use external emojis from other server", color=0x191638),
                
                Embed(title=":warning: NSFW!", description=f"`{prefix}hentai` Random hentai pictures\n`{prefix}gelbooru` Get gelbooru picture by tag", color=0x191638),
                Embed(title=":eyes: Memes!", description=f"`{prefix}dltv` \n`{prefix}bed` \n`{prefix}yesno` \n`{prefix}hack` \n`{prefix}salt` \n`{prefix}wanted`", color=0x191638),
                Embed(title=":microbe: Covid19!", description=f"`{prefix}corona`", color=0x191638),
                Embed(title=":minidisc: Secret commands!", description=f"`{prefix}give`\n`{prefix}serverstatus`\n`{prefix}userstatus`\n`{prefix}servers`", color=0x191638)
            ]
            if ctx.author.id == 546558917929598978:
                paginator = BotEmbedPaginator(ctx, secembeds)
                await paginator.run()
            else:
                paginator = BotEmbedPaginator(ctx, embeds)
                await paginator.run()



def setup(bot):
    bot.add_cog(newhelp(bot))