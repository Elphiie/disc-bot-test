import asyncio
import functools
import itertools
import math
import random
from re import search
from tracemalloc import stop
from click import command

import discord
from werkzeug import Client
from async_timeout import timeout
from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

class InActive(commands.Cog):
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx

        self.current = None
        self.next = asyncio.Event()

class Command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.msg_state = {}

    def getchannel(self, ctx: commands.Context):
        state = self.msg_state.get(ctx.guild.id)
        if not state:
            state = InActive(self.bot, ctx)
            self.msg_state[ctx.guild.id] = state
            
        return state

 

    @commands.command(name='hello')
    async def hello(self, ctx: commands.Context):
        async with ctx.typing():    
            await getchannel().send('Hello World! {}'.format(str()))


bot = commands.Bot('!', description='Testing',)
bot.add_cog(Command(bot))        


client = MyClient()
client.run('OTI3NDY5NDIwMzg3OTEzNzI4.YdKrNQ.c0GL07c_RCo0QlRSTfv3UiJzH60')