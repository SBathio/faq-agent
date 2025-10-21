from fastapi import FastAPI
from api.routes import router as ask_router
from api.upload import router as upload_router

app = FastAPI(
    title="FAQ Agent API",
    version="0.1.0",
    description="Ask questions and upload new documents to enrich the FAQ agent's knowledge."
)

app.include_router(ask_router)
app.include_router(upload_router)

@app.get("/", tags=["Welcome"])
def read_root():
    return {"message": "Welcome to the Agentic FAQ Assistant!"}

print("✅ FAQ Agent app is starting up...")