import discord
from discord.ext import commands

# DOn't store this here, dingus!
DISCORD_TOKEN = "MTMzMDI5MDE3MDc3NTIxMjE4NA.Gn4F9X.ypNYhSTMCVWbnnR-bS09ewmk-QXgI7_jpadpbo"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def slap(ctx, who : discord.Member, withwhat):
    nick = who.nick
    me = ctx.author.nick
    await ctx.send(f"{me} slapped {nick} with a {withwhat}")


bot.run(DISCORD_TOKEN)

print("Bot is connected to server")