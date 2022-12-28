from interactions import Modal

from ...api.suins import get_suins_username
from ...api.generate import generate_new_image
from ...components.action_rows import STYLES_ACTION_ROW, MINT_ACTION_ROW
from ...content import generate_content

def init_create_nft_modal(client=None):
    @client.modal("user_prompt_form")
    async def _user_prompt_form(ctx: Modal, user_prompt: str, title: str, address: str):
        await ctx.defer(ephemeral=True)

        suins_val = get_suins_username(address)
        
        suins_info = "\n SuiNS: " + address if (suins_val) else ""
        
        if (suins_val):
            address = suins_val
        else:
            if (len(address) != 42):
                await ctx.send(content="Invalid Wallet Address")
                return False

        image_url = generate_new_image(user_prompt)

        response_content = generate_content(prompt=user_prompt, title=title, address=address+suins_info, image_url=image_url)

        await ctx.send(content=response_content, components=[
            STYLES_ACTION_ROW,
            MINT_ACTION_ROW
        ], ephemeral=False,)        
