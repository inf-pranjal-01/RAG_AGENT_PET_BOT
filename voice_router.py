# if you dont know much about web side, comments throughout the code will help you understand.

 



from fastapi import APIRouter, UploadFile, File

from voice_module import voice_to_text, text_to_voice_sexy
from KALUii_Logic import pet_bot_reply
from fastapi.responses import JSONResponse
import json



# routing to voice endpoint as Two FastAPI() apps = two completely separate servers
# frontend calls render.com/voice-chat → which app handles it? 💀 main has app too!
router = APIRouter()


# /chat (text):
# Even if sync, 1-2 seconds blocking
# Not a big deal for most cases ✅

# /voice-chat:
# 5-8 seconds blocking per user
# 3 users simultaneously = 
# User 2 waits 8 seconds
# User 3 waits 16 seconds 💀
# thats why async is needed

@router.post("/voice_chat")
async def voice_chat(audio: UploadFile = File(...)):
          audio_in = await audio.read()
          text_version=voice_to_text(audio_in, audio.filename)  #filename is just for the API, not actually used to read file
          reply_in_text = pet_bot_reply(text_version)
          reply_in_voice = text_to_voice_sexy(reply_in_text)

          sexy_voice_response = {
              "voice": reply_in_voice ,
              "text": reply_in_text , }
                                    
                                    
          

          
          return JSONResponse(sexy_voice_response)
 