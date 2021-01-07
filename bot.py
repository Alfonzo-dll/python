import discord
import os
from discord.ext import commands

intents = discord.Intents().all()
client = commands.Bot(command_prefix = '?', intents=intents)

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Bot with Python"))
     print('Bot is online and connected to discord')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("Nzk2Njk2MTQzMzA3NjAzOTg5.X_brGg.GAMBhWn_0jyS1fUi0BcsVReuA6w")
