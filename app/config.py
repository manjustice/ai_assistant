import json
import os
from dotenv import load_dotenv
from starlette.templating import Jinja2Templates

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

templates = Jinja2Templates(directory="templates")

with open("FAQ.json", encoding="utf-8") as f:
    FAQ_DATA = json.load(f)
