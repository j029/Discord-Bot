from os import environ
from tokenize import Token
import discord
from discord.ext import commands
from decouple import config
from colorama import Back, Fore, Style
import time

MY_TOKEN= config('MY_TOKEN')

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@client.event
async def on_ready():
    prfx = (Back.GREEN + Fore.WHITE + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(prfx + " Bot is up and running!")
    print("Logged in as " + Fore.BLUE + client.user.name)

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command(aliases=['close','stop'])
async def shutdown(ctx):
    await ctx.send(client.user.name + " logged out...")
    await client.close()

@client.command(aliases=['uinfo','whois'])
async def userinfo(ctx, member:discord.Member=None):
    if member == None:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(title="User info", description=f"Here's the info for {member.name}", color=discord.Color.green(), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Created At", value=member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p "))
    embed.add_field(name="Joined At", value=member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p "))

    await ctx.send(embed=embed)

client.run(MY_TOKEN)
