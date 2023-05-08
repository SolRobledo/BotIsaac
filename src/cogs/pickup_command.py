from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context

from src.db.queries import Queries
from src.parametros import Types


class PickupCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query: Queries = Queries()

    @commands.command(name="pickup")
    async def pickup_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list[str] = message.split(" ")
        pickup_name: str = " ".join(message_l[1:]).strip()
        pickup: Optional[dict] = self.query.get_item(pickup_name, type_=Types.PICKUP)
        if pickup is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The pickup you are looking for doesn't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            name: str = pickup.get("name")
            function: Optional[str] = pickup.get("function")
            type_f: str = pickup.get("type")
            probability: str = pickup.get("probability")
            link: dict = self.query.get_link(name, type_=Types.PICKUP)
            if function is not None:
                embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **"+function, colour=discord.Color.dark_green())
            else:
                embed_a: discord.Embed = discord.Embed(title=name, colour=discord.Color.dark_green())
            embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
            embed_a.add_field(name="*Probability:* ", value=probability, inline=True)
            if link:
                link_f: str = link.get("url")
                embed_a.set_thumbnail(url=link_f)
            await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(PickupCommand(bot))
