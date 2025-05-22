import requests

from config.environments import (
    EVOLUTION_API_URL,
    AUTHENTICATION_API_KEY
)


class Evolution:

    def __init__(self):
        self.__api_url = EVOLUTION_API_URL
        self.__api_key = AUTHENTICATION_API_KEY

    def send_message(self, number_contact, message):
        url = f'{self.__api_url}/message/sendText/ZapStore-Assistant'

        headers = {
            'apikey': self.__api_key,
            'Context-Type': 'application/json'
        }

        payload = {
            'number': number_contact,
            'text': message
        }

        requests.post(
            url=url,
            headers=headers,
            json=payload
        )
