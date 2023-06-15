from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer


class Message(BaseModel):
    text: str

class HorarioPonto(BaseModel):
    id: str
    id_funcionario: str
    data_hora: str
    tipo: str
    localizacao: str

app = FastAPI()
producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

@app.post("/send")
async def send_notification(message: Message):
    try:
        producer.send('message', value=message.text.encode())
        return {"message": "Notification sent in the background"}
    except e: 
        return {"message": "Notification failed to send", "error": e}

@app.post('/enviar_horario_ponto')
async def enviar_horario_ponto(horario_ponto: HorarioPonto):
    try:
        producer.send('horario_ponto', value=horario_ponto.json().encode())
        return {"message": "Horario de ponto enviado com sucesso"}
    except e: 
        return {"message": "Falha ao enviar horario de ponto", "error": e}