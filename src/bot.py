import discord
from discord.ext import commands
import dotenv
import os

TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

bot = discord.Client()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.CustomActivity(name =f"slaying it"))

bot.run(TOKEN)