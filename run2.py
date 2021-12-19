import asyncio, discord
from discord.ext import commands
import random
import readcsv

bot = commands.Bot(command_prefix='$') # $붙은 명령에만 반응

data = readcsv.readdata()

@bot.event
async def on_ready():
	print("We have loggedd in as {0.user}".format(bot))

@bot.command()
async def test(ctx):
    await ctx.send("test")
    
#특정 문자로 시작하는 메세지를 받으면 실행
@bot.event
async def on_message(message):
    if message.content.startswith('골라 '):
        channel = message.channel
        message.content = message.content.replace("골라 ","")#추천을 공백으로 대치
        messagesplit = message.content.split(",")# 문자열을 , 기준으로 자르기
        msg = random.choice(messagesplit)+'을 골랐습니다'#random.choice(배열) =>배열 중 랜덤으로 뽑음
        await channel.send(msg)
        await bot.process_commands(msg1 = 'test')

# 사용자에게 정보입력 받아서 메뉴추천해주기 미완성
@bot.event
async def on_message(message):
    if message.content.startswith('추천'):
        embed = discord.Embed(title = data[1][1], description ="", color = 0xFF0000, url = data[1][5])
        embed.add_field(name = data[0][1], value = data[1][1], inline = True)
        embed.add_field(name = data[0][2], value = data[1][2], inline = True)
        embed.add_field(name = data[0][4], value = data[1][4], inline = True)
        embed.set_footer(text = "", icon_url= data[1][5])
        channel = message.channel
        await channel.send(embed=embed)
        await channel.send(data[1][5])

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")

bot.run('OTE1Mjk1NTE5MDEyNzE2NTQ1.YaZhYQ.V8GFp21Sk1Jex5uvqbfX630KEZc') #토큰