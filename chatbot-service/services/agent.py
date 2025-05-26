import json
import requests
from typing import Dict, Any

from openai import OpenAI
from services.catalog import Catalog

from config.environments import OPENAI_API_KEY
from utils.kind_message import MessageType
from utils.prompts import (
    PROMPT_RESUME_AGENT_SYSTEM,
    PROMPT_DETECT_TYPE_MESSAGE
)
from utils.messages import OUT_OF_SCOPE

class Agent:

    def __init__(self) -> None:
        self.__catalog = Catalog()
        self.__client = OpenAI(
            api_key=OPENAI_API_KEY
        )


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

    def detect_type_message(self, message) -> Dict[Any, Any]:
        response = self.__invoke_llm(user_prompt=message, system_prompt=PROMPT_DETECT_TYPE_MESSAGE)

        try:
            return json.loads(response)

        except json.JSONDecodeError:

            return {
                'type': MessageType.UNKNOWN.value,
                'filters': None,
                'output': None
            }

    def invoke(self, message: str, data: dict) -> str:
        message_type = MessageType(data.get('type', MessageType.UNKNOWN.value))
        filters = data.get('filters', None)
        output_prompt = data.get('output_prompt', None)
        catalog_data: str = None
        context_messages = data.get('context_messages', [])

        messages_prompt = []

        if message_type == MessageType.PRODUCT:
            catalog_json = self.__catalog.get_products(filters=filters)

            catalog_data = json.dumps(catalog_json)

        if message_type == MessageType.BRAND:
            catalog_json = self.__catalog.get_products(filters=filters)

            catalog_data = json.dumps(catalog_json)

        if message_type == MessageType.CATEGORY:
            catalog_json = self.__catalog.get_categories(filters=filters)

            catalog_data = json.dumps(catalog_json)

        if message_type == MessageType.SUPPLIER:
            catalog_json = self.__catalog.get_suppliers(filters=filters)

            catalog_data = json.dumps(catalog_json)

        if message_type == MessageType.INVENTORY:
            catalog_json = self.__catalog.get_inventory(filters=filters)

            catalog_data = json.dumps(catalog_json)

        if message_type == MessageType.SALE:
            catalog_json = self.__catalog.get_sales(filters=filters)

            catalog_data = json.dumps(catalog_json)

        if message_type == MessageType.UNKNOWN:
            return OUT_OF_SCOPE

        system_prompt = f"{PROMPT_RESUME_AGENT_SYSTEM} \n\n{output_prompt}\n\nDados em formato json (a serem analisados): {catalog_data}"

        messages_prompt.append({
            'role': 'system',
            'content': system_prompt
        })

        if context_messages:
            historic_conversation = []

            for conversation in context_messages:
                historic_conversation.append(conversation)

            messages_prompt.append({'role': 'system', 'content': f'Histórico de conversa: \n {str(conversation)}'})

        messages_prompt.append({
            'role': 'user',
            'content': message
        })

        response = self.__client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages_prompt
        )

        return response.choices[0].message.content


    def process_intent(self, message: str, intent_type: str):
        catalog_data = self.load_catalog_data()

        if MessageType(intent_type) == MessageType.PRODUCTS:
            prompt = f"Liste os produtos disponíveis com base nessa base de dados:\n\n{catalog_data}"

        elif MessageType(intent_type) == MessageType.SPECIFIC_PRODUCT:
            prompt = f"Com base na seguinte base de dados:\n\n{catalog_data}\n\nResponda à pergunta do usuário: {message}"

        elif MessageType(intent_type) == MessageType.INFORMATION_ABOUT_BRANDS:
            brands = list({item["brand"] for item in catalog_data})  # Extrai marcas únicas
            prompt = f"Estas são as marcas disponíveis: {', '.join(brands)}.\nResponda de forma útil à pergunta: {message}"

        elif MessageType(intent_type) == MessageType.CHEAPER_PRODUCTS:
            sorted_data = sorted(catalog_data, key=lambda x: x["price"])
            cheapest = sorted_data[:5]
            prompt = f"Estes são os 5 produtos mais baratos:\n\n{cheapest}\n\nDê uma resposta amigável ao usuário."

        else:
            prompt = message

        return self.__invoke_llm(system_prompt=PROMPT_RESUME_AGENT_SYSTEM, user_prompt=prompt)

    def invokedede(
        self,
        received_message: str,
        intent_type: str | None = None,
        context: list[str] | None = None,
    ) -> None:
        messages = [
            {
                'role': 'system',
                'content': PROMPT_RESUME_AGENT_SYSTEM
            }
        ]

        if context:
            for message in context:
                messages.append({'role': 'user', 'content': message})

        messages.append({'role': 'user', 'content': received_message})

        response = self.__client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages
        )

        return response.choices[0].message.content
