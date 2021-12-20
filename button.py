import asyncio,discord
from discord_slash import ButtonStyle
from discord_slash.utils.manage_components import *
from discord.ext import commands
from discord_buttons_plugin import *
from discord_components import *
from discord_ui import *



bot = commands.Bot(command_prefix='!', description = "I'm Bot!!")

buttons = ButtonsClient(bot)

@bot.event
async def on_ready():
	print(f"We have loggedd in as {bot.user.name}")

@buttons.click
async def hagye(ctx):
    # hagye = []
    # for one_data in data:
    #     if[one_data[12]=='A']:
    #         hagye.append(one_data)
    # embed = discord.Embed(title=hagye[0][1], description = "", color = 0xb67ffd, url = hagye[0][5])
    # embed.add_field(name = "Name", value = hagye[0][1], inline = True)
    # embed.add_field(name = "Score", value = hagye[0][2], inline = True)
    # embed.add_field(name = "Review", value = hagye[0][4], inline = True)
    await ctx.reply("하계동 맛집을 찾아드리겠습니다")
    
@buttons.click
async def jungye(ctx):
    await ctx.reply("중계동 맛집을 찾아드리겠습니다")
    
@buttons.click
async def sangye(ctx):
    await ctx.reply("상계동 맛집을 찾아드리겠습니다")
    
@bot.command()
async def 지역(ctx):
    embed = discord.Embed(title=f"안녕하세요~! {bot.user.name}, 어느 지역의 맛집을 추천해드릴까요?", color = 0x0073ff)
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
#     e1 = discord.Embed(title="이것을 찾으셨나요", description="이 키워드를 채팅에 적어보세요!!", color=0xffd032)
    
#     while True:
#        try:
#            interaction = await bot.wait_for("button_click", check=None)
           
#            label = interaction.label
           
#            if label == "하계동":
#                   await interaction.send(embed=e1)
                  
#            elif label == "중계동":
#                   await interaction.send("중계입니다")
                  
#            elif label == "상계동":
#                   await interaction.send("상계입니다")
                  
#            elif label == "공릉동":
#                   await interaction.send("공릉입니다")
                  
#            elif label == "월계동":
#                   await interaction.send("월계입니다")
                    
#        except discord.NotFound:
#             print("error.")
              

@bot.command()
async def hi(ctx):
    await ctx.send("hi~")
    
# @buttons.click
# async def hagye(ctx):
#     await ctx.reply("하계동 맛집을 찾아드리겠습니다")
    
# @buttons.click
# async def jungye(ctx):
#     await ctx.reply("중계동 맛집을 찾아드리겠습니다")
    
# @buttons.click
# async def sangye(ctx):
#     await ctx.reply("상계동 맛집을 찾아드리겠습니다")
    
    
# @bot.command()
# async def button(ctx):
#     await buttons.send(
#         content = "Hello",
#         channel = ctx.channel.id,
#         components = [
#             ActionRow([
#                 Button(
#                     label = "하계동",
#                     style = discord.ButtonStyle.green,
#                     custom_id = "hagye"
#                 ),
           
#                 Button(
#                     label = "중계동",
#                     style = ButtonType().Danger,
#                     custom_id = "jungye",
#                 ),
            
#                 Button(
#                     label = "상계동",
#                     style = ButtonType().Success,
#                     custom_id = "sangye",
#                 )
#             ])
#         ]
#     )

# @bot.command()
# async def hi(cxt):
#     button1 = Button(label="Click me", style=discord.ButtonStyle().green, emoji="🤡")
#     button2 = Button(label="hihihihi")
#     button3 = Button(label="hello haha!")  
#     button4 = Button(label="okay bye~")
    
#     view = View()
#     view.add_item(button1)
#     view.add_item(button2)
#     view.add_item(button3)
#     view.add_item(button4)
    
#     await ctx.send("Hi!", view=view)
    
# @bot.command()
# async def choice(ctx):
#     buttons = [
#         create_button(
#             style=ButtonType().Primary,
#             label="hihi",
#             custom_id="one"
#         ),
#         create_button(
#             style=ButtonType().Primary,
#             label="hello",
#             custom_id="two"
#         )
#     ]
#     action_row = create_actionrow(*buttons)
#     fait_choice = await ctx.send("Fail to choice", components = [action_row])
    
bot.run('') #토큰