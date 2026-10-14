import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8712507397:AAEJVMD213TIpTbu85OeqrXNwsnX16f9ZUA")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "30247401"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "15672484ee3efb90c52f8fcc0339f525")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "6367695013").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "User")  # Making CREDIT an environment variable for flexibility
