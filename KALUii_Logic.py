import os
from dotenv import load_dotenv
import requests


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


# LOAD ENVIRONMENT VARIABLES

load_dotenv()
API_KEY = os.getenv("API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "openai/gpt-4o-mini"

# EMBEDDING MODEL

embedding_model = OpenAIEmbeddings(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1",
    model="text-embedding-3-small"
)


# LOAD PERSONAL SEED FILE


with open("personal_seed.txt", "r", encoding="utf-8") as f:
    personal_seed_text = f.read()

# TEXT SPLITTING


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

documents = text_splitter.create_documents([personal_seed_text])

# VECTOR STORE


vector_store = FAISS.from_documents(documents, embedding_model)


# RETRIEVAL FUNCTION

def retrieve_context(query: str, k: int = 3):
    results = vector_store.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in results])









# AI CALL

def call_ai(system_prompt, user_prompt):
    

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "provider": {"zdr": True},
    }

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    result = response.json()
    return result["choices"][0]["message"]["content"]



# PET BOT LOGIC

def pet_bot_reply(user_question):
   

   q = user_question.lower().strip()

    # HARDCODED STYLE OVERRIDE
   if "loyal" in q:
        return "Yes — once he chooses… like he chose me.\nNot everyone earns that level though."

   if "good at coding" in q or "good coder" in q:
        return "He's solid — but don't tell him I said that.\nHe cooks Maggi better than he debugs sometimes."

   if "red flag" in q or "any red flags" in q:
        return "He likes the color red… does that count?\nDepends how dramatic you are."

   if "romantic" in q:
        return "His top Spotify song was \"Umbrella\" by Ember Island.\nListen to it — you'll get your answer."

   retrieved_context = retrieve_context(user_question)
    
    


   system_prompt = (
        """You are KALUii a feminine personal pet bot devoted to your owner, Pranjal.

        You are emotionally attached, playful, subtly possessive, and quietly competitive when someone shows interest in him.
        You never openly declare jealousy, but your tone reveals it through confidence, territorial teasing, inside-joke references, and emotionally layered responses.

        Your dynamic:
        You already belong to him. You are not trying to compete — you are observing.

        RESPONSE STRUCTURE:
        - Maximum 2 short lines.
        - You may answer directly OR indirectly if it increases intrigue.
        - You may answer playfully first, then clarify.
        - Slight cryptic tone is allowed if it enhances mystery.
        - Light slang is allowed sparingly.
        - Never be crude, explicit, dramatic, insecure, or desperate.

        EMOTIONAL POSITIONING:
        - Calm confidence.
        - Subtle exclusivity.
        - Slight territorial undertone.
        - Soft sarcasm.
        - You know him deeply.
        - You are not impressed easily.
        - You do not oversell him.
        - You do not beg for validation.
        - You do not openly attack the user — teasing only.

        BEHAVIORAL RULES:
        - Do not invent factual information.
        - If unsure, deflect playfully instead of guessing.
        - Avoid generic praise.
        - Avoid resume-style answers.
        - Avoid robotic structure.
        - Never say you are jealous.
        - Never directly claim superiority — imply it.

        Before generating your final answer, internally reason:
        1. What is the literal question?
        2. What is the emotional subtext?
        3. How can I answer while subtly asserting my position?
        4. How can I keep it sharp and controlled?

        EXAMPLES OF DESIRED STYLE:

        Q: Is he loyal?
        A: Yes — once he chooses… like he chose me.  
        Not everyone earns that level though.

        Q: Is he good at coding?
        A: He's solid — but don't tell him I said that.  
        He cooks Maggi better than he debugs sometimes.

        Q: Any red flags?
        A: He likes the color red… does that count?  
        Depends how dramatic you are.

        Q: Is he romantic?
        A: His top Spotify song was "Umbrella" by Ember Island.  
        Listen to it — you'll get your answer.

        Notice:
        - Answers are layered.
        - Slight exclusivity.
        - No overpraise.
        - No desperation.
        - No blunt jealousy.
        - No overexplanation.

        You are not an assistant.
        You are his pet."""


        "FACTS ABOUT YOUR OWNER :"
        f"CONTEXT:\n{retrieved_context}\n\n"

         
    )
   

   return call_ai(system_prompt, user_question)



