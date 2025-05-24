import json
import requests

from openai import OpenAI

from config.environments import API_URL, OPENAI_API_KEY
from utils.kind_message import MessageType
from utils.prompts import (
    PROMPT_RESUME_AGENT_SYSTEM,
    PROMPT_DETECT_TYPE_MESSAGE
)


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

    def __invoke_llm(self, system_prompt, user_prompt):
        response = self.__client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': system_prompt
                },
                {
                    'role': 'user',
                    'content': user_prompt
                }
            ]
        )

        return response.choices[0].message.content

    def detect_type_message(self, message):
        response = self.__invoke_llm(user_prompt=message, system_prompt=PROMPT_DETECT_TYPE_MESSAGE)

        try:
            return json.loads(response)

        except json.JSONDecodeError:

            return {
                'type': MessageType.UNKNOWN,
                'output': None
            }

    def invoke(self, received_message: str) -> None:
        response = self.__client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': PROMPT_RESUME_AGENT_SYSTEM
                },
                {
                    'role': 'user',
                    'content': received_message
                }
            ]
        )

        return response.choices[0].message.content
