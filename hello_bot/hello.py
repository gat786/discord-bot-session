import discord
from discord import client 
import json

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as {0}".format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == "!hello":
            await message.channel.send("Hello {0.author}".format(message))
        

with open("./../secrets.json") as secrets:
    secret_object = json.loads("".join(secrets.readlines()))

    client = MyClient()
    client.run(secret_object["discord_token"])
