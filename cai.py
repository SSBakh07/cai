from redbot.core import commands

class CAi(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @client.event
    async def on_message(message):
        if "thank you fazuran" in message.content.lower():
            channel = message.channel
            await channel.send("You're very welcome <3")