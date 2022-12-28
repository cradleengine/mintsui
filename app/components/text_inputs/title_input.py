from .template import create_text_input

TITLE_INPUT = create_text_input(
    label="Title",
    custom_id="title_input",
    min_length=1,
    max_length=50,
    placeholder="Give Your NFT a nice Title!"
)
