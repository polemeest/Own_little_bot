"""
Environment variable configuration and other dependencies
"""

from os import getenv
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = getenv("BOT_TOKEN")
