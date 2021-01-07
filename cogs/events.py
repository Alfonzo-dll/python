import discord
import time
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
         print('Bot is online and connected to discord')

def setup(client):
    client.add_cog(Events(client))
