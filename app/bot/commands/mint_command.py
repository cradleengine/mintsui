from interactions import CommandContext

from ...api.suins import get_suins_username
from ...api.generate import generate_new_image
from ...components.options import IDEA_OPTION, TITLE_OPTION, ADDRESS_OPTION
from ...components.action_rows import STYLES_ACTION_ROW, MINT_ACTION_ROW
from ...content import generate_content

def init_mint_command(client=None, scope=[]):
    @client.command(name="mint", description="Generate a Pretty Image!", scope=scope, options=[IDEA_OPTION, TITLE_OPTION, ADDRESS_OPTION])
    async def minting_command(ctx: CommandContext, idea: str, title: str, sui_wallet_address: str):
        await ctx.defer(ephemeral=True)

        suins_val = get_suins_username(sui_wallet_address)
        
        suins_info = "\n SuiNS: " + sui_wallet_address if (suins_val) else ""
        
        if (suins_val):
            sui_wallet_address = suins_val
        else:
            if (len(sui_wallet_address) != 42):
                await ctx.send(content="Invalid Wallet Address")
                return False

        image_url = generate_new_image(idea)

        response_content = generate_content(prompt=idea, title=title, address=suins_info+sui_wallet_address, image_url=image_url)

        await ctx.send(content=response_content, components=[
            STYLES_ACTION_ROW,
            MINT_ACTION_ROW
        ], ephemeral=False,)
