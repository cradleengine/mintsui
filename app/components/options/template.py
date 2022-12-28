from interactions import Option
from interactions import OptionType

def create_option(name="set_command_name", description="Set a command description"):
    return Option(name=name, description=description, type=OptionType.STRING, required=True)