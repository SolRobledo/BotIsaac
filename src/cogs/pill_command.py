from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context

from src.db.queries import Queries
from src.parametros import Types


class PillCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query: Queries = Queries()

    @commands.command(name="pill")
    async def pill_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list[str] = message.split(" ")
        pill_name: str = " ".join(message_l[1:]).strip()
        pill: Optional[dict] = self.query.get_item(pill_name, type_=Types.PILL)
        if pill is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The pill you are looking for doesn't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            name: str = pill.get("name")
            function: str = pill.get("function")
            id_: int = pill.get("id")
            type_f: str = pill.get("type")
            horse_pill_effect: str = pill.get("horse_pill")
            link: str = "https://static.wikia.nocookie.net/bindingofisaacre_gamepedia/images/e/e7/Achievement_2_new_pills_icon.png/revision/latest/scale-to-width-down/20?cb=20210821142409"
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **"+function, colour=discord.Color.purple())
            embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
            embed_a.add_field(name="*ID:* ", value=id_, inline=True)
            embed_a.add_field(name="*Horse pill effect:* ", value=horse_pill_effect, inline=False)
            embed_a.set_thumbnail(url=link)
            await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(PillCommand(bot))
