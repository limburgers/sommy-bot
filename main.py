import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all()) 

# BOT CHECK
@bot.event
async def on_ready():
    print("NOW ONLINE")
    time.sleep(5)

@bot.command(pass_content=True)

async def jail(ctx, member: discord.Member, nick):
    for x in range(50): # for loop (range goes from 0-9)
        await member.edit(nick=nick) 
        # await ctx.send(f'done')
        time.sleep(5)


@bot.command()
async def shutdown(ctx):
    await ctx.send("shutting down")
    await bot.close()



bot.run('TOKEN')