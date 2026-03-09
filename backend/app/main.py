from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routes import generate, knowledge

# Create DB tables
Base.metadata.create_all(bind=engine)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Writing Agent API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In development, allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(generate.router, prefix="/api")
app.include_router(knowledge.router, prefix="/api/knowledge", tags=["knowledge"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
