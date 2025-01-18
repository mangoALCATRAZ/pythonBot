import discord

# DOn't store this here, dingus!
DISCORD_TOKEN = "MTMzMDI5MDE3MDc3NTIxMjE4NA.Gu_q7i.tY0m5qM2Q_7XU3Zg68tHkUe1iXFP9EpeVYvpZM"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content == "!hello":
        await message.channel.send(f'Hello, {message.author.mention}!')

client.run(DISCORD_TOKEN)
print("Bot is connected to server")