import asyncio,discord
from discord import embeds
from discord.embeds import Embed
#from discord_slash import ButtonStyle
#from discord_slash.utils.manage_components import *
from discord.ext import commands
from discord_buttons_plugin import *
from discord_components import *
#from discord_ui import *
import readcsv

data = readcsv.readdata()

bot = commands.Bot(command_prefix='!', description = "I'm Bot!!")

buttons = ButtonsClient(bot)

@bot.event
async def on_ready():
	print(f"We have loggedd in as {bot.user.name}")

@bot.command()
async def 지역(ctx):
    embed = discord.Embed(title="안녕하세요~!, 어느 지역의 맛집을 추천해드릴까요?", color = 0x0073ff)
    await ctx.send(
        embed = embed,
        content ="Discord Button!please",
        components=[
            Button(label="하계동",
                   emoji="❤️",
                   custom_id="hagye",),
            
            Button(label="중계동",
                   emoji="❤️",
                   custom_id="jungye"),
            
            Button(label="상계동",
                   emoji="❤️",
                   custom_id="sangye"),
            
            Button(label="공릉동",
                   emoji="❤️",
                   custom_id="gong"),
            
            Button(label="월계동",
                   emoji="❤️",
                   custom_id="wol")
        ]
    )

@buttons.click
async def gong(ctx):
    await ctx.reply("공릉동 맛집을 찾아드리겠습니다.")

@buttons.click
async def wol(ctx):
    location = 'B'
    await ctx.reply("월계동 맛집을 찾아드리겠습니다.")

@buttons.click
async def sangye(ctx):
    location = 'C'
    await ctx.reply("상계동 맛집을 찾아드리겠습니다")
    
@buttons.click
async def jungye(ctx):
    location = 'D'
    await ctx.reply("중계동 맛집을 찾아드리겠습니다")
    
@buttons.click
async def hagye(ctx):
    location = 'E'
    await ctx.reply("하계동 맛집을 찾아드리겠습니다.")

bot.run('') #토큰





######################################


'''e1 = discord.Embed(title="이것을 찾으셨나요", description="이 키워드를 채팅에 적어보세요!!", color=0xffd032)
    
    while True:
       try:
           interaction = await bot.wait_for("button_click", check=None)
           
           label = interaction.component.label
           
           if label == "하계동":
                  await interaction.send(embed=e1)
                  
           elif label == "중계동":
                  await interaction.send("중계입니다")
                  
           elif label == "상계동":
                  await interaction.send("상계입니다")
                  
           elif label == "공릉동":
                  await interaction.send("공릉입니다")
                  
           elif label == "월계동":
                  await interaction.send("월계입니다")
                    
       except discord.NotFound:
            print("error.")'''