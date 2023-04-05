import discord
from discord.ext import commands
import asyncio
from datetime import datetime, time, timedelta

##
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

##
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    channel = discord.utils.get(client.get_all_channels(), name='test')
    while True:
        await asyncio.sleep(60)
        await channel.send('AKTYWNY JESTEM :green_circle:')

##

@client.event
async def on_member_join(member):
    channel = discord.utils.get(client.get_all_channels(), name='test')
    await channel.send(f"Witaj {member.mention} luju na serwerze! :fire:")

##

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Adept")
    await member.add_roles(role)
    await asyncio.sleep(30) # 30 dni w sekundach
    await member.remove_roles(role)

##


bot = commands.Bot(command_prefix='!', intents=intents)




##
client.run('MTA5Mjk2MTY2NDEzMjk3NjY2MA.G38oQ4.EuoMMLU61Zwq_BJGEzkLN-aeOUNHqVdHzEjIFc')