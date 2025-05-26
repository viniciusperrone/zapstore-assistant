import requests

from config.environments import API_URL


class Catalog:

    def __init__(self):
        self.__api_url = f'{API_URL}/api/v1'

    def __get(self, endpoint: str, params: dict | None = None):
        response = requests.get(f"{self.__api_url}/{endpoint}", params=params)

        response.raise_for_status()

        return response.json()

    def get_products(self, filters: dict = None):
        return self.__get(
            endpoint='product',
            params=filters
        )

    def get_brands(self, filters: dict = None):
        return self.__get(
            endpoint='brand',
            params=filters
        )

    def get_categories(self, filters: dict = None):
        return self.__get(
            endpoint='category',
            params=filters
        )

    def get_suppliers(self, filters: dict = None):
        return self.__get(
            endpoint='supplier',
            params=filters
        )

    def get_inventory(self, filters: dict = None):
        return self.__get(
            endpoint='inventory/inflow',
            params=filters
        )

    def get_sales(self, filters: dict = None):
        return self.__get(
            endpoint='sales',
            params=filters
        )
