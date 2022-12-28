from interactions import ActionRow, Button, ButtonStyle

from ..buttons import FANTASY_BUTTON, PAINTING_BUTTON, ANIME_BUTTON, COMIC_BUTTON, DYSTOPIAN_BUTTON

STYLES_ACTION_ROW = ActionRow(
    components=[
        FANTASY_BUTTON,
        PAINTING_BUTTON,
        ANIME_BUTTON,
        COMIC_BUTTON,
        DYSTOPIAN_BUTTON
    ]
)
