import discord
from discord.ext import commands

from rich.console import Console


def start(token):
    intents = discord.Intents().all()
    intents.message_content = True
    bot = commands.Bot(command_prefix='--', intents=intents)

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

    console.rule("[bold red]Rich console Initiated[/bold red]", style="bold red", align="left",)



    @bot.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(bot))
        print('Bot is ready')
        console.rule("[bold red]Discord Bot Initiated[/bold red]", style="bold red", align="left",)
        console.print('\nTracker is now ready for its mission\n', style="white", justify="center")

    @bot.event
    async def on_message(message):
        console.print(f'{message.author}\n    [b i ]{message.content}[b i]', style="white", justify="left")
        if message.author == bot.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello!')

        await bot.process_commands(message)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command used.')

    # user edits a message
    @bot.event
    async def on_message_edit(before, after):
        console.print(f'{before.author} edited a message\n    [b i gray]{before.content}[/b i gray]\n    [b i ]{after.content}[b i]', style="yellow", justify="left")
        # send message to log channel

    # user deletes a message
    @bot.event
    async def on_message_delete(message):
        console.print(f'{message.author} deleted a message\n    [b i ]{message.content}[b i]', style="red", justify="left")
        # send message to log channel

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    @bot.command()
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @bot.command()
    async def exit(ctx, reason="gave none, please try and give one next time"):
        await ctx.send('Exiting... for reason: ' + reason)
        await bot.close()
        return reason



    bot.run(token)