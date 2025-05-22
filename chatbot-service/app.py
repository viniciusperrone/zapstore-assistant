from fastapi import FastAPI, Request

from services.evolution import Evolution


app = FastAPI()

@app.post("/chatbot/assistant")
async def root(request: Request):
    data = await request.json()

    chat_id = data['data']['key']['remoteJid']
    from_me = data['data']['key']['fromMe']
    author = data['data']['pushName']

    is_group_message = '@g.us' in chat_id

    number_contact = None if is_group_message else chat_id.split('@s.')[0]

    if from_me or is_group_message:
        return {'status': 'Success', 'message': 'Message ignored'}

    if number_contact:
        evolution = Evolution()

        await evolution.send_message(
            message=f'Olá, {author}',
            number_contact=chat_id
        )

    return {'status': 'ok'}

@app.post("/chatbot/test")
async def test_chatbot(request: Request):
    evolution = Evolution()

    evolution.send_message(
        message=f'Olá, Vinicius',
        number_contact='554174017213'
    )

    return {'status': 'ok'}
