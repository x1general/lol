import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')
client.remove_command('help')
admins = [764991778767110145]

Dis = client.get_guild(764991778767110145)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="💛"))
    print('Bot is Ready')

@client.command(aliases=['Help', 'Commands', 'Info', 'HELP'])
async def help(ctx):
    embed=discord.Embed(title="Among Us Assistant", description="Command List", color=0x07d5b9)
    embed.set_author(name="Invite Link", url="https://InviteLink.com/", icon_url="https://cdn.discordapp.com/attachments/724941836002787393/761895104309886986/shhhhhhh.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724941836002787393/761895104309886986/shhhhhhh.jpg")
    embed.add_field(name="Prefix = $", value="Bot Prefix is $, use $ before any command", inline=False)
    embed.add_field(name="$Help", value="Shows the Command List", inline=False)
    embed.add_field(name="$join", value="Joins the channel (REQUIRED to use other Commands)", inline=False)
    embed.add_field(name="$muteall", value="Server Mute All Users in the voice Channel", inline=False)
    embed.add_field(name="$unmuteall", value="Server UnMute All Users in the voice Channel", inline=False)
    embed.add_field(name="$code [MATCHCODE]", value="Send Match code to all users in the voice channel, Example : $code RNSDKW", inline=False)
    embed.add_field(name="$dc", value="Disconnect from the voice channel.", inline=False)
    embed.set_footer(text="Coded With 💖")
    await ctx.send(embed=embed)
    print('Help Embed Sent')

@client.command(aliases=['Join', 'JOIN', 'come', 'Come'])
async def join(ctx):
    if ctx.message.author.id in admins:
        channel = ctx.author.voice.channel
        await channel.connect()
        print('[BoT] Connected to Voice!')
    else:
        await ctx.send('You Are not an Admin...')
        pass

@client.command(aliases=['Muteall', 'MUTEALL', 'ma', 'Ma'])
async def muteall(ctx):
    if ctx.message.author.id in admins:
        channel = ctx.author.voice.channel
        for member in channel.members:
            await member.edit(mute=True)
        print('[BoT] Muted All')
    else:
        await ctx.send('You Are not an Admin...')
        pass

@client.command(aliases=['Unmuteall', 'UNMUTEALL', 'ua', 'Ua'])
async def unmuteall(ctx):
    if ctx.message.author.id in admins:
        channel = ctx.author.voice.channel
        for member in channel.members:
            await member.edit(mute=False)
        print('[BoT] UnMuted All')
    else:
        await ctx.send('You Are not an Admin...')
        pass

@client.command(aliases=['Dc', 'DC'])
async def dc(ctx):
    if ctx.message.author.id in admins:
        await ctx.voice_client.disconnect()
        print('[BoT] Disconnected From Voice!')
    else:
        await ctx.send('You Are not an Admin...')
        pass


@client.command(aliases=['dm', 'sendall', 'all'])
async def code(ctx, *, code):
    if ctx.message.author.id in admins:
        channel = ctx.author.voice.channel
        for user in channel.members:
            await user.send(code)
    else:
        await ctx.send('You Are not an Admin...')
        pass


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='MmdSlr', url='http://www.twitch.tv/mmdslr?sr=a You cant do YT only Twitch.'))
    print("status avaz shod gozo")




client.run('Nzc5MDYzMDUxNjQyMDc3MTk1.X7bFAQ.GbQ5aogyO8yFEIS25dB-kOEErX0')