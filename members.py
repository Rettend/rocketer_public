import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math
from discord.ext import commands

#-------------------DATA---------------------
version = "0.8.9"
owner = ["361534796830081024"]
startup_extensions = ["members", "rng"]
bot = commands.Bot(command_prefix='r--', description=None)
bot.remove_command("help")
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
Imox = ["365173881952272384"]
permissions = discord.Permissions
underworking = ":warning: **Meh Boi, this command hasn't finished. Please wait until it's got.** :warning:"

class Members():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(self, member : discord.Member):
        await self.bot.say('**{0.name} joined in __{0.joined_at}__**'.format(member))
    
    @commands.command(pass_context=True)
    async def set_welcome(ctx, channel,  mesg):
	    wchannel = discord.utils.get(ctx.message.server.channels, name=channel)
	    await bot.say(f":white_check_mark: Welcome-message set to **{mesg}**\nThe channel is {wchannel.mention}")

    @commands.listen()
    async def on_member_join(member):
        await bot.send_message(wchannel, embed=em)
        
    @commands.listen()
    async def on_member_remove(member):
        await bot.send_message(wchannel, f"**{member} left without saying anything...** <:thonkSad:421004865049985035>")

def setup(bot):
    bot.add_cog(Members(bot))
