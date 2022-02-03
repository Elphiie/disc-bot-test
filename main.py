

from collections import UserList
import time
from async_timeout import timeout
import discord
import asyncio
import math
from discord.ext import commands




client = discord.Client()



@client.event
async def on_message(message):

    if message.author != client.user:
        print('Message from {}'.format(message.author.name) + ': {}'.format(message.content))



class Bank():


    async def banking(ctx):
        member_lst = []
        for guild in bot.guilds:
            for member in guild.members:
                member_lst.append(str(member))
            return member_lst
        return member_lst    
    
    

    async def select_user(ctx):
        member_lst = []
        for guild in bot.guilds:
            for member in guild.members:
                member_lst.append(str(member))
            return member_lst



        


        
class Commandings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.msg_state = {}
        self.bank = Bank()


    @commands.command(name = 'hello')
    async def __hello(self, ctx: commands.Context):

        async with ctx.typing():
                await ctx.send('Hello {}'.format(ctx.author.name))
                return

    @commands.command(name = "users")
    async def __user_list(self, ctx: commands.Context):
        
        members = await self.bank.user_list()

        async with ctx.typing():
            await asyncio.sleep(0.5)
            await ctx.send(members)
            return

    @commands.command(name = 'select')
    async def __select(self, ctx: commands.Context):

        member_lst = await self.bank.select_user()

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in member_lst

        input = await client.wait_for('message', check=check, timeout=20)
            async with ctx.typing():
                await ctx.send('yay')
        


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot('!', description='Testing', intents=intents)
        
bot.add_cog(Commandings(bot))

@bot.event
async def on_ready():
    print('Logged on as {0.user.name}!'.format(bot))


bot.run('OTI3NDY5NDIwMzg3OTEzNzI4.YdKrNQ.c0GL07c_RCo0QlRSTfv3UiJzH60')