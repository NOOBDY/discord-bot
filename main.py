import json
import os

from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount+1):
        messages.append(message)
    await channel.delete_messages(messages)
    print("Messages deleted")

if __name__ == "__main__":

    with open("secrets.json") as secrets:
        data = json.load(secrets)
        TOKEN = data["TOKEN"]

    client.run(TOKEN)
