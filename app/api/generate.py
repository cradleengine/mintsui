from requests import request

# Generate Image Function
def generate_new_image(user_prompt):
    url = "https://mint-api.playcradle.com/generate"
    payload = {"prompt": user_prompt}
    headers = {"Content-Type": "application/json"}
    response = request("POST", url, json=payload, headers=headers)
    image_url = response.json()['url']
    return image_url