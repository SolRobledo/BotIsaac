from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context

from src.db.queries import Queries
from src.parametros import Types


class TransformationsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query = Queries()

    @commands.command(name="transformations", aliases=["ts"])
    async def transformations_command(self, ctx: Context):
        transformation_l: list[dict] = self.query.get_transformations()

        if transformation_l is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="could not find the transformations", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            for transformation in transformation_l:
                name: str = transformation.get("name")
                description: str = transformation.get("function")
                type_f: str = transformation.get("type")
                item_list: Optional[list[str]] = transformation.get("item_list")
                link: Optional[dict] = self.query.get_link(name, type_=Types.TRANSFORMATION)
                items: str = ""
                if item_list:
                    for item in item_list:
                        items += "\n" + item
                embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **"+description, colour=discord.Color.dark_purple())
                embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
                if items:
                    embed_a.add_field(name="*Valid items for this transformation:* ", value=items, inline=False)
                if link:
                    link_f: str = link.get("url")
                    embed_a.set_thumbnail(url=link_f)
                await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(TransformationsCommand(bot))
