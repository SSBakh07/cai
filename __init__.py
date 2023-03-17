from .cai import CAi


def setup(bot):
    bot.add_cog(CAi(bot))