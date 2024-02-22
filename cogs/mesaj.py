import discord
from discord.ext import commands
from datetime import datetime, date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

formatted_date = datetime.now().strftime("%d-%B-%Y")

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        Viorel = 180328125765386240 
        Birgovan = 339854159761244161
        if ctx.author.id == Viorel:
            await ctx.send("Sugi pula Viorel")
        elif ctx.author.id == Birgovan:
            await ctx.send("Sa-mi iei coaiele pe piept Birgovan!")
        else:
            await ctx.send("Hello!")

    @commands.command()
    async def ceas(self, ctx):
        await ctx.send(current_time)

    @commands.command()
    async def data(self, ctx):
        await ctx.send(formatted_date)


async def setup(bot):
    await bot.add_cog(BotCommands(bot))