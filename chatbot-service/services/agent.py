import requests
from dotenv import load_dotenv

load_dotenv()

from config.environments import API_URL


class Agent:

    def __init__(self) -> None:
        self.__catalog_url = f"{API_URL}/api/v1/all_data"

    def load_catalog_data(self):
        response = requests.get(self.__catalog_url)

        data = response

        return data.json()
