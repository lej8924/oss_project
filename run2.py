import asyncio, discord
from discord.ext import commands
from discord_buttons_plugin import *
from discord_components import *
import random
import readcsv


#bot = commands.Bot(command_prefix='!') # ?붙은 명령에만 반응
bot = ComponentsBot('?')
buttons = ButtonsClient(bot)

data = readcsv.readdata()


@bot.event
async def on_ready():
	print(f"We have loggedd in as {bot.user.name}")

# @bot.command()
# async def joined(ctx, member: discord.Member): #Says when a member joined.
#     await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def test(ctx):
    await ctx.send("test")

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def 추천(ctx):
    embed = discord.Embed(title = data[1][1], description ="", color = 0xFF0000, url = data[1][5])
    embed.add_field(name = data[0][1], value = data[1][1], inline = True)
    embed.add_field(name = data[0][2], value = data[1][2], inline = True)
    embed.add_field(name = data[0][4], value = data[1][4], inline = True)
    embed.set_footer(text = "", icon_url= data[1][5])
    await ctx.send(embed=embed)
 
##########select문############
async def selectboxTesting(ctx):
    await ctx.send(content="어떤 기준으로 맛집을 찾으시나요?",
                   components=[Select(placeholder="Select Something",
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
                    # custom_id="SelectTesting"
                    )])
    # interaction = await bot.wait_for('select_option',check=None)
    # await interaction.send(interaction.values[0])
    e1 = discord.Embed(title="?지역", description="이 키워드를 채팅에 적어보세요!!", color=0xffd032)
    e2 = discord.Embed(title="?음식 종류", description="이 키워드를 채팅에 적어보세요!!", color=0xffd032)
    e3 = discord.Embed(title="?도전", description="이 키워드를 채팅에 적어보세요!!", color=0xffd032)

    while True:
        try: # try except is not required but i would recommend using it
            event = await bot.wait_for("select_option", check=None)

            label = event.values[0]

            if label == "1":
                await event.send(
                    # type=InteractionType.ChannelMessageWithSource,
                    ephemeral=True, # we dont want to spam someone
                    embed=e1
                )

            elif label == "2":
                await event.send(
                    # type=InteractionType.ChannelMessageWithSource,
                    ephemeral=True, # we dont want to spam someone
                    embed=e2
                )
            elif label == "3":
                await event.send(
                    # type=InteractionType.ChannelMessageWithSource,
                    ephemeral=False, # we dont want to spam
                    embed=e3 
                )


        except discord.NotFound:
            print("error.")
            
@bot.command()
async def testing(ctx):
    await selectboxTesting(ctx)    

######select문 끝#########   

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
	
######버튼########


@buttons.click
async def region_hagye(ctx):
    hagye = []
    for one_data in data:
        if[one_data[12]=='A']:
            hagye.append(one_data)
    embed = discord.Embed(title=hagye[0][1], description = "", color = 0xb67ffd, url = hagye[0][5])
    embed.add_field(name = "Name", value = hagye[0][1], inline = True)
    embed.add_field(name = "Score", value = hagye[0][2], inline = True)
    embed.add_field(name = "Review", value = hagye[0][4], inline = True)
    await ctx.send("하계동 맛집을 찾아드리겠습니다")
    
@buttons.click
async def region_jungye(ctx):
    await ctx.send("중계동 맛집을 찾아드리겠습니다")
    
@buttons.click
async def region_sangye(ctx):
    await ctx.send("상계동 맛집을 찾아드리겠습니다")
    
@bot.command()
async def 버튼(ctx):
    embed = discord.Embed(title=f"안녕하세요~! {bot.user.name}, 어느 맛집을 추천해드릴까요?", color = 0x0073ff)
    await buttons.send(
        content = None,
        channel = ctx.channel.id,
        embed = embed,
        components = [
            ActionRow([
                Button(
                    label = "하계동",
                    style = ButtonType().Primary,
                    custom_id = "region_hagye"
                ),
           
                Button(
                    label = "중계동",
                    style = ButtonType().Danger,
                    custom_id = "region_jungye"
                ),
            
                Button(
                    label = "상계동",
                    style = ButtonType().Success,
                    custom_id = "region_sangye"
                )
            ]
            )
        ]
    )

####버튼 끝#####
     
bot.run('') #토큰
