import environ

env = environ.Env()
environ.Env.read_env()

DB_NAME = env("DB_NAME")
DB_USER = env("DB_USER")
DB_PASSWORD = env("DB_PASSWORD")
DB_HOST = env("DB_HOST")
DB_PORT = env("DB_PORT")
API_TOKEN = env("API_TOKEN")