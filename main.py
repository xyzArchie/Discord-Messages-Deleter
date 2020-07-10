import json
from discord.ext import commands
from os import system, path, _exit
from time import gmtime, strftime
from colors import green, red, white, reset
from discord.ext.commands import CommandNotFound

system('title [Discord Message Deleter]')
system('cls')
client = commands.Bot(command_prefix='!', self_bot=True)
deleted = 0

@client.event
async def on_connect():
    system('cls')
    print('> %sLogged in as%s: %s%s\n' % (green(), white(), client.user, reset()))

# Hide errors if an unknown command is executed
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@client.command()
async def purge(ctx, amount):
    global deleted

    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=int(amount)).filter(lambda m: m.author == client.user).map(lambda m: m):
        await message.delete()
        deleted += 1
        system('title [Discord Message Deleter] - Deleted Messages: %s' % (deleted))
        print('%s[%s%s%s] Deleted Message%s: %s%s' % (red(), white(), strftime('%H:%M:%S', gmtime()), red(), white(), message.content, reset()))

@client.command()
async def masspurge(ctx):
    global deleted

    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=500).filter(lambda m: m.author == client.user).map(lambda m: m):
        await message.delete()
        deleted += 1
        system('title [Discord Message Deleter] - Deleted Messages: %s' % (deleted))
        print('%s[%s%s%s] Deleted Message%s: %s%s' % (red(), white(), strftime('%H:%M:%S', gmtime()), red(), white(), message.content, reset()))

if path.exists('Token.json'):
    with open('Token.json', 'r', encoding='UTF-8', errors='replace') as f:
        try:
            config = json.load(f)
            token = config['token']
        except:
            with open('Token.json', 'w') as f:
                f.write('{\n    "token": "..."\n}')
            print('> %sReplace "..." with your Discord token inside Token.json — avoid including spaces or quotation marks%s.\n' % (red(), white()))
            system('pause >NUL')
            _exit(0)
    print('> Logging in . . .')
else:
    token = input('> Discord token: ')
    print()
    with open('Token.json', 'w') as f: f.write('{\n    "token": "%s"\n}' % (token))

try:
    client.run(token, bot=False)
except:
    system('cls')
    print('> %sIncorrect Discord token%s.' % (red(), white()))
    system('pause >NUL')
