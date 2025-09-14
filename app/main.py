from fastapi import FastAPI
from pydantic import BaseModel

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="API Genérica em Contêiner",
    description="Um template para APIs containerizadas com FastAPI e Azure Container Apps.",
    version="1.0.0"
)

# Define um modelo de dados para a requisição POST usando Pydantic
class GreetingRequest(BaseModel):
    name: str

# Endpoint raiz (GET) para verificação de saúde (health check)
@app.get("/", tags=["Health Check"])
def read_root():
    """Retorna uma mensagem simples para indicar que a API está no ar."""
    return {"status": "ok", "message": "Bem-vindo à API!"}

# Endpoint principal (POST) que recebe um nome e retorna uma saudação
@app.post("/api/hello", tags=["Greetings"])
def create_greeting(request: GreetingRequest):
    """
    Recebe um nome em um corpo JSON e retorna uma saudação personalizada.
    """
    return {"message": f"Olá, {request.name}! Sua requisição POST foi recebida."}

# Endpoint alternativo (GET) com parâmetro na URL
@app.get("/api/hello", tags=["Greetings"])
def get_greeting(name: str):
    """
    Recebe um nome como parâmetro de consulta na URL e retorna uma saudação.
    """
    return {"message": f"Olá, {name}! Sua requisição GET foi recebida."}
