import discord_patch  # Must be before discord import
import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot connecté en tant que {client.user}')
    channel = client.get_channel(1502015834674036856)
    if channel:
        await channel.send('Starting Container')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.reply(message.content)

client.run(os.environ['DISCORD_TOKEN'])
