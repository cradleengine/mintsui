from interactions import Modal

def create_modal(title="SET_TITLE", custom_id="SET_CUSTOM_ID", components=[]):
    return Modal(title=title, custom_id=custom_id, components=components)