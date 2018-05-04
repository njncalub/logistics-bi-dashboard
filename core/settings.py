import warnings

from dotenv import find_dotenv, load_dotenv
from envparse import Env


env = Env(READ_DOT_PROJENV=bool,
          DOT_PROJENV_OVERRIDE=bool,
          DEBUG=bool,
          SCRAPER_PAGINATION_DIVIDER=int)


# Using a flag here to check if .proj-env should be loaded. We use .proj-env
# instead of .env to circumnavigate pipenv's default feature of automatically
# loading .env files in your project.
READ_DOT_PROJENV = env('READ_DOT_PROJENV', default=True)
DOT_PROJENV_FILENAME = env('DOT_PROJENV_FILENAME', default='.proj-env')
DOT_PROJENV_OVERRIDE = env('DOT_PROJENV_OVERRIDE', default=False)

if READ_DOT_PROJENV:
    with warnings.catch_warnings():
        warnings.filterwarnings('error')
        try:
            ENV_PATH = find_dotenv(filename=DOT_PROJENV_FILENAME)
            load_dotenv(dotenv_path=ENV_PATH, override=DOT_PROJENV_OVERRIDE,
                        verbose=True)
        except Warning:
            pass


SECRET_KEY = env('SECRET_KEY', default='SET-YOUR-SECRET-KEY')
DEBUG = env('DEBUG', default=False)

# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------
DATABASE_URL = env('DATABASE_URL',
                   default='postgresql://127.0.0.1:5432/logistiko')

# -----------------------------------------------------------------------------
# Server
# -----------------------------------------------------------------------------
SERVER_HOST = env('SERVER_HOST', default='0.0.0.0')
SERVER_PORT = env('SERVER_PORT', default='5000')
