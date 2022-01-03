import discord
from discord.ext import commands
from os import getenv
import traceback
from server import keep_alive

prefix = getenv('discord_prefix')
intents=discord.Intents.all()

bot = commands.Bot(command_prefix=prefix,help_command=None,intents=intents)

@bot.event
async def on_ready():
    print("Botの名前")
    print(bot.user.name)  
    print("BotのID")
    print(bot.user.id)  
    print("Discord.pyのバージョン")
    print(discord.__version__)
    await bot.change_presence(activity=discord.Game(name=f"TEST"))#サーバー数を表示するには{len(bot.guilds)} ユーザー数を表示するなら{len(bot.users)}
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
keep_alive()
bot.run(getenv('discord_token'))
