from requests import request

# Mint NFT Function
def mint_nft(user_prompt, image_url, title, sui_address, discord_username=""):
    new_url = "https://mint-api.playcradle.com/mint"
    new_payload = {
        "prompt": user_prompt,
        "url": image_url,
        "title": title,
        "address": sui_address,
        "discord_username" : discord_username
    }
    
    response = request("POST", new_url, json=new_payload)

    new_image_url = response.json()['url']

    return new_image_url