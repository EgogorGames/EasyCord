# Importing modules

import esycord as es # Importing esycord module
from discord import * # Importing Discord module

# Creating client/tree

client = es.client(command_prefix="!", intents=Intents.all()) # Creating client, `command_prefix` - Default command prefix, `intents` - Intents.
tree = client.get_tree() # Creating tree

# Creating default command(!reply) what replyes with hello message.

@client.default_command(name="reply") # Creating command with name `reply`
async def reply(esyraction:es.Esyraction): # Creating reply def
    await esyraction.reply("hello") # Making bot replyes to message with hello message

# Creating on_msd(on_message) event

@client.on_msg() # Creating event
async def on_msg(message:Message): # Creating on_msg def
    print(message.content) # Printing message into console

# Creating slash command(/help) what gives help menu

@tree.command(name="help", description="Help menu") # Creating slash command with name help and description `Help menu`
async def help(interaction : Interaction): # Creating help def
    await interaction.response.send_message("Help menu.\n- `!reply` - Replyes with hello message!") # Sending message with help menu

# Running bot

client.bot_run("TOKEN") # Running bot

# Code without comments

"""
import esycord as es
from discord import *

client = es.client(command_prefix="!", intents=Intents.all())
tree = client.get_tree()

@client.default_command(name="reply")
async def reply(esyraction:es.Esyraction):
    await esyraction.reply("hello")

@client.on_msg()
async def on_msg(message:Message):
    print(message.content)

@tree.command(name="help", description="Help menu")
async def help(interaction : Interaction):
    await interaction.response.send_message("Help menu.\n- `!reply` - Replyes with hello message!")

client.bot_run("TOKEN")
"""
