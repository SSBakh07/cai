from redbot.core import commands

class CAi(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        self.last_msg = "I saw nothing"

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @client.event
    async def on_message(message):
        if "thank you fazuran" in message.content.lower():
            channel = message.channel
            self.last_msg = message.content
            await channel.send("You're very welcome <3")
    
    @commands.command()
    async def lastthingyousaw(self, ctx):
        """?????"""
        await ctx.send(self.last_msg)