import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()


token = os.getenv('TOKEN')


intents = discord.Intents.all()
intents.messages = True
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='$', description="text", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


async def load_extensions():
    await bot.wait_until_ready()
    try:
        await bot.load_extension("cogs.mesaj")
    except Exception as e:
        print(f"Failed with load exception {e}")




@bot.event
async def on_connect():
    await load_extensions()

bot.run(token)