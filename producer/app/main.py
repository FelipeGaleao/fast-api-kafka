from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer


class Message(BaseModel):
    text: str


class HorarioPonto(BaseModel):
    id: str
    matricula_funcionario: str
    data_hora: str
    tipo: str
    local: str
    dep_funcionario: str
    setor_funcionario: str
    unidade_funcionario: str
    empresa_funcionario: str


class ComprovanteDeMatricula(BaseModel):
    id: str
    id_aluno: str
    data_hora: str
    localizacao: str
    codigo_aluno: str

class CadastroMatricula(BaseModel):
    id: str
    id_aluno: str
    data_hora: str
    curso: str

app = FastAPI()
producer = KafkaProducer(bootstrap_servers=["kafka:9092"])


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    headers = dict(request.headers)
    user_agent = headers.get("user-agent")

    body = await request.body()

    response = await call_next(request)

    process_time = time.time() - start_time

    log_data = {
        "method": request.method,
        "path": request.url.path,
        "headers": headers,
        "user-agent": user_agent,
        "request_body": body.decode(),
        "status_code": response.status_code,
        "response_body": await response.text(),
        "process_time": process_time,
    }

    # log the data using your preferred logging library
    logger.info(log_data)

    return response


@app.post("/send")
async def send_notification(message: Message):
    try:
        producer.send("message", value=message.text.encode())
        return {"message": "Notification sent in the background"}
    except e:
        return {"message": "Notification failed to send", "error": e}


@app.post("/enviar_horario_ponto")
async def enviar_horario_ponto(horario_ponto: HorarioPonto):
    try:
        producer.send("horario_ponto", value=horario_ponto.json().encode())
        return {"message": "Horario de ponto enviado com sucesso"}
    except e:
        return {"message": "Falha ao enviar horario de ponto", "error": e}


@app.post("/comprovante_de_matricula")
async def comprovante_de_matricula(comprovante_matricula: ComprovanteDeMatricula):
    try:
        producer.send(
            "comprovante_de_matricula", value=comprovante_matricula.json().encode()
        )
        return {"message": "Comprovante de matricula enviado com sucesso"}
    except e:
        return {"message": "Falha ao enviar comprovante de matricula", "error": e}


@app.post("/cadastro_matricula")
async def cadastro_matricula(cadastro_matricula: CadastroMatricula):
    try:
        producer.send(
            "cadastro_matricula", value=cadastro_matricula.json().encode()
        )
        return {"message": "Cadastro de matricula enviado com sucesso"}
    except e:
        return {"message": "Falha ao enviar cadastro de matricula", "error": e}
