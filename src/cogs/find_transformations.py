from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context

from src.parametros import Types
from src.db.queries import Queries


class FindTransformations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query = Queries()

    @commands.command(name="transformation", aliases=["t"])
    async def find_transformations_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list = message.split(" ")
        transformation_name: str = " ".join(message_l[1:]).strip()
        transformation: Optional[dict] = self.query.get_transformation(transformation_name, type_=Types.TRANSFORMATION)
        if transformation is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The transformation you are looking for doesn't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            name: str = transformation.get("name")
            description: str = transformation.get("function")
            type_f: str = transformation.get("type")
            item_list: list[str] = transformation.get("item_list")
            link: dict = self.query.get_link(name, type_=Types.TRANSFORMATION)
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **" + description, colour=discord.Color.dark_purple())
            embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
            if link:
                link_f: str = link.get("url")
                embed_a.set_thumbnail(url=link_f)
            if item_list:
                embed_a.add_field(name="*Valid items for this transformation:* ", value="listed below", inline=False)
            await ctx.send(embed=embed_a)

            if item_list:
                for item in item_list:
                    item_f: dict = self.query.get_card(item, type_=Types.ITEM)
                    name: str = item_f.get("name")
                    function: str = item_f.get("function")
                    pickup: str = item_f.get("pickup")
                    quality: str = item_f.get("quality")
                    unlock: Optional[str] = item_f.get("unlock")
                    recharge: Optional[str] = item_f.get("recharge")
                    item_type: str = item_f.get("item_type")
                    id_: int = item_f.get("id")
                    item_link: dict = self.query.get_link_by_id(id_, type_=Types.ITEM)
                    embed_i: discord.Embed = discord.Embed(title=name, description=f"**Description:  **" + function, colour=discord.Color.dark_teal())
                    embed_i.add_field(name="*Type:* ", value=item_type, inline=True)
                    embed_i.add_field(name="*Quality:* ", value=quality, inline=True)
                    embed_i.add_field(name="*ID:* ", value=id_, inline=True)
                    if recharge is not None:
                        embed_i.add_field(name="*Recharge:* ", value=recharge, inline=True)
                    if unlock is not None:
                        embed_i.add_field(name="*Unlock method:* ", value=unlock, inline=False)
                    if item_link:
                        link: str = item_link.get("url")
                        embed_i.set_thumbnail(url=link)
                    embed_i.add_field(name="*Pickup:* ", value=pickup, inline=True)
                    await ctx.send(embed=embed_i)


async def setup(bot):
    await bot.add_cog(FindTransformations(bot))
