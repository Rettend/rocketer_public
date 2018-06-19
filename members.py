import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math, asyncpg
from time import gmtime
from discord.ext import commands

#-------------------DATA---------------------
version = "0.8.9"
owner = ["361534796830081024"]
bot = commands.Bot(command_prefix='r-', description=None)
bot.remove_command("help")
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
Imox = ["365173881952272384"]
permissions = discord.Permissions
underworking = ":warning: **Meh Boi, this command hasn't finished. Please wait until it's got.** :warning:"
"""timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""
#--------------------------------------------

class Members():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(self, member : discord.Member):
        await self.bot.say('**{0.name} joined in __{0.joined_at}__**'.format(member))
    
    @commands.command(pass_context=True)
    async def set_welcome(self, ctx, mesg1, mesg2):
        wchannel = ctx.message.channel
        emb = discord.Embed(title="DONE!", description=f":blue_book: Welcome-message set to this channel!\nWhen a member joins: **{mesg1}**\nWhen a member leaves: **{mesg2}**", colour=0x3498db)
        emb.set_thumbnail(url="https://discordapp.com/assets/c6b26ba81f44b0c43697852e1e1d1420.svg")
        await bot.say(embed=emb)

    @bot.event
    async def on_member_join(self, member):
        em = discord.Embed(title=f"{member.metion} joined!", description="mesg1", colour=0x3498db)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/391322023739129856.png?v=1")
        await bot.send_message(wchannel, embed=em)
        
    @bot.event
    async def on_member_remove(self, member):
        embed = discord.Embed(title=f"{member.metion} joined!", description="mesg2", colour=0x3498db)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/421004865049985035.png?v=1")
        await bot.send_message(wchannel, embed=embed)
    
def setup(bot):
    bot.add_cog(Members(bot))
