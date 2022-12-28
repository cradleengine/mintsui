
def generate_content(prompt="SET PROMPT", title="SET TITLE", address="SET ADDRESS", image_url="SET IMAGE URL"):
    lbr = "\n"
    return (
        "Your Prompt: "+ prompt +
        lbr +
        "Title: " + title +
        lbr +
        "Address: " + address + 
        lbr +
        "Your Image: " + image_url + 
        lbr +
        lbr +
        "Remix Your NFT Using One Of The Art Styles Below 🎨 " +
        lbr
    )
