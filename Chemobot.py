 # Chemobot.py
import os
import random
import discord
import asyncio
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
sallaniyor = False
playing = False

CHANNEL_LOL_GENEL = 730109719087284311 
CHANNEL_GENERAL = 705195568389161003
CHANNEL_VOICE_CH1 = 714920405910945832


print("Attempting to connect to Discord...")
client = commands.Bot(command_prefix = '$')

@client.command(name='selam', help ='Selamlar')
async def greet(ctx):
    print(ctx.message.content)
    response = "MERHABALAR AQ"
    await ctx.send(response)
    
@client.command(name='ahegao', help = 'ascii ahegao')
async def ahegao(ctx):
    print(ctx.message.content)
    ahegao = """⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠"""
    await ctx.send(ahegao)


@client.command(name='kura',help="""Default: CH1 kanalındaki oyuncuları kullanarak iki takım oluşturur.\n
2. Parametre olarak verilen oyuncuları ignorelayabilir veya oyuncu ekleyebilir.\n
Örnek: $kura add visne feseka
Örnek 2: $kura ignore @mention @mention2""")
async def kura(ctx,*argv):
    ch = client.get_channel(CHANNEL_VOICE_CH1)
    members = ch.members
    players = []
    for member in members:
        players.append(member.name)
    if len(argv) != 0:
        if (argv[0] == 'ignore'):
            for arg in argv[1:]:
                players.remove(arg)
        if (argv[0] == 'add'):
            for arg in argv[1:]:
                players.append(arg)
    random.shuffle(players)
    takim1 = players[:5]
    takim2 = players[5:]
    print('takımlar done')
    response = ''
    response += 'Takim 1:\n'
    for player in takim1:
        response = response + str(player) + '\n'
    response += '\n\nTakim 2:\n'
    for player in takim2:
        response = response + str(player) + '\n'
    await ctx.send(response)

@client.command(name='yazitura',help='Yazı tura. Alican ok nightmare')
async def yazitura(ctx):
    coin = random.randint(0,1)
    if coin == 0:
        await ctx.send('Yazı')
    else:
        await ctx.send('Tura')
    

@client.command(name='spam',help="""Bir kullanıcıya özelden mesajı spamler.\n
Boş bırakılırsa Dc\'ye çağırılıyorsun mesajını spamler\n
Örnek : $spam @feseka 5 sa as\n
Örnek2 :$spam @feseka 7 """)
async def spam(ctx, user: discord.User, n: int, *,message=None):
    if n > 10:
        await ctx.send('Abartma sen de')
    print(ctx.message.content)
    message = message or "DC ye çağırılıyorsun"
    message = ctx.author.name + ': ' + message
    for i in range(n):
        await user.send(message)
    await ctx.message.delete()
    
@client.event
async def on_voice_state_update(member,before,after):
    channel = client.get_channel(CHANNEL_LOL_GENEL)
    if before.channel == None and after.channel != None:
        await channel.send(f'{member.name} hg')


@client.event
async def on_ready():
    print(
            f'{client.user.name} has connected to Discord!'
        )
    channel = client.get_channel(CHANNEL_LOL_GENEL)
    response = "Alandayıs"
    await channel.send(response)


client.run(TOKEN)
