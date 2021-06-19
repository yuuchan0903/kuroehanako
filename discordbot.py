from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['ODE2NzA4MTM1OTIxMTIzMzk5.YD-4uQ.yEM7IVxIxsOzI9ZQNPcXN1qf_gE']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
© 2021 GitHub, Inc.
