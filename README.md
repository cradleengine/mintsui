<p align="center">
  <a href="https://mintsui.com">
    <img alt="mintsui logo" width="100%" src="https://user-images.githubusercontent.com/39306557/209747719-412595d9-ed17-4521-94e4-a83bb8ee2dcb.png" />
  </a>
</p>

# MintSui
MintSui is a simple Discord bot that allows users to Generate AI NFTs and Mint them on the Sui Blockchain

## Pre-requistes
- You will need to create an `.env` file and put it in the root directory of the repository. Look at `.env.example` to see what the env should look like.
- You also want to change the `SCOPES` variable under `app/scope.py` with the ID of the Server you want to add the Discord bot to.

## Setup
```
cd mintsui
pip3 install -r requirements.txt
python3 run.py
```

## Usage
Once the Bot has been added to your server you can use it by doing either of the following:
1. Use the `/mint` command which will prompt you to enter a `prompt` (idea), `title`, and a `sui_wallet_address`
2. Click the green button at the bottom of the latest NFT generation. If no generations yet, use the first method.

## Questions ?
If you have any questions, feel free to open an issue on Github or send me a DM on Discord (thayallan#6706)
