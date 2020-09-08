import discord
from discord.ext import commands
import json
import random
#import asyncio

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(">>Logic is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['CHANNEL']))
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['CHANNEL']))
    await channel.send(f'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def pic(ctx):
   random_pic = random.choice(jdata['PICT'])
   pict = discord.File(random_pic)
   await ctx.send(file = pict)

@bot.command()
async def wu(ctx):
    await ctx.send('吳子傑你媽死了')

bot.run(jdata['TOKEN'])