import os
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.audiorec import NativeVoiceClient
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents().all()

bot = commands.Bot(command_prefix= '$',intents = intents)








@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(pass_context = True)
async def join(ctx):
    if(ctx.voice_client):
        await ctx.send("Already in a channel")
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await channel.connect(cls=NativeVoiceClient)
        ctx.voice_client.record(lambda e: print(f"Exception: {e}"))
    else:
        await ctx.send("You must be in a voice channel for me to join!")



@tasks.loop(seconds = 1) # repeat after every 10 seconds
async def myLoop():
    
    print(ctx.voice_client.record())


@bot.command(pass_context = True)
async def leave(ctx):
    if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send('You have to be connected to the same voice channel to disconnect me.')

myLoop.start(pass_context = True)
bot.run(TOKEN)