import discord
import gspread
client = discord.Client()

TOKEN = 'OTMyNDU5MzM3MzEyNTMwNDYz.YeTSbg.wJlgpx-3-wf_cQ1HRdWNuDapvNI'

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

client.run(TOKEN)
