import asyncio, discord
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands
from discord_buttons_plugin import *
from discord_components import *
import readcsv
import pandas as pd

bot = commands.Bot(command_prefix='!', description = "I'm Bot!!")
bot = ComponentsBot('!')
buttons = ButtonsClient(bot)

data = pd.DataFrame(readcsv.readdata())

userdata = [False, False, False]

@bot.event
async def on_ready():
	print(f"We have loggedd in as {bot.user.name}")

##########select문############
@bot.command()
async def select(ctx):
    await selectboxTesting(ctx) 

async def selectboxTesting(ctx):
    await ctx.send(content="어떤 기준으로 맛집을 찾을까요?",
                   components=[
                    Select(
                    placeholder="기준을 선택해 주세요",
                    options = [
                        SelectOption(
                        label="지역",
                        value='1',
                        description = "난 지역을 기준으로 음식을 골라~!",
                        emoji="😄"),
                        SelectOption(
                        label="음식 종류",
                        value='2',
                        description = "난 음식종류를 기준으로 음식을 골라~!",
                        emoji="😄"),
                        SelectOption(
                        label="아님 새로운 음식 도전!!",
                        value='3',
                        description = "난 딴 거 필요없이 새로운 곳 갈래!",
                        emoji="😄")
                        ]
                    )
                ]
            )
    e1 = discord.Embed(title="!location", description="이 키워드를 채팅에 적어보세요!!", color=0xffd032)
    e2 = discord.Embed(title="!type", description="이 키워드를 채팅에 적어보세요!!", color=0xffd032)
    e3 = discord.Embed(title="!challenge", description="이 키워드를 채팅에 적어보세요!!", color=0xffd032)

    while True:
        event = await bot.wait_for("select_option", check=None)

        label = event.values[0]

        if label == "1": 
            await event.send(ephemeral=True,embed=e1)
        elif label == "2":
            await event.send(ephemeral=True,embed=e2)
        elif label == "3":
            await event.send(ephemeral=False,embed=e3 )
######select문 끝######

######지역 버튼######
@bot.command()
async def location(ctx):
    embed = discord.Embed(title="노원구의 어디서 맛집을 추천해드릴까요?", color = 0x0073ff)
    await ctx.send(
        embed = embed,
        content ="",
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
    userdata[0] = 'A'
    await ctx.reply("공릉동 맛집을 찾아드리겠습니다.")

@buttons.click
async def wol(ctx):
    userdata[0] = 'B'
    await ctx.reply("월계동 맛집을 찾아드리겠습니다.")

@buttons.click
async def sangye(ctx):
    userdata[0] = 'C'
    await ctx.reply("상계동 맛집을 찾아드리겠습니다")
    
@buttons.click
async def jungye(ctx):
    userdata[0] = 'D'
    await ctx.reply("중계동 맛집을 찾아드리겠습니다")
    
@buttons.click
async def hagye(ctx):
    userdata[0] = 'E'
    await ctx.reply("하계동 맛집을 찾아드리겠습니다.")
######지역버튼 끝######

######음식 버튼######
@bot.command()
async def type(ctx):
    embed = discord.Embed(title="어떤 종류의 음식을 추천해드릴까요?", color = 0x0073ff)
    await ctx.send(
        embed = embed,
        content ="",
        components=[
            Button(label="한식",
                   emoji="❤️",
                   custom_id="kor",),
            
            Button(label="중식",
                   emoji="❤️",
                   custom_id="chi"),
            
            Button(label="일식",
                   emoji="❤️",
                   custom_id="jap"),
            
            Button(label="양식",
                   emoji="❤️",
                   custom_id="west"),
            
            Button(label="카페",
                   emoji="❤️",
                   custom_id="cafe"),
                    ]
                )

@buttons.click
async def kor(ctx):
    userdata[1] = 0
    await ctx.reply("한식 맛집을 찾아드릴게요.")

@buttons.click
async def chi(ctx):
    userdata[1] = 1
    await ctx.reply("중식 맛집을 찾아드릴게요.")

@buttons.click
async def jap(ctx):
    userdata[1] = 2
    await ctx.reply("일식 맛집을 찾아드릴게요")
    
@buttons.click
async def west(ctx):
    userdata[1] = 3
    await ctx.reply("양식 맛집을 찾아드릴게요")
    
@buttons.click
async def cafe(ctx):
    userdata[1] = 4
    await ctx.reply("카페를 찾아드릴게요.")
######음식버튼 끝######

######도전 버튼######
@bot.command()
async def challenge(ctx):
    embed = discord.Embed(title="새로운 맛집을 추천해드릴까요?", color = 0x0073ff)
    await ctx.send(
        embed = embed,
        content ="",
        components=[
            Button(label="도전!",
                   emoji="❤️",
                   custom_id="ch",),
            
            Button(label="안도전!",
                   emoji="❤️",
                   custom_id="nch"),
                   ]
                )

@buttons.click
async def ch(ctx):
    userdata[2] = 0
    await ctx.reply("새로운 곳을 찾아드릴게요.")

@buttons.click
async def nch(ctx):
    userdata[2] = 1
    await ctx.reply("맛집을 찾아드릴게요.")

######도전버튼 끝######

@bot.command()
async def fin(ctx):
    i=0
    print(userdata)
    if (userdata[0]!= None) and (userdata[1] == None):
        temp = data.loc[(data['Dong']== userdata[0]) & (data['Challenge']== userdata[2])]
        print(temp)
        embed1 = Embed(title = temp['Name'][i],description = "",url = temp['Link'][i],color = 0xFF0000)
        embed1.add_field(name = '별점',value=temp['Score'][i])
        embed1.add_field(name = '별점수',value=temp['Numberofscore'][i])
        embed1.add_field(name = '블로그리뷰수',value=temp['Review'][i])
        await ctx.send(embed = embed1)

    elif (userdata[0] == None) and (userdata != None):
        temp = data.loc[(data['Typenum']==userdata[1]) & (data['Challenge']== userdata[2])]
        print(temp)
        embed2 = Embed(title = temp['Name'][i],description = "",url = temp['Link'][i],color = 0xFF0000)
        embed2.add_field(name = '별점',value=temp['Score'][i])
        embed2.add_field(name = '별점수',value=temp['Numberofscore'][i])
        embed2.add_field(name = '블로그리뷰수',value=temp['Review'][i])
        await ctx.send(embed = embed2)

    else:
        temp = data.loc[(data['Dong']== userdata[0]) & (data['Typenum']==userdata[1]) & (data['Challenge']== userdata[2])]
        print(temp)
        embed3 = Embed(title = temp['Name'][i],description = "",url = temp['Link'][i],color = 0xFF0000)
        embed3.add_field(name = '별점',value=temp['Score'][i])
        embed3.add_field(name = '별점수',value=temp['Numberofscore'][i])
        embed3.add_field(name = '블로그리뷰수',value=temp['Review'][i])
        await ctx.send(embed = embed3)




bot.run('') #토큰
