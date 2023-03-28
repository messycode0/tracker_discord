import discord
from discord.ext import commands

from rich.console import Console


def start(token):
    intents = discord.Intents().all()
    intents.message_content = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    console = Console()

    # print the title saying tracker ascii art

    console.print('''

████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    ''')

    console.rule("[bold red]Rich console Initiated[/bold red]", style="bold red", align="left", width=50, characters=("-","")



    @bot.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(bot))
        print('Bot is ready')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello!')

        await bot.process_commands(message)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run(token)