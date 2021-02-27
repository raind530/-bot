import discord
from discord.ext import commands
import json
import keep_alive
import os
intents = discord.Intents.all()

with open('正版.json', 'r', encoding='utf8') as botfild:
   data = json.load(botfild)

bot = commands.Bot(command_prefix='指令！', intents=intents)
client = discord.Client(intents=intents)

for filename in os.listdir('./指令'):
  if filename.endswith('.py'):
    bot.load_extension(f'指令.{filename[:-3]}')
    print(filename)

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(data['TOKEN'])
