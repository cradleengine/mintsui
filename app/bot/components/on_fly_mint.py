from interactions import ComponentContext

from ...components.modals import NFT_Modal

def init_on_fly_mint(client=None):
    @client.component("on_fly_mint")
    async def _on_fly_mint(ctx: ComponentContext):
        await ctx.popup(modal=NFT_Modal)
