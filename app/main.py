from fastapi import FastAPI

app = FastAPI(
    title="API de Gestão de Chamados",
    description="API RESTful para gerenciamento e triagem de atendimentos ao cliente.",
    version="1.0.0"
)

@app.get("/", tags=["Status"])
def verificar_status():
    return {
        "status": "online",
        "mensagem": "API de Gestão de Chamados operando normalmente."
    }