import requests

from config.environments import API_URL


class Catalog:

    def __init__(self):
        self.__api_url = API_URL

    def get_all_data(self):
        response = requests.get(self.__api_url)

        data = response.json()

        return data
