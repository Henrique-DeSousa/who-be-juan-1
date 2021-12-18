import discord
from discord.ext import commands

import music
import config

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="who be juan ", intents=intents)

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    channel = discord.utils.get(client.get_all_channels(), name="general")
    await client.get_channel(channel.id).send("Ahhh shit here we go again...")


@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        message = f"Olha quem é ele!!!\nParece que o {member.mention} decidiu aparecer."
        await guild.system_channel.send(message)

client.run(config.token)