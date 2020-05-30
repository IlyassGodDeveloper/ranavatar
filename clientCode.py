import random
import discord
from discord.ext import commands
from time import sleep

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('the bot is ready')


@client.command()
async def gif(ctx):
    for i in range(5):
        sleep(5)
        gifsC = client.get_channel(channel_ID)
        avatars = open("مكان وجود ملف روابط الصور")
        avatars = avatars.readlines()
        randomavatar  = discord.Embed(color = discord.Color.dark_blue())
        randomavatar.set_image(url=random.choice(avatars))
        randomavatar.set_footer(text="© ทστ__мσαiα∂.#1230")
        await gifsC.send(embed=randomavatar)
        

@client.command()
async def avatar(ctx):
    for i in range(5):
        sleep(5)
        avatarC = client.get_channel(channel_id)
        avatars = open("مكان وجود ملف روابط الصور")
        avatars = avatars.readlines()
        randomavatar  = discord.Embed(color = discord.Color.dark_blue())
        randomavatar.set_image(url=random.choice(avatars))
        randomavatar.set_footer(text="© ทστ__мσαiα∂.#1230")
        await avatarC.send(embed=randomavatar)


client.run("Your token here")
