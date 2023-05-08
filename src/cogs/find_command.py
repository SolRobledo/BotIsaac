from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context

from src.parametros import Types
from src.db.queries import Queries


class FindCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query = Queries()

    @commands.command(name="find")
    async def card_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list[str] = message.split(" ")
        item_name: str = " ".join(message_l[1:]).strip()
        items: Optional[list] = self.query.get_r_items(item_name)
        if items is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The element/elements you are looking for don't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            for item in items:
                embed: discord.Embed = self.sorting_hat(item)
                await ctx.send(embed=embed)

    def sorting_hat(self, item: dict) -> discord.Embed:
        item_type: Types = item.get("type")
        if item_type == Types.ITEM:
            embed: discord.Embed = self.get_item_embed(item)
            return embed
        elif item_type == Types.TRINKET:
            embed: discord.Embed = self.get_trinket_embed(item)
            return embed
        elif item_type == Types.CARD:
            embed: discord.Embed = self.get_card_embed(item)
            return embed
        elif item_type == Types.PICKUP:
            embed: discord.Embed = self.get_pickup_embed(item)
            return embed
        elif item_type == Types.PILL:
            embed: discord.Embed = self.get_pill_embed(item)
            return embed

    def get_item_embed(self, item: dict) -> discord.Embed:
        name: str = item.get("name")
        function: str = item.get("function")
        pickup: str = item.get("pickup")
        quality: int = item.get("quality")
        unlock: Optional[str] = item.get("unlock")
        recharge: Optional[str] = item.get("recharge")
        item_type: str = item.get("item_type")
        id_: int = item.get("id")
        item_link: dict = self.query.get_link_by_id(id_, type_=Types.ITEM)
        embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **" + function, colour=discord.Color.dark_teal())
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
        return embed_a

    def get_trinket_embed(self, trinket: dict) -> discord.Embed:
        name: str = trinket.get("name")
        function: str = trinket.get("function")
        type_f: Types = trinket.get("type")
        pickup: str = trinket.get("pickup")
        unlock: Optional[str] = trinket.get("unlock")
        id_: int = trinket.get("id")
        trinket_link: dict = self.query.get_link_by_id(id_, type_=Types.TRINKET)
        embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **" + function, colour=discord.Color.dark_orange())
        embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
        embed_a.add_field(name="*ID:* ", value=id_, inline=True)
        if trinket_link:
            link: str = trinket_link.get("url")
            embed_a.set_thumbnail(url=link)
        if unlock is not None:
            embed_a.add_field(name="*Unlock method:* ", value=unlock, inline=False)
        embed_a.add_field(name="*Pickup:* ", value=pickup, inline=True)
        return embed_a

    def get_card_embed(self, card: dict) -> discord.Embed:
        name: str = card.get("name")
        function: str = card.get("function")
        id_: int = card.get("id")
        type_f: Types = card.get("type")
        unlock: Optional[str] = card.get("unlock")
        pickup: str = card.get("pickup")
        link: dict = self.query.get_link_by_id(id_, type_=Types.CARD)
        if function != "":
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **" + function, colour=discord.Color.teal())
        else:
            embed_a: discord.Embed = discord.Embed(title=name, colour=discord.Color.teal())
        embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
        embed_a.add_field(name="*ID:* ", value=id_, inline=True)
        embed_a.add_field(name="*Pickup:* ", value=pickup, inline=True)
        if unlock is not None:
            embed_a.add_field(name="*Unlock method:* ", value=unlock, inline=False)
        if link:
            link_f: str = link.get("url")
            embed_a.set_thumbnail(url=link_f)
        return embed_a

    def get_pickup_embed(self, pickup: dict) -> discord.Embed:
        name: str = pickup.get("name")
        function: str = pickup.get("function")
        type_f: Types = pickup.get("type")
        probability: str = pickup.get("probability")
        link: dict = self.query.get_link(name, type_=Types.PICKUP)
        if function != "":
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **" + function, colour=discord.Color.dark_green())
        else:
            embed_a: discord.Embed = discord.Embed(title=name, colour=discord.Color.dark_green())
        embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
        embed_a.add_field(name="*Probability:* ", value=probability, inline=True)
        if link:
            link_f: str = link.get("url")
            embed_a.set_thumbnail(url=link_f)
        return embed_a

    @staticmethod
    def get_pill_embed(pill: dict) -> discord.Embed:
        name: str = pill.get("name")
        function: str = pill.get("function")
        id_: int = pill.get("id")
        type_f: Types = pill.get("type")
        horse_pill_effect: str = pill.get("horse_pill")
        link: str = "https://static.wikia.nocookie.net/bindingofisaacre_gamepedia/images/e/e7/Achievement_2_new_pills_icon.png/revision/latest/scale-to-width-down/20?cb=20210821142409"
        embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **" + function, colour=discord.Color.purple())
        embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
        embed_a.add_field(name="*ID:* ", value=id_, inline=True)
        embed_a.add_field(name="*Horse pill effect:* ", value=horse_pill_effect, inline=False)
        embed_a.set_thumbnail(url=link)
        return embed_a


async def setup(bot):
    await bot.add_cog(FindCommand(bot))
