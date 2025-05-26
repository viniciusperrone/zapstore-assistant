import os
from dotenv import load_dotenv


load_dotenv()

EVOLUTION_API_URL = os.getenv('EVOLUTION_API_URL')
AUTHENTICATION_API_KEY = os.getenv('AUTHENTICATION_API_KEY')
EVOLUTION_INSTANCE_NAME = os.getenv('EVOLUTION_INSTANCE_NAME')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
API_URL = os.getenv('API_URL', 'http://host.docker.internal:8000')

MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME')
