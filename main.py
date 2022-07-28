from nextcord.ext import commands
import nextcord
import os
import pyfiglet
from dotenv import load_dotenv
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True

load_dotenv()

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    result = pyfiglet.figlet_format(f'{bot.user}')
    print(result)


@bot.command()
async def quoi(ctx):
    await ctx.send("Feur")

bot.run(os.getenv("BOT_TOKEN"))