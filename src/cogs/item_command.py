from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context

from src.parametros import Types
from src.db.queries import Queries


class ItemCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query: Queries = Queries()

    @commands.command(name="item", aliases=["i"])
    async def item_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list = message.split(" ")
        item_name: str = " ".join(message_l[1:]).strip()
        item: Optional[dict] = self.query.get_item(item_name, type_=Types.ITEM)
        if item is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The item you are looking for doesn't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            name: str = item.get("name")
            function: str = item.get("function")
            pickup: str = item.get("pickup")
            quality: int = item.get("quality")
            unlock: Optional[str] = item.get("unlock")
            recharge: Optional[str] = item.get("recharge")
            item_type: str = item.get("item_type")
            id_: int = item.get("id")
            item_link: dict = self.query.get_link_by_id(id_, type_=Types.ITEM)
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **"+function, colour=discord.Color.dark_teal())
            embed_a.add_field(name="*Type:* ", value=item_type, inline=True)
            embed_a.add_field(name="*Quality:* ", value=quality, inline=True)
            embed_a.add_field(name="*ID:* ", value=id_, inline=True)
            if recharge is not None:
                embed_a.add_field(name="*Recharge:* ", value=recharge, inline=True)
            if unlock is not None:
                embed_a.add_field(name="*Unlock method:* ", value=unlock, inline=False)
            if item_link:
                link: str = item_link.get("url")
                embed_a.set_thumbnail(url=link)
            embed_a.add_field(name="*Pickup:* ", value=pickup, inline=True)
            await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(ItemCommand(bot))
