from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "AQADgrtGBYdEQ7_uzZIPLHszCazaxxCJe0QkVT0QQ3htNMMXaD-526bvbA4zp8nVivWHklOqw2HlRpSzs4NvERGew5muzzwiBnaLvQN2gfwXBAYJSg13MBcG9LY4lFJG_ZQ7fVPEDn4K2Gnj9uDJaBMsBJuIDNCOpUZYYxZVMeTx0j5pVC4Z6Ldy74vCIhxyAAgzYN-Mxp9Oc5wVfR5isGJc2f0LQw7LVHlC33tSpzvbS1zflR8nLxwVqUEuJWP3X5MmBryRmSfdworxHG-lxE5FxG0BnavaOe3CJ0_x0-U9CGuHj-c86eulohTnUfe6Y6ezNfPQwcOhJfVtY5-HgbUAaA-KyQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1788824202:AAHQ1mG36pESwEfRBw6ck0qWQ4TUDVzxn60")
API_ID = int(getenv("API_ID", "8538756"))
API_HASH = getenv("API_HASH", "be2899f8951793b33a8eccfd4adcfb19")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "50"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
