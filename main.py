from nextcord.ext import commands
import nextcord
import os
import pyfiglet
from dotenv import load_dotenv

intents = nextcord.Intents.default()
intents.message_content = True

load_dotenv()

bot = commands.Bot(command_prefix='', intents=intents)


@bot.event
async def on_ready():
    result = pyfiglet.figlet_format(f'{bot.user}')
    print(result)


@bot.event
async def on_message(message):
    if "quoi" in message.content:
        channel = message.channel
        await channel.send("Feur")


bot.run(os.getenv("BOT_TOKEN"))
