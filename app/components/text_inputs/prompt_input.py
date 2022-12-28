from .template import create_text_input

PROMPT_INPUT = create_text_input(
    label="Describe the image you want to generate!",
    custom_id="text_input",
    min_length=1,
    max_length=500,
    placeholder="A dog on the beach with his best friend"
)
