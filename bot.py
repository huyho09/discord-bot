import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import json


f = open("data.json", "r")
y = json.load(f)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
guild = discord.Guild

bot = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


def write_json(command):
    f = open("data.json", "r+")
    y = json.load(f)
    string_list = command.split("|")
    dict.update({string_list[0]: string_list[1]})
    y.update(dict)

    if os.path.exists("data.json"):
        os.remove("data.json")

    if "data.json":
        with open("data.json", "w") as f:
            json.dump(y, f)
    f.close()


@bot.command(name='learn')
async def guiding_bot(ctx, command):
    await ctx.send(command)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# print(str(list(y.keys())[0]))
# print(type(str(y.keys())))
# print(y.values())


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for i, j in y.items():
        if message.content.lower() == i.lower():
            await message.channel.send(j)
        elif message.content == 'raise-exception':
            raise discord.DiscordException

client.run(TOKEN)
