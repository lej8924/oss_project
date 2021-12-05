import asyncio,discord
from discord.ext import commands

### 미완성 ###
bot = commands.Bot()

def reply():
    @bot.command()
    async def choose(ctx, *choices : str):
        await ctx.send("1","2","3")
        await ctx.send(f"{ctx}에서 맛집을 찾겟습니다.")
