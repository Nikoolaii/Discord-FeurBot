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
    await bot.change_presence(status=nextcord.Status.idle, activity = nextcord.Activity(type=nextcord.ActivityType.watching, name=f"quoi sur {len(bot.guilds)} serveurs"))


@bot.event
async def on_message(message):
    if "quoi" in message.content:
        channel = message.channel
        await channel.send("Feur")


@bot.event
async def on_guild_remove():
    await bot.change_presence(status=nextcord.Status.idle, activity = nextcord.Activity(type=nextcord.ActivityType.watching, name=f"quoi sur {len(bot.guilds)} serveurs"))


@bot.event
async def on_guild_join():
    await bot.change_presence(status=nextcord.Status.idle, activity = nextcord.Activity(type=nextcord.ActivityType.watching, name=f"quoi sur {len(bot.guilds)} serveurs"))


bot.run(os.getenv("BOT_TOKEN"))
