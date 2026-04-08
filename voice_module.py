
# refer to Groq's and Google tts docs for more details on the functions below

import os
import base64
from groq import Groq

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play


load_dotenv()

# if os.path.exists("Rag_Agent_google_TTS-KEY-API.json"):
#     # Local development
#     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Rag_Agent_google_TTS-KEY-API.json"
# else:
#     # Production (Render.com)
#     creds_base64 = os.getenv("GOOGLE_CREDENTIALS_BASE64")
#     creds_json = base64.b64decode(creds_base64).decode("utf-8")    # Converting base64 string back to json string at runtime
    
    
#     with open("/tmp/google-creds.json", "w") as f:
#         f.write(creds_json)                                        # direct decoded json needed so , NO - json.dump(creds_json, f)
    
#     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/tmp/google-creds.json"



groq_client = Groq(api_key=os.getenv("groq_api_key"))


def voice_to_text(audio_bytes, filename):
 
    transcript = groq_client.audio.transcriptions.create(
    model="whisper-large-v3",
    file=(filename, audio_bytes, "audio/webm"),
             )
    return transcript.text








def text_to_voice_sexy(reply):
    
    
    client = ElevenLabs(
    api_key=os.getenv("ELEVEN_LABS_KALUii")

    )

    audio = client.text_to_speech.convert(
    text={reply},
    voice_id="kPzsL2i3teMYv0FxEYQ6",  # KALUii's voice ID
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
    )

    
    # bytes → base64 bytes → string (so it can be sent in JSON)
    audio_base64 = base64.b64encode(audio).decode("utf-8")   
    return audio_base64









#   ***   ***
#  ***** *****
#  ***********
#   *********     FOR YOU ~
#    *******       
#     *****
#      ***
#       *
# Developer_freedom