import asyncio, discord
from discord.ext import commands
import random
import readcsv

bot = commands.Bot(command_prefix='?') # $붙은 명령에만 반응

data = readcsv.readdata()

@bot.event
async def on_ready():
	print("We have loggedd in as {0.user}".format(bot))

@bot.command()
async def joined(ctx, member: discord.Member): #Says when a member joined.
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

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

@bot.command()
async def menu(ctx):
    embed = discord.Embed(title = "제목", description = None, color = 0xFF0000)
    embed.add_field(name = "필드이름", value = None, inline = False)
    embed.set_footer(text = "footer")
    await ctx.send(embed=embed)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
	
######버튼########
@bot.command()
async def 버튼(ctx):
    await buttons.send(
        content = "어느 지역의 맛집이 궁금하시나요~?",
        channel = ctx.channel.id,
        components = [
            ActionRow(
                Button(
                    label = "하계동",
                    style = ButtonType().Primary,
                    custom_id = "region_hagye"
                ),
           
                Button(
                    label = "중계동",
                    style = ButtonType().Primary,
                    custom_id = "region_jungye"
                ),
            
                Button(
                    label = "상계동",
                    style = ButtonType().Primary,
                    custom_id = "region_sangye"
                )
            )
        ]
    )

@buttons.click
async def region_hagye(ctx):
    await ctx.reply("하계동 맛집을 찾아드리겠습니다")

bot.run('') #토큰
