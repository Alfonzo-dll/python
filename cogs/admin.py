import discord
import time
import typing
from discord.ext import commands

client = discord.Client()
class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Ban command
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided."):
        if ctx.message.author.id == member.id:
            await ctx.send("You cannot ban yourself :angry:")
            return
        await member.ban(reason=reason)
        ban = discord.Embed(title=f':boom: Banned {member.name}!', description=f'Reason: {reason}\nBy: {ctx.author.mention}', color=0x992d22)
        ban.set_footer(text=f'Command used by: {ctx.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)

    # Kick command
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided."):
        if ctx.message.author.id == member.id:
            await ctx.send("You cannot kick yourself :angry:")
            return
        await member.kick(reason=reason)
        kick = discord.Embed(title=f':boom: Kicked {member.name}!', description=f'Reason: {reason}\nBy: {ctx.author.mention}', color=0x992d22)
        kick.set_footer(text=f'Command used by: {ctx.author.name}', icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)

    # Clear command
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount: int):
        limitsayi = 100

        if amount < 1:
            await ctx.send('Enter a high number than 1')
            return

        if amount > limitsayi:
            await ctx.send(f'Your value cannot be more than {limitsayi}')
            return

        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleaned {amount} messages.")






def setup(client):
    client.add_cog(Admin(client))
