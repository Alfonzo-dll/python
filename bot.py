import discord
import os
from discord.ext import commands

intents = discord.Intents().all()
client = commands.Bot(command_prefix = 'prefix giriniz', intents=intents, owner_id="")

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Activity (type=discord.ActivityType.listening, name="botun durumu istediğinizi girin"))
     print('Bot is online and connected to discord')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I dont have requirement permissions :angry:")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have requirement permissions :angry:")
    if isinstance(error, commands.NotOwner):
        await ctx.send("Only my owner can use this command :angry:")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("The command you entered was not found :angry:")

@commands.is_owner()
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@commands.is_owner()
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    
 
@commands.is_owner()
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("token")
