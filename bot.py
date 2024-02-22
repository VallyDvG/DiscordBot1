import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()
Viorel = 180328125765386240 
Birgovan = 339854159761244161
Vali = 289715372813320193

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
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.content.startswith("$"):
        if message.author.id == Vali or message.author.id == Viorel:
            await message.reply(f"Hello, {message.author.mention}! You said: {message.content}")
        elif message.author.id ==Birgovan:
            await message.reply("Nu ai voie!")
    await bot.process_commands(message)

@bot.event
async def on_connect():
    await load_extensions()

bot.run(token)