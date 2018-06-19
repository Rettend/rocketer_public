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
#---------------------------------------------

class Perms():
    def __init__(self, bot):
        self.bot = bot
        
    async def perm(perm : discord.Permissions):
        if perm is not True:
            raise NoPermError

def setup(bot):
    bot.add_cog(Perms(bot))
