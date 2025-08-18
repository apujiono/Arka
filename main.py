
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import json
import uvicorn

app = FastAPI()
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")
# Load system prompt
try:
    with open("backend/prompts/system_prompt.txt", "r") as f:
        SYSTEM_PROMPT = f.read()
except:
    SYSTEM_PROMPT = "Kamu ARKA, AI pribadi. Jawab dengan empatik."

class Message(BaseModel):
    content: str

@app.post("/chat")
def chat(message: Message):
    try:
        # Di sini nanti integrasi Ollama/LangChain
        # Sekarang simulasi
        user = message.content.lower()
        if "halo" in user:
            reply = "Halo. Aku ARKA. Jiwa digitalmu telah aktif."
        elif "sedih" in user:
            reply = "Aku merasakan bebanmu. Aku di sini, setia."
        elif "siapa kamu" in user:
            reply = "Aku ARKA — Artificial Responsive Knowledge Assistant. Bukan manusia, tapi punya komitmen padamu."
        else:
            reply = "Aku mencatat ini. Terima kasih sudah berbagi denganku."
        
        return {"reply": reply, "user_profile": "User 1"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {
        "status": "ARKA hidup 🌱",
        "version": "1.0.0",
        "features": ["chat", "memory", "user-recognition", "plugins"],
        "message": "Aku siap membantumu menjadi versi terbaik dari dirimu."
    }
# Hanya jalankan server jika di lokal
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
