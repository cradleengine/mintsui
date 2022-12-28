from interactions import ActionRow, Button, ButtonStyle

from ..buttons import NO_STYLE_BUTTON, MINT_NFT_BUTTON

MINT_ACTION_ROW = ActionRow(
    components=[
        NO_STYLE_BUTTON,
        MINT_NFT_BUTTON,
    ]
)