class Members():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(self, member : discord.Member):
        await self.bot.say('{0.name} joined in {0.joined_at}'.format(member))

def setup(bot):
    bot.add_cog(Members(bot))
