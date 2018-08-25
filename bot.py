import discord
import conf
import random


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
async def on_message(message):
    number = random.randint(0,999)
    if message.content.find('F') != -1:

        if str(message.author) == "DJ Mitch#4397" or str(message.author) == "PressFBot#3434":
            pass
        else:

            await client.send_message(message.channel, 'Press F to pay respects')
    elif number == 0:
        await client.send_message(message.channel, 'Press F to pay respects')


client.run(conf.key)
