import discord 
import random
import requests
import json
from discord.ext import commands

TOKEN = '000'

krdict_token = '0000'
client = commands.Bot(command_prefix = '&')


@client.event 
async def on_ready():
    print('we arrived {0.user}'.format(client))

mensagensrandom = ['파이팅!', '괜찮아요!', '힘내', '응원할게', '할 수 있어', '포기하지 마', '다 잘 될 거야', '걱정하지 마', '자랑스러워', '잘했어', '꿈을 이루길 바랄게']
frases = ['`멈추지 말고 계속 해나가기만 한다면 늦어도 상관없다` - *Confucius*', '`세상에서 보고싶은 변화가 있다면 당신 스스로 그 변화가 되어라` - *Mahatma Ghandi*', '`나무를 심는데 가장 좋았던 때는 20년 전이었다. 두 번째로 좋은 때는 지금이다` - *Chinese Proverb*', '`꿈을 꾸고 믿을 수 있다면 이룰 수도 있다` - *Napoleon Hill*']
ajuda = 'wellcome to sejong 폐하 bot!! i hope you enjoy using it💗\n❗commands are:❗\n ⏺ &h = help\n ⏺ &we = Words of Encouragement in Korean\n ⏺ &iq = Inspirational quotes in korean\n||this bot is under construction||'


@client.command()
async def w(ctx, *args):
    for arg in args:  
      await ctx.send(arg)  
@client.command() 
async def we(ctx):
    nmensardn = random.randint(0,len(mensagensrandom))
    embedVar = discord.Embed(title="Words of Encouragement in Korean", description = mensagensrandom[nmensardn] , color=0xAF7AD2)
    await ctx.channel.send(embed=embedVar)
@client.command() 
async def iq(ctx):
    nfrnd = random.randint(0,len(frases))
    embedVar = discord.Embed(title="Inspirational quotes in korean", description = frases[nfrnd] , color=0x6FA8DC)
    await ctx.channel.send(embed=embedVar)
@client.command()
async def h(ctx):
    embedVar = discord.Embed(title="HELP", description = ajuda , color=0xF2D37A)
    await ctx.channel.send(embed=embedVar)
@client.command()
async def marcel(ctx):
    await ctx.send('저는 marcel을 싫어해요')     

client.run(TOKEN)

