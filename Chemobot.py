# Chemobot.py
import os
import random
import youtube_dl
import discord
import asyncio
from discord.ext import commands

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_LOL_GENEL = 714920349107486911
CHANNEL_GENERAL = 705195568389161003
CHANNEL_VOICE_CH1 = 714920405910945832

print("Attempting to connect to Discord...")
client = commands.Bot(command_prefix='$')


@client.command(name='ping', help='test bot')
async def ping(ctx):
    await ctx.send('pong')


@client.command(name='selam', help='Selamlar')
async def greet(ctx):
    print(ctx.message.content)
    response = "MERHABALAR AQ"
    await ctx.send(response)


@client.command(name='ahegao', help='ascii ahegao')
async def ahegao(ctx):
    print(ctx.message.content)
    ahegaoascii = """⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
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
    await ctx.send(ahegaoascii)



@client.command(name='mertnox', help="""Babaaaa""", pass_context=True)
async def mertnox(ctx):
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }
    data = ytdl.extract_info('https://www.youtube.com/watch?v=_zLzSlmZm4c', download=True)
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(ytdl.prepare_filename(data),**FFMPEG_OPTIONS),volume=1.0),
            after=lambda e: print('mertnox done', e))
    await asyncio.sleep(30)
    await vc.disconnect()


@client.command(name='kura', help="""Default: CH1 kanalındaki oyuncuları kullanarak iki takım oluşturur.\n
2. Parametre olarak verilen oyuncuları ignorelayabilir veya oyuncu ekleyebilir.\n
Örnek: $kura add visne feseka
Örnek 2: $kura ignore @mention @mention2""")
async def kura(ctx, *argv):
    ch = client.get_channel(CHANNEL_VOICE_CH1)
    members = ch.members
    players = []
    for member in members:
        players.append(member.nick or member.name)
    if len(argv) != 0:
        if argv[0] == 'ignore':
            for arg in argv[1:]:
                players.remove(arg)
        if argv[0] == 'add':
            for arg in argv[1:]:
                players.append(arg)
    random.shuffle(players)
    takim1 = players[:len(players) // 2]
    takim2 = players[len(players) // 2:]
    print('takımlar done')
    response = ''
    response += 'Takim 1:\n'
    for player in takim1:
        response = response + str(player) + '\n'
    response += '\n\nTakim 2:\n'
    for player in takim2:
        response = response + str(player) + '\n'
    await ctx.send(response)


@client.command(name='yazitura', help='Yazı tura. Alican ok nightmare')
async def yazitura(ctx):
    coin = random.randint(0, 1)
    if coin == 0:
        await ctx.send('Yazı')
    else:
        await ctx.send('Tura')


@client.command(name='sevket', help='Chate ağır yara atar')
async def sevket(ctx):
    await ctx.send("https://imgur.com/a/BRcAmWk")


@client.command(name='spam', help="""Bir kullanıcıya özelden mesajı spamler.\n
Boş bırakılırsa Dc\'ye çağırılıyorsun mesajını spamler\n
Örnek : $spam @feseka 5 sa as\n
Örnek2 :$spam @feseka 7 """)
async def spam(ctx, user: discord.User, n: int, *, message=None):
    if n > 10:
        await ctx.send('Abartma sen de')
    print(ctx.message.content)
    message = message or "DC ye çağırılıyorsun"
    message = ctx.author.name + ': ' + message
    for i in range(n):
        await user.send(message)
    await ctx.message.delete()


client.run(TOKEN)
