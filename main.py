import asyncio
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv


def get_prefix(bot_, message):
    prefix: list[str] = [";"]
    return commands.when_mentioned_or(*prefix)(bot_, message)


async def load_extensions(bot_):
    for filename in os.listdir("src/cogs"):
        if filename.endswith(".py"):
            await bot_.load_extension(f"src.cogs.{filename[:-3]}")


async def main():
    intents: discord.Intents = discord.Intents.all()
    bot_: Bot = commands.Bot(command_prefix=get_prefix, intents=intents)
    async with bot_:
        await load_extensions(bot_)
        load_dotenv()
        TOKEN: str = os.getenv("TOKEN")
        await bot_.start(TOKEN, reconnect=True)


if __name__ == '__main__':
    asyncio.run(main())
