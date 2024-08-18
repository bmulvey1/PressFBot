#!/usr/bin/env python3

import discord
import conf
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
async def on_message(message):
    number = random.randint(0, 999)
    if message.content.find('F') != -1:

        if str(message.author) == "DJ Mitch#4397" or str(message.author) == "PressFBot#3434":
            pass
        else:

            await message.channel.send('Press F to pay respects')
    elif number == 0:
        await message.channel.send('Press F to pay respects')


client.run(conf.key)
