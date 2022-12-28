# Import in all Options that need to be accessed
from .template import create_option

IDEA_OPTION = create_option(name="idea", description="What you want your NFT to look like")
TITLE_OPTION = create_option(name="title", description="The Title of your NFT")
ADDRESS_OPTION = create_option(name="sui_wallet_address", description="Your Sui Wallet Address")