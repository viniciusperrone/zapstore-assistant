import requests
from openai import OpenAI

from config.environments import API_URL, OPENAI_API_KEY
from utils.prompts import PROMPT_AGENT_SYSTEM


class Agent:

    def __init__(self) -> None:
        self.__catalog_url = f"{API_URL}/api/v1/all_data"
        self.__client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def load_catalog_data(self):
        response = requests.get(self.__catalog_url)

        data = response

        return data.json()

    def __detect_type_message(self):
        return ''

    def invoke(self, received_message: str) -> None:
        response = self.__client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': PROMPT_AGENT_SYSTEM
                },
                {
                    'role': 'user',
                    'content': received_message
                }
            ]
        )

        return response.choices[0].message.content
