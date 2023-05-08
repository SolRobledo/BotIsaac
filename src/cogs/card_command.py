from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context

from src.parametros import Types
from src.db.queries import Queries


class CardCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query: Queries = Queries()

    @commands.command(name="card")
    async def card_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list[str] = message.split(" ")
        card_name: str = " ".join(message_l[1:]).strip()
        card: Optional[dict] = self.query.get_card(card_name, type_=Types.CARD)
        if card is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The card you are looking for doesn't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            name: str = card.get("name")
            function: str = card.get("function")
            id_: int = card.get("id")
            type_f: Types = card.get("type")
            unlock: str = card.get("unlock")
            pickup: str = card.get("pickup")
            link: dict = self.query.get_link_by_id(id_, type_=Types.CARD)
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **"+function, colour=discord.Color.teal())
            embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
            embed_a.add_field(name="*ID:* ", value=id_, inline=True)
            embed_a.add_field(name="*Pickup:* ", value=pickup, inline=True)
            if unlock is not None:
                embed_a.add_field(name="*Unlock method:* ", value=unlock, inline=False)
            if link:
                link_f: str = link.get("url")
                embed_a.set_thumbnail(url=link_f)
            await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(CardCommand(bot))
