


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from voice_router import router as voice_router
from KALUii_Logic import pet_bot_reply




# FASTAPI INIT:-----------
   
    #Render runs: uvicorn main:app --host 0.0.0.0 --port 8000
                      
    # only main.py app runs

    # voice_router.py's app is NEVER STARTED 💀


app = FastAPI()
app.include_router(voice_router)  # Include the voice router for /voice_chat endpoint

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# REQUEST MODEL


class ChatRequest(BaseModel):
    message: str

# API ROUTE


@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        reply = pet_bot_reply(request.message)
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}
