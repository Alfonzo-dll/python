import discord
import time
from discord.ext import commands

client = discord.Client()
class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Log out command
    @commands.is_owner()
    @commands.command()
    async def logout(self, ctx):
        await ctx.send("Cya :wave:")
        exit(0)



def setup (client):
    client.add_cog(Owner(client))
