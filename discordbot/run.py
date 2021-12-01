import asyncio, discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$") # $붙은 명령에만 반응

@bot.event
async def on_ready():
	print("We have loggedd in as {0.user}".format(bot))

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
        
bot.run('token값 입력') #토큰
