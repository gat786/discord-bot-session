import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix="!", description="Default help message")

bot.oof_counter = 0

@bot.command("hello")
async def hello_command(ctx: commands.context):
    await ctx.send("Hello {0.author}".format(ctx))

@bot.command("oof")
async def oof_counter(ctx:commands.context):
    bot.oof_counter += 1
    await ctx.send("counter at {0.oof_counter}".format(bot))

with open("./../secrets.json") as secrets:
    secret_object = json.loads("".join(secrets.readlines()))
    bot.run(secret_object["discord_token"])

# bot.run()

