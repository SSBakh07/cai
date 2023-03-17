from redbot.core import commands

class CAi(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        self.last_msg = "I saw nothing"
        self.event_count = 0
        self.triggers = {
            "thank you fazuran": ["You're very welcome <3", "Fuck Dyno :)"],
            "i love nya": ["Same u///w///u"],
            "i love zef": ["Same u///w///u"],
            "i am saqi": ["Oh hey simp"],
            "hello fazuran": ["Hello! <3"]
        }

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @commands.Cog.listener()
    async def on_message(self, message):
        self.last_msg = message.content
        trigger_keys = self.triggers.keys()
        msg_lower = message.content.lower()
        for trig in trigger_keys:
            if trig in msg_lower:
                await message.channel.send(self.triggers[trig])
    
    @commands.command()
    async def lastthingyousaw(self, ctx):
        """?????"""
        await ctx.send(self.last_msg)

    @commands.command()
    async def thankyou(self, ctx):
        """You *should* appreciate her."""
        await ctx.send("You're very welcome <3")