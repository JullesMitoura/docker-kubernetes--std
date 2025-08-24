from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.llm_call import llm_call
import uvicorn

app = FastAPI(
    title="LLM Chat API",
    description="API para chat com LLM",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "LLM Chat API está funcionando! 🚀"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Endpoint principal do chat
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Validar input
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Mensagem não pode estar vazia")
        
        # Chamar LLM
        llm_response = llm_call(request.message.strip())
        
        return ChatResponse(response=llm_response)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )