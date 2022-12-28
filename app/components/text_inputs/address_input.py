from .template import create_text_input

ADDRESS_INPUT = create_text_input(
    label="Wallet Address",
    custom_id="address_input",
    min_length=1,
    max_length=100,
    placeholder="Let us know what your Sui Wallet Address is!"
)
