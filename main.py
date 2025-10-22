from fastapi import FastAPI

from api.routes import router as ask_router
from api.upload import router as upload_router
# from agent.faq_agent import run_agent  # ✅ Import the LangChain agent

app = FastAPI(
    title="Agentic FAQ Assistant API",
    version="1.0.0",
    description="A LangChain-powered Agent system to answer FAQ questions and handle document uploads."
)

# Attach routers
app.include_router(ask_router, prefix="/ask", tags=["FAQ Agent"])
app.include_router(upload_router, prefix="/upload", tags=["File Upload"])

@app.get("/", tags=["Welcome"])
def read_root():
    return {"message": "✅ Welcome to the Agentic FAQ Assistant API!"}

# Optional: Print agent tools and setup summary
print("✅ FAQ Agent app is starting up...")