from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("6124843978:AAHt9JKT-80M0QGQ66RMEUAs96M4jpbOijs")
API_ID = int(getenv("2882780", ""))
API_HASH = getenv("2ce43eaffaae1fc4016406b5b374cef9")
DURATION_LIMIT_MIN = int(getenv("10", "10"))
MONGO_DB_URI = getenv("mongodb+srv://MinatoMusicBot:<password>@cluster0.av8owp2.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("5575457497", "").split()))
OWNER_ID = list(map(int, getenv("5575457497", "").split()))
LOG_GROUP_ID = int(getenv("-1001941821946", ""))
MUSIC_BOT_NAME = getenv("Minato Music Bot")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/NotReallyShikhar/YukkiMusicBot"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("minatoesp")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("minatoesp")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("minatoespchats"))


if str(getenv("AQBpfBpk_CBn6lrm7MwyifrGqJK-lCzBhLbt8pTNVknKt_rYqiPUsMzZ0FP27SNG51YrpYMYvJSwi2je76IiTYC9gyxPK6x1z9r0CPR9n8IV0qCC0YLOCoLvPBhoWJiwhaR4TsMs2914Jonvy-nfEdgr_vZtIxrllnI_C51mcbpHyK-wqYpstHd5Hg3YC-OL22ZQdwyNswYUdjGWXszKaAQThiIccWCgKutkRUhX-Ql6FMYEMGnGO_MkTiPgnugIPZXZoM6UMKFN5xIfBZEfSk5TuKqkdQHHBD_dW60arWrhl__OZO6yck3-7jTzE7bThtQd7wHy5fPfm75jpN-D9ffIAAAAATxdOk0A")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
