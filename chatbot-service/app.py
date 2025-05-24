from fastapi import FastAPI, Request

from services.evolution import Evolution
from services.agent import Agent

from models.conversation_history import ConversationHistoryModel
from utils.kind_message import MessageType


app = FastAPI()

@app.post("/chatbot/assistant")
async def root(request: Request):
    data = await request.json()

    chat_id = data['data']['key']['remoteJid']

    is_group_message = '@g.us' in chat_id

    if not 'data' in data:
        return {'status': 'Success', 'message': 'Format unknown'}

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
    custom_prompt = detection_result.get('output')
    message_type = detection_result.get('type', MessageType.UNKNOWN)

    if message_type == MessageType.UNKNOWN:
        response_text = "Desculpe, não entendi sua mensagem. Você pode reformular?"
    elif message_type == MessageType.FIRST_INTERACTION:
        response_text = "Olá! Sou o assistente virtual da ZapStore. Posso te ajudar com nossos produtos!"
    else:
        response_text = agent.invoke(
            received_message=custom_prompt or message,
            context=context_messages
        )

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

    return {'status': 'Success', 'message': 'Message processed successfully'}
