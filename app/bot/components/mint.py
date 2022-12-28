from interactions import ComponentContext

from ...api.mint import mint_nft
from ...components.buttons import MINT_YOUR_OWN_NFT_BUTTON

import re

def init_mint(client=None):
    @client.component("mint")
    async def _mint(ctx: ComponentContext):
        await ctx.defer(ephemeral=True)

        total_message = ctx.message.content

        prompt_group = re.search('Your Prompt: (.*)\n', total_message)
        user_prompt = prompt_group.group(1)

        title_group = re.search('Title: (.*)\n', total_message)
        title = title_group.group(1)

        address_group = re.search('Address: (.*)\n', total_message)
        address = address_group.group(1)

        suins_group = re.search("SuiNS: (.*)\n", total_message)
        suins = suins_group.group(1) if (suins_group and suins_group.group(1)) else address

        image_url_group = re.search('Your Image: (.*)\n', total_message)
        image_url = image_url_group.group(1)

        new_image_url = mint_nft(user_prompt, image_url, title, address)

        new_image_url = new_image_url.replace("gateway.pinata.cloud", "copper-recent-slug-804.mypinata.cloud")
        print(new_image_url)


        await ctx.send(content="MintSui Has Shipped", ephemeral=False)
        await ctx.channel.send(content=suins+" created " + "\"" + title + "\"" + "\n " + new_image_url, components=MINT_YOUR_OWN_NFT_BUTTON,)