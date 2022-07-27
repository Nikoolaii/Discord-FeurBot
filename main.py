from nextcord.ext import commands
import nextcord
import os
import pyfiglet

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)


@bot.event
async def on_ready():
    result = pyfiglet.figlet_format(f'{bot.user}')
    print(result)


@bot.command()
async def quoi(ctx):
    await ctx.send("Feur")

bot.run("MTAwMTkwNzEyNDYzNDM5NDY1NA.Gj-DvI.EvtHBUyp_kFnui9FB3suCg7Hrtckcim2GyWaw8")
