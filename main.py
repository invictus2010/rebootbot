from dotenv import load_dotenv
import discord
from twilio.rest import Client
from discord.ext import commands
import os
import requests

load_dotenv()

digitalocean_token = os.environ.get("digitalocean_token")
discord_token = os.environ.get("discord_token")
twilio_token = os.environ.get("twilio_token")
twilio_account = os.environ.get("twilio_account")
phone_number = os.environ.get("phone_number")
digitalocean_droplet_id = os.environ.get("digitalocean_droplet_id")

client = discord.Client()
twilio_client = Client(twilio_account, twilio_token)


def reboot_digitalocean():
    data = {"type": "reboot"}
    endpoint = f'https://api.digitalocean.com/v2/droplets/{digitalocean_droplet_id}/actions'
    headers = {"Authorization": f"Bearer {digitalocean_token}"}
    response = requests.post(endpoint, data=data, headers=headers)
    if (response.status_code == 201):
        print("Success")
    else:
        print(response.status_code)


def text_message():
    message = twilio_client.messages \
        .create(
            body = 'Check Haze Discord.',
            from_ = '+17342281586', # Your Twilio account phone number here
            to = phone_number # Number you want to text
        )
    return message.status


@client.event
async def on_message(message):
    if message.content.startswith('^reboot'):
        author_role_ids = [y.id for y in message.author.roles]
        if 788117328046719017 in author_role_ids:
            reboot_digitalocean()
            await message.channel.send('Rebooting...')
        else:
            print(author_role_ids)
    elif message.content.startswith('^ping'):
        sms_message = text_message()
        await message.channel.send(
            f'Texting Invictus. Message status: {sms_message}'
        )  # Customize to your name
    elif message.content.startswith('^test'):
        author_role_ids = [y.id for y in message.author.roles]
        if 788117328046719017 in author_role_ids:
            await message.channel.send('I am awake...')
        else:
            print(author_role_ids)


client.run(discord_token)

# DISCORD_TOKEN = os.getenv("TOKEN")
# bot = commands.Bot(command_prefix="^")
# # print(DISCORD_TOKEN)
# bot.run('OTE1NDAxODQyOTc5MTM5NjE0.YabEZg.PihkTK4VAxAOjntRpCyyBCTL934')

# @bot.event
# async def on_message(message):
#     if message.content == 'reboot':
#         await message.channel.send('rebooting')
#     await bot.process_commands(message)

# @bot.command(name="ping")
# async def ping(ctx):
#     # try:
#     #     memberToLookUp = ctx.author
#     #     role = memberToLookUp.top_role
#     #     await ctx.channel.send(role)
#     # except:
#     #     await ctx.channel.send("pong")
#     await ctx.channel.send("pong")
