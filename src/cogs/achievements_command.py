from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands import Context
from src.db.queries import Queries
from src.parametros import Types


class AchievementCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query: Queries = Queries()

    @commands.command(name="achievement", aliases=["a"])
    async def challenges_command(self, ctx: Context):
        message: str = ctx.message.content
        message_l: list = message.split(" ")
        achievement_name: str = " ".join(message_l[1:]).strip()
        achievement: Optional[dict] = self.query.get_achievement(achievement_name, type_=Types.ACHIEVEMENT)
        if achievement is None:
            embed_e: discord.Embed = discord.Embed(title="There has been an error", description="The achievement you are looking for doesn't exist D: srry", colour=discord.Color.dark_red())
            await ctx.send(embed=embed_e)

        else:
            name: str = achievement.get("name")
            function: str = achievement.get("description")
            unlock: Optional[str] = achievement.get("unlock")
            type_f: str = achievement.get("type")
            secret_number: int = achievement.get("secret_number")
            achievement_link: dict = self.query.get_link(name, type_=Types.ACHIEVEMENT)
            embed_a: discord.Embed = discord.Embed(title=name, description=f"**Description:  **"+function, colour=discord.Color.dark_magenta())
            embed_a.add_field(name="*Type:* ", value=type_f, inline=True)
            embed_a.add_field(name="*Secret number:* ", value=secret_number, inline=True)
            if unlock is not None:
                embed_a.add_field(name="*Unlock method:* ", value=unlock, inline=False)
            if achievement_link:
                link: str = achievement_link.get("url")
                embed_a.set_thumbnail(url=link)
            await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(AchievementCommand(bot))
