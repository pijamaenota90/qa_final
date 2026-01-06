import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class WikiUser:
    username: str = os.getenv('WIKI_USERNAME')
    password: str = os.getenv('WIKI_PASSWORD')
