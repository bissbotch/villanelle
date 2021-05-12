import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv
import os
import json

load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

bot = commands.Bot(command_prefix=PREFIX)
slash = SlashCommand(bot)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.CustomActivity(name =f"slaying it"))

@slash.slash(name="hello")
async def hello(ctx:SlashContext):
    await ctx.hannel.send("Hello!")

bot.run(TOKEN)