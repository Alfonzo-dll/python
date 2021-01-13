import discord
import time
from discord.ext import commands

client = discord.Client()
class User(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(client):
    client.add_cog(User(client))
