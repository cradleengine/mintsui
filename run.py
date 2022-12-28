from app import init
from dotenv import load_dotenv
from os import environ

if __name__ == "__main__":
    # Initialize ENV Variables from .env file
    load_dotenv()

    # Initialize Discord Client
    client = init(environ.get("MINTSUI_TESTING_API_KEY"))

    # Start Discord Client
    client.start()