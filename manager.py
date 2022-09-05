import token
import discord
import asyncio
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/',intents=intents) 
token = ('MTAxNjI0NDI0OTY1OTk3MzgwMg.GzwoLg.mj23a7HK284PMSgxvRf3U0fsft4RIs8oL_wpGo')
@bot.event
async def on_ready(ctx):    
    print ("bot run shod")

@bot.command()
async def massage_to_almas(ctx):
    await ctx.send ("almasmafor account |Almasmafor#5949")

bot.run ('MTAxNjI0NDI0OTY1OTk3MzgwMg.GzwoLg.mj23a7HK284PMSgxvRf3U0fsft4RIs8oL_wpGo')