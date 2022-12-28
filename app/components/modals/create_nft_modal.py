from .template import create_modal
from ..text_inputs import PROMPT_INPUT, TITLE_INPUT, ADDRESS_INPUT

NFT_Modal = create_modal(title="Create NFT", custom_id="user_prompt_form", components=[PROMPT_INPUT, TITLE_INPUT, ADDRESS_INPUT])