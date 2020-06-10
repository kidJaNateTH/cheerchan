import discord
from discord.ext import commands
from discord.utils import get
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from discord import Embed


class newhelp(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command()
    async def help(self,ctx):
        embeds = [
            Embed(title=":firecracker: Fun command!", description="`c!dice` Rolling a dice\n`c!fight` Fight with your enemy\n`c!say` Use cheer chan to say something\n`c!avatar` Show your avatar\n`c!yt` Search youtube videos\n`c!emoji` use Cheer chan emoji", color=0x115599),
            Embed(title=":computer: Manage Server!", description="`c!create` Create the channel\n`c!clear` Clear the messages\n`c!ban` Ban...? Yes.. Ban\n`c!dm` Send direct message to someone\n`c!serverinfo` See the server info", color=0x5599ff),
            Embed(title=":diamonds: Minigames!", description="`c!slot` UH..Slot", color=0x191638),
            Embed(title=":jigsaw: Other commands!", description="`c!translate` Translate the languages", color=0x191638),
            Embed(title=":crossed_swords: Levels!", description="`c!profile` See ur profile", color=0x191638),
            Embed(title=":warning: NSFW!", description="`c!hentai` Random hentai pictures\n`c!gelbooru` Get gelbooru picture by tag", color=0x191638),
            Embed(title=":eyes: Memes!", description="`c!dltv` \n`c!bed` \n`c!yesno` \n`c!hack` \n`c!salt`", color=0x191638),
            Embed(title=":microbe: Covid19!", description="`c!corona`", color=0x191638)
        ]
        secembeds = [
            Embed(title=":firecracker: Fun command!", description="`c!dice` Rolling a dice\n`c!fight` Fight with your enemy\n`c!say` Use cheer chan to say something\n`c!avatar` Show your avatar\n`c!yt` Search youtube videos\n`c!emoji` use Cheer chan emoji", color=0x115599),
            Embed(title=":computer: Manage Server!", description="`c!create` Create the channel\n`c!clear` Clear the messages\n`c!ban` Ban...? Yes.. Ban\n`c!dm` Send direct message to someone\n`c!serverinfo` See the server info", color=0x5599ff),
            Embed(title=":diamonds: Minigames!", description="`c!slot` UH..Slot", color=0x191638),
            Embed(title=":crossed_swords: Levels!", description="`c!profile` See ur profile", color=0x191638),
            Embed(title=":warning: NSFW!", description="`c!hentai` Random hentai pictures\n`c!gelbooru` Get gelbooru picture by tag", color=0x191638),
            Embed(title=":eyes: Memes!", description="`c!dltv` \n`c!bed` \n`c!yesno` \n`c!hack` \n`c!salt`", color=0x191638),
            Embed(title=":microbe: Covid19!", description="`c!corona`", color=0x191638),
            Embed(title=":minidisc: Secret commands!", description="`c!snipe`", color=0x191638)
        ]
        if ctx.author.id == 546558917929598978:
            paginator = BotEmbedPaginator(ctx, secembeds)
            await paginator.run()
        else:
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()



def setup(bot):
    bot.add_cog(newhelp(bot))