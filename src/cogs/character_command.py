from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context
from src.db.queries import Queries
from src.parametros import Types


class CharacterCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query: Queries = Queries()

    @commands.command(name="character", aliases=["char"])
    async def characters_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list = message.strip().split(" ")
        char_name: str = " ".join(message_l[1:]).strip()
        character: Optional[dict] = self.query.get_character(char_name, type_=Types.CHARACTER)
        print(character)
        if character is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The character you are looking for doesn't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)
        else:
            char_link: str = character.get("link")
            name: str = character.get("name")
            health: dict = character.get("health")
            damage: str = character.get("damage")
            tears: str = character.get("tears")
            shot_speed: str = character.get("shot_speed")
            range_: str = character.get("range_")
            speed: str = character.get("speed")
            luck: str = character.get("luck")
            items: list = character.get("items")
            unlock: str = character.get("unlock")
            type_: str = character.get("type_")
            items_f: str = ""
            health_f = ""
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Unlock:  **" + unlock, colour=discord.Color.blue())
            embed_a.add_field(name="*Damage:* ", value=damage, inline=True)
            embed_a.add_field(name="*Tears:* ", value=tears, inline=True)
            embed_a.add_field(name="*Shot Speed:* ", value=shot_speed, inline=True)
            embed_a.add_field(name="*Range:* ", value=range_, inline=True)
            embed_a.add_field(name="*Speed:* ", value=speed, inline=True)
            embed_a.add_field(name="*Luck:* ", value=luck, inline=True)
            embed_a.add_field(name="*Type:* ", value=type_, inline=True)
            if char_link:
                embed_a.set_thumbnail(url=char_link)
            if type(items) == list:
                for item in items:
                    items_f += "\n" + item
                embed_a.add_field(name="*Starts with this items/attributes:* \n", value=items_f.strip(), inline=True)
            else:
                embed_a.add_field(name="*Starts with this item:* ", value=items, inline=True)
            if type(health) == str:
                embed_a.add_field(name="*Health:* ", value=health, inline=True)
            else:
                for key in health:
                    health_f += "\n" + key
                embed_a.add_field(name="*Health:* ", value=health_f.strip(), inline=True)

            await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(CharacterCommand(bot))
