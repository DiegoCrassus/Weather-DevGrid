from os import environ
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.VERSION = environ.get("VERSION")
        self.FLASK_SERVER_NAME = None
        self.RESTX_VALIDATE = True
        self.RESTX_MASK_SWAGGER = False
        self.RESTX_SWAGGER_UI_DOC_EXPANSION = list
        self.RESTX_ERROR_404_HELP = False
        self.ENVIRONMENT = environ.get("ENVIRONMENT", "local")
        self.ENVIRONMENT = "local" if self.ENVIRONMENT == "local" else self.ENVIRONMENT

        # Env_vars
        self.FLASK_DEBUG = True if self.ENVIRONMENT == "local" else False
        self.FLASK_HOST = environ.get("FLASK_HOST", "0.0.0.0")
        self.FLASK_PORT = environ.get("FLASK_PORT", "5000")
        self.FLASK_URL_FIX = environ.get("FLASK_URL_FIX", "/api")
        self.ROUTE = environ.get("ROUTE", "/")
        self.HEALTH_ENDPOINT = environ.get("HEALTH_ENDPOINT", "status")
        self.WEATHER_ENDPOINT = environ.get("WEATHER_ENDPOINT", "weather")
        self.USER_ENDPOINT = environ.get("USER_ENDPOINT", "user")
        self.PATH_LOG = environ.get("PATH_LOG", "./log_amazon")
        self.DATABASE_URL = environ.get("DATABASE_URL", "postgresql+psycopg2://postgres:post2024@db:5432/postgres")

        self.OPEN_WEATHER_KEY = environ.get("OPEN_WEATHER_KEY", "ac2dad7604ad3b0a491d8e1739e9bc7d")
        self.OPEN_WEATHER_URL = environ.get("OPEN_WEATHER_URL", "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}")


envs = Config()
