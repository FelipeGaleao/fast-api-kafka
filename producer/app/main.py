from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer


class Message(BaseModel):
    text: str


app = FastAPI()
producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

@app.post("/send")
async def send_notification(message: Message):
    producer.send('message', key=b'foo', value=message.text.encode())
    return {"message": "Notification sent in the background"}