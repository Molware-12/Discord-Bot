# This file creates a connection to the discord API

import discord
import response
from datetime import datetime

# Discord bot authorization link
link = "https://discord.com/api/oauth2/authorize?client_id=1140474199455047810&permissions=1634235578432&scope=bot"
guild_id = ""
# for the guild id, find the id for your guild, go to settings on discord, then going to 'advanced and enable developer mode'. Then, right-click on the server title and select "Copy ID" to get the guild id.
name = ""
# Just simply input the name of your server above ^

# Function to send a message based on user input
async def send_message(message, user_message, private):
    try:
        resp = response.handler(user_message,)
        if private == False:
            await message.channel.send(resp)
        else:
            await message.author.send(resp)
    except Exception as e:
        print(e)

# Function to run the Discord bot
def run_bot():
    token = ""
    # The token is your discord bots password essentially. 
    
    # Creating a Discord client instance with all intents enabled
    client = discord.Client(intents=discord.Intents.all())
    
    @client.event
    async def on_ready():
        # Event triggered when the bot is ready
        print(f"{client.user} is now running.")

    @client.event
    async def on_message(message):
        # Event triggered when a message is received

        if message.author == client.user:
            # Ignore messages from the bot itself
            return
        elif message.channel == client.get_channel(guild_id):
            # Ignore messages from a specific channel
            return

        user = str(message.author)
        user_msg = str(message.content)
        channel = str(message.channel)

        now = datetime.now()
        current_time = str(now.strftime("%M:%S"))

        print(f"{user} said '{user_msg}' ({channel}) at {current_time}")
        
        # Call the function to handle and send a response
        await send_message(message, user_msg, private=False)

    # Run the Discord bot with the specified token
    client.run(token)

# Entry point to run the bot
run_bot()
