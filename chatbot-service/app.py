from fastapi import FastAPI, Request

from services.evolution import Evolution
from services.agent import Agent

from models.conversation_history import ConversationHistoryModel
from utils.kind_message import MessageType
from utils.messages import PROMPT_WELCOME_MESSAGE


app = FastAPI()


@app.post("/chatbot/assistant")
async def root(request: Request):
    data = await request.json()

    chat_id = data['data']['key']['remoteJid']

    is_group_message = '@g.us' in chat_id

    if 'data' not in data:
        return {
            'status': 'Success',
            'message': 'Format unknown'
        }

    from_me = data['data']['key']['fromMe']

    if is_group_message or from_me:
        return {'status': 'Success', 'message': 'Message ignored'}

    author = data['data']['pushName']
    messageType = data['data']['messageType']

    if not messageType == 'conversation':
        return {'status': 'Success', 'message': 'Invalid message format'}

    message = data['data']['message']['conversation']

    chat_history = ConversationHistoryModel.get_messages_by_chat_id(
        chat_id=chat_id
    )

    context_messages = [item.get("message") for item in chat_history] if chat_history else []

    agent = Agent()
    evolution = Evolution()

    detection_result = agent.detect_type_message(message=message)

    output_prompt = detection_result.get('output_prompt', None)
    message_type = detection_result.get('type', MessageType.UNKNOWN.value)
    filters = detection_result.get('filters', None)

    if message_type == MessageType.GREETING.value:
        response_text = PROMPT_WELCOME_MESSAGE.format(author)

    elif len(chat_history) == 0 and message_type == MessageType.UNKNOWN.value:

        response_text = PROMPT_WELCOME_MESSAGE.format(author)

    else:
        context_data = {
            'type': message_type,
            'filters': filters,
            'output_prompt': output_prompt,
            'context_messages': context_messages
        }

        response_text = agent.invoke(message=message, data=context_data)

    ConversationHistoryModel.create_message(
        chat_id=chat_id,
        sender=author,
        message=message
    )

    ConversationHistoryModel.create_message(
        chat_id=chat_id,
        sender="agent",
        message=response_text
    )

    evolution.send_message(
        message=response_text,
        number_contact=chat_id
    )

    return {
        'status': 'Success',
        'client_message': message,
        'response_text': response_text
    }
