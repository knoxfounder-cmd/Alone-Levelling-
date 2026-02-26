import discord
from discord.ext import commands

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')