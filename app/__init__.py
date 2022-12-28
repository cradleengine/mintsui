from interactions import Client
from .bot import init_mint_command, init_create_nft_modal, init_generate_again, init_fantasy_regen, init_painting_regen, init_anime_regen, init_comic_regen, init_dystopian_regen, init_on_fly_mint, init_mint
from .scope import SCOPES

def init(api_key):
    # Initialize MintSui Client with Discord API KEY TODO: Link where to get this information from.
    mintsui_client = Client(token=api_key)

    init_mint_command(client=mintsui_client, scope=SCOPES)
    init_create_nft_modal(client=mintsui_client)
    init_generate_again(client=mintsui_client)
    init_fantasy_regen(client=mintsui_client)
    init_painting_regen(client=mintsui_client)
    init_anime_regen(client=mintsui_client)
    init_comic_regen(client=mintsui_client)
    init_dystopian_regen(client=mintsui_client)
    init_on_fly_mint(client=mintsui_client)
    init_mint(client=mintsui_client)

    return mintsui_client


