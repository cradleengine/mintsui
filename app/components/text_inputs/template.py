from interactions import TextInput
from interactions import TextStyleType

def create_text_input(label="Set A Label", placeholder="Set placeholder text here", custom_id="SET_CUSTOM_ID", min_length=0, max_length=100):
    return TextInput(style=TextStyleType.SHORT, label=label, custom_id=custom_id, min_length=min_length, max_length=max_length, placeholder=placeholder)