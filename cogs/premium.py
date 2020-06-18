import paypalrestsdk
from paypalrestsdk import Payment
import json
from discord import utils
from discord.utils import get

import discord
from discord.ext import commands


class paypal(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    paypalrestsdk.configure({
        "mode": "live", # sandbox or live
        "client_id": "AUvsxWM9mdHP7Y_ajYOVlQBmzvgngTIahWeYEelgJdNoJfMQWHpUyPWX1NSsaOrc-yiNaxPenxWH6hVo",
        "client_secret": "EPxYOpm_Nbr7w8MxH9_2IALl7gdzueYlnyoiRQqobU1Q4_b7EXygkY0VimMdYXzNHDqJSkEZtfsnzqRL" })

    @commands.command()
    async def premium(self,ctx,member:discord.Member= None,t:str=None,pay:str=None,payid:str=None):
        member = ctx.author if not member else member
        with open('users.json','r',encoding='utf8') as f:
            users = json.load(f)
            if users[str(member.id)]['premium'] == True:
                return await ctx.send(f"<@!{member.id}> already have premium")
        if t == "verify":
            try:
                authorization = Payment.find(pay)
                print("Got Authorization details for Authorization[%s]" % (authorization.id))
                if authorization.execute({"payer_id": payid}):
                    print("Payment[%s] execute successfully" % (authorization.id))
                    with open('premiumbuylog.txt','r') as f:
                        if not pay in f.read():
                            with open('premiumbuylog.txt','a',encoding='utf8') as f:
                                f.write(f"{pay} {member.id} {member.name}\n")
                            with open('users.json','r',encoding='utf8') as f:
                                users = json.load(f)
                            with open('users.json','w',encoding='utf8') as f:
                                users[str(member.id)]['premium'] = True
                                json.dump(users,f,sort_keys=True, indent=4, ensure_ascii=False)
                                await ctx.send("Payment Successful")
                                await ctx.send(f"Premium activated to <@!{member.id}>")

                                embed = discord.Embed(
                                    title = f"{member.name} has bought Cheer Chan premium!",
                                    description = f"With paypal for 1 USD",
                                    colour = discord.Colour.gold()
                                )
                                embed.set_thumbnail(url=member.avatar_url)
                                await self.bot.get_guild(719837288670167100).get_channel(721257084640952351).send(embed=embed)
                        else:
                            await ctx.send("This payment has used already")
                else:
                    error = json.load(authorization.error)
                    return await ctx.send(error['message'])
                return
            except:
                return await ctx.send("Not found your payment")



        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "https://www.cheerchan.xyz/",
                "cancel_url": "https://www.cheerchan.xyz/"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "Premium",
                        "sku": "Cheer Chan",
                        "price": "1.00",
                        "currency": "USD",
                        "quantity": 1}]},
                "amount": {
                    "total": "1.00",
                    "currency": "USD"},
                "description": "Cheer Chan premium."}]})

        if payment.create():
            print("Payment created successfully")
            for link in payment.links:
                if link.rel == "approval_url":
                    # Convert to str to avoid Google App Engine Unicode issue
                    # https://github.com/paypal/rest-api-sdk-python/pull/58
                    approval_url = str(link.href)
                    embed = discord.Embed(
                        title = "Premiun",
                        colour =discord.Colour.gold(),
                    )
                    embed.set_image(url="https://cdn.discordapp.com/attachments/711570460487450687/722022953327263744/GIF-200615_163635.gif")
                    embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/250_Paypal_logo-512.png")
                    embed.add_field(name="Approval link",value=f"[[Click here]]({approval_url})",inline=True)
                    embed.add_field(name="_ _",value="[[Have a problems?]](https://discord.gg/MVwkZt7)",inline=False)
                    await ctx.send(embed=embed)

                    embed = discord.Embed(
                        title = "Cheer Chan premium!",
                        colour = discord.Color.from_rgb(255, 247, 0)
                    )
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/711570460487450687/721929129112502322/crown.png")
                    embed.add_field(name=":thinking: What can Premium do? ",value="Customize your profile! 💎 \nGet the supporter role in my server 🎉 \n[[Cheer Chan Support server]](https://discord.gg/MVwkZt7) ↤ 🎀 \nUse external emojis from other server 🍕\n\nAnd supporting us who work hard 😊 ",inline=False)

                    embed.add_field(name="🎨 How can I buy Premium?",value="Type `c!premium` :white_heart:\nClick at `[Click here]` :white_heart:\nExecute payment :white_heart:\nType `c!premium @you verify [PAYID] [PayerID]` :white_heart:\nIf you have any questions or problems pls [contact](https://discord.gg/MVwkZt7) us :white_heart:\nP.S. If you are afraid you can buy premium on your private server :heart:",inline=False)
                    
                    embed.add_field(name="✨ Can I have Premium for free?",value="In the [Cheer Chan Support](https://discord.gg/MVwkZt7)server, there are Premium giveaways for free! :money_with_wings:",inline=False)
                    
                    await ctx.send(embed=embed)
        else:
            print(payment.error)

    @commands.is_owner()
    @commands.command()
    async def premiumlog(self,ctx):
        with open('premiumbuylog.txt','r',encoding='utf8') as f:
            try:
                user = self.bot.get_user(ctx.author.id)
                await user.send(f.read())
                await ctx.send("I has send all premium logs to your DM")
            except:
                await ctx.send("something went wrong")
                
    @commands.command()
    async def emoji(self,ctx,emoname:str):
        with open('users.json','r',encoding='utf8') as f:
            users = json.load(f)
            if users[str(ctx.author.id)]['premium'] == True:
                try:
                    msg = ctx.message
                    emoji=discord.utils.get(self.bot.emojis,name=emoname)
                    await ctx.send(emoji)
                    await msg.delete()
                except:
                    await ctx.send(f"Emoji {emoname} not found")
            else:
                embed = discord.Embed(
                    title = "Cheer Chan premium!",
                    colour = discord.Color.from_rgb(255, 247, 0)
                )
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/711570460487450687/721929129112502322/crown.png")
                embed.add_field(name=":thinking: What can Premium do? ",value="Customize your profile! 💎 \nGet the supporter role in my server 🎉 \n[[Cheer Chan Support server]](https://discord.gg/MVwkZt7) ↤ 🎀 \nUse external emojis from other server 🍕 \n\nAnd supporting us who work hard 😊 ",inline=False)

                embed.add_field(name="🎨 How can I buy Premium?",value="Type `c!premium` :white_heart:\nClick at `[Click here]` :white_heart:\nExecute payment :white_heart:\nType `c!premium @you verify [PAYID] [PayerID]` :white_heart:\nIf you have any questions or problems pls [contact](https://discord.gg/MVwkZt7) us :white_heart:\nP.S. If you are afraid you can buy premium on your private server :heart:",inline=False)
                
                embed.add_field(name="✨ Can I have Premium for free?",value="In the [Cheer Chan Support](https://discord.gg/MVwkZt7)server, there are Premium giveaways for free! :money_with_wings:",inline=False)
                
                await ctx.send(embed=embed)

   

def setup(bot):
    bot.add_cog(paypal(bot))



