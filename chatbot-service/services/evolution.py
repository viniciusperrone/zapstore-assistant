import os
import requests
from dotenv import load_dotenv


load_dotenv()

class Evolution:

    def __init__(self):
        self.__api_url = 'http://evolution-api:9000'
        self.__api_key = os.getenv('AUTHENTICATION_API_KEY')

    def send_message(self, number_contact, message):
        url = f'{self.__api_url}/message/sendText/ZapStore-Assistance'

        headers = {
            'apikey': self.__api_key
        }

        body = {
            'number': number_contact,
            'text': message
        }

        requests.post(
            url=url,
            headers=headers,
            data=body
        )
