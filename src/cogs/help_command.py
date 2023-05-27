import discord
from discord.ext import commands
from discord.ext.commands import Context


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["h"])
    async def send_help(self, ctx: Context):
        embed_a: discord.Embed = discord.Embed(title="Isaac Helper :D", description=f"**Commands:**\n1- *Item*: (item \"Item name\") Gives you a description of the item you are looking for. Alias: \"i\" \n"
                                                                                    f"2- *Card*: (card \"Card/rune name\") Gives you a description of the card/rune you are looking for. Alias: \"c\" \n"
                                                                                    f"3- *Trinket*: (trinket \"Trinket name\") Gives you a description of the Trinket you are looking for. Alias: \"tk\" \n"
                                                                                    f"4- *Pill*: (pill \"Pill name\") Gives you the effect of the pill you are looking for. Alias: \"pi\" \n"
                                                                                    f"5- *Pickup*: (pickup \"Pickup name\") Gives you a description of the pickup you are looking for. Alias: \"p\" \n"
                                                                                    f"6- *Find*: (finds\"item/card/rune/pickup/trinket/pill name\") Gives you the item or list of items you are looking for. Alias: \"f\" \n"
                                                                                    f"7- *Transformations*: (transformations) lists all isaac's transformations and how to get them. Alias: \"ts\" \n"
                                                                                    f"8- *Transformation*: (t \"transformation name\") Gives you the information of the transformation and the items you need to get it. Alias: \"t\" \n"
                                                                                    f"9- *Achievement*: (achievement \"Achievement name\") Gives you a description of the achievement you are looking for. Alias: \"a\" \n"
                                                                                    f"10- *Character*: (character \"Character name\") Gives you the stats of the character you are looking for. Alias: \"char\" \n", colour=discord.Color.dark_gold())
        embed_a.set_thumbnail(url="https://static.wikia.nocookie.net/bindingofisaacre_gamepedia/images/e/e5/Character_Isaac_appearance.png/revision/latest?cb=20210818221550")
        await ctx.send(embed=embed_a)


async def setup(bot):
    await bot.add_cog(Help(bot))
