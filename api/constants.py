import os
from dotenv import load_dotenv

load_dotenv()


KEY = os.getenv("JWT_SECRET_KEY")
ACCESS = "access"
ALGORITH = "HS256"

PROFILE = "profile"
DEFAULT_PROFILE = ""
DEFAULT_PROFILE_URL = ""


DEFAULT_SUBGROUP = ""
DEFAULT_SUBGROUP_URL = ""


DEFAULT_EVENT = ""
DEFAULT_EVENT_URL = ""
