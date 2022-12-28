from interactions import ComponentContext


from ...api.suins import get_suins_username
from ...api.generate import generate_new_image
from ...components.action_rows import STYLES_ACTION_ROW, MINT_ACTION_ROW
from ...content import generate_content

import re

def init_generate_again(client=None):
    @client.component("generate_again")
    async def _generate_again(ctx: ComponentContext):
        await ctx.defer(ephemeral=True)

        total_message = ctx.message.content
        prompt_group = re.search('Your Prompt: (.*)\n', total_message)
        user_prompt = prompt_group.group(1)

        title_group = re.search('Title: (.*)\n', total_message)
        title = title_group.group(1)

        address_group = re.search('Address: (.*)\n', total_message)
        address = address_group.group(1)

        suins_group = re.search("SuiNS: (.*)\n", total_message)
        suins = "\n SuiNS: " + suins_group.group(1) if (suins_group and suins_group.group(1)) else ""

        image_url = generate_new_image(user_prompt)


        await ctx.send(
            content=generate_content(
                prompt=user_prompt,
                title=title,
                address=address+suins,
                image_url=image_url
            ),
            components=[
                STYLES_ACTION_ROW,
                MINT_ACTION_ROW
            ], 
            ephemeral=False,
        )
