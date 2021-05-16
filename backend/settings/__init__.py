import os

IS_PRODUCTION = os.getenv('IS_PRODUCTION') or False
DEBUG = os.getenv('DEBUG') or False
SERVICE_HOST = os.getenv('SERVICE_HOST') or '0.0.0.0'
SERVICE_PORT = os.getenv('SERVICE_PORT') or 7070

# Database:

DB_URL = os.getenv('DB_URL') or 'postgresql://user:pswrd@127.0.0.1:5432/calc'

STATE_CODES = ['CA', 'AL', 'UT', 'TX', 'NV']
