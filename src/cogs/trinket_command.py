from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context

from src.db.queries import Queries
from src.parametros import Types


class TrinketCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query: Queries = Queries()

    @commands.command(name="trinket", aliases=["tk"])
    async def trinket_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list[str] = message.split(" ")
        trinket_name: str = " ".join(message_l[1:]).strip()
        trinket: Optional[dict] = self.query.get_item(trinket_name, type_=Types.TRINKET)
        if trinket is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The trinket you are looking for doesn't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            name: str = trinket.get("name")
            function: str = trinket.get("function")
            type_f: str = trinket.get("type")
            pickup: str = trinket.get("pickup")
            unlock: Optional[str] = trinket.get("unlock")
            id_: int = trinket.get("id")
            trinket_link: dict = self.query.get_link_by_id(id_, type_=Types.TRINKET)
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **"+function, colour=discord.Color.dark_orange())
            embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
            embed_a.add_field(name="*ID:* ", value=id_, inline=True)
            if trinket_link:
                link: str = trinket_link.get("url")
                embed_a.set_thumbnail(url=link)
            if unlock is not None:
                embed_a.add_field(name="*Unlock method:* ", value=unlock, inline=False)
            embed_a.add_field(name="*Pickup:* ", value=pickup, inline=True)
            await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(TrinketCommand(bot))
