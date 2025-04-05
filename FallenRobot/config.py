class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 6
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002124344872)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = ""  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://media-hosting.imagekit.io//29c440e1c11a483f/Leonardo_Phoenix_09_A_futuristic.png?Expires=1835940922&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=mLurawjT-Bi9EidlFkD41nejDH4f2Ujb6IoXtfJ1IE6WFCx~CR6k3CAa3GKthkzdEC9X8KzK0qY6IlglWoMgAiuuWon4U3hwZdwYIsKH~~0tDnCqCYxTbvX9c7EfrBiBA4ozpvYLOUu-cg0H5OK1~9P4J0~my81p06nBRfA3nEFHFyL4tUQAaXj-Xd6glONZUTMKow93sAQptovx5aiOxdJuqFRJtnm3knpSaSVm~SAUGcYPkWJm3IyPXVXzh7EPRe4olWtWgF~-m8ixdWxSEkVDYdvmXq4RfgEp0Q1QEqauNi2B-O-9P1F1dE0Y68E3ndllLlY1mBWEqK44qr75Gw__"

    SUPPORT_CHAT = "GARUD_SUPPORT"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7448520005  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
