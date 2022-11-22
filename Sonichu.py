import os
import random
import discord
import requests
import json
import youtube_dl
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord import client

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)





load_dotenv()
TOKEN = os.getenv('OTA1NTIxNzk0ODY0Mjc1NDg2.Gp0kuo.3hC_GsuZ2qECSiUTy4AsmafO0TekmWVuyklUs0')

bot = commands.Bot(command_prefix='.')

@bot.command(name='Early')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "IF YOU DO NOT COME CLEAN RIGHT NOW I AM GOING TO GET MY FATHER IN ON THIS FURTHER AND YOU ARE GOING TO GET FUCKIN' ARRESTED THROWN IN JAIL AND YOU WILL NOT GET TO LIVE THE PEACEFUL HAPPY LIFE WITH CASEY THAT I WOULD LIKE YOU TO LIVE BECAUSE CASEY REALLY CARES FOR YOU MAN!",

    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
@bot.command(name='hat')
async def hat(ctx):
    hat_names = ['Booty Hunter',
    'Lifeguard On Booty',
    'Groom',
    'Free Hat Limit 1',
    'Nice Legs, What Time They Open?',
    'Tell Your Titties To Stop Staring At My Eyes!',    
    "I'm Did Asbestos I Can",
    "Too Funk To Druck",
    "I ♡ Cock Fighting",
    "Hold My Hat While I Have Sex With Your Wife",
    "Rock Out With Your Jock Out Daytona Beach 1986",
    "No Habla Jibber Jabber",
    "Breath If You're Horny",
    "Divorce Is Strong With This One",
     "The Big E",

    ]
    response = random.choice(hat_names)
    await ctx.send(response)

@bot.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('ChrisChan.wav')
        player = voice.play(source)
    else:
        await ctx.send("Boy, get your ass in a voice channel before I whup that ass!")

@bot.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I done did left that bitch you feel me?")
    else:
        await ctx.send("I aint in a voice channel if your dumbass aint in there boy.")       






    

bot.run('')























































































