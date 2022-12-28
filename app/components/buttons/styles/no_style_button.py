from interactions import Button, ButtonStyle

NO_STYLE_BUTTON = Button(
    style=ButtonStyle.PRIMARY,
    label="Generate Again with No Style",
    custom_id="generate_again",
    emoji={
        "id" : None,
        "name" : "🔁"
    }
)