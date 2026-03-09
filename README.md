<h1 align="center">KALUii – AI Companion for My Profile</h1>

<p align="center">
An <b>RAG-Retrieval Augmented Generation</b> based AI personality bot that answers questions about me in a playful way.
</p>

<hr>

<h2>About</h2>

<p>
This PetBot is a small <b>AI personality companion</b> designed to represent me interactively.
Instead of reading a static bio, visitors can <b>chat with an AI companion</b> that knows about my interests, skills, and personality.
</p>

<p>
The bot behaves like a playful <b>“pet” personality</b> attached to its owner and responds with short, witty answers.
</p>

<hr>

<h2>How It Works</h2>

<ul>
<li>Personal information is stored in a text file <code>personal_seed.txt</code></li>
<li>The text is split into chunks</li>
<li>Chunks are embedded using OpenAI embeddings</li>
<li>A FAISS vector database stores these embeddings</li>
</ul>

<p><b>When a user asks a question:</b></p>

<ol>
<li>Relevant context is retrieved from FAISS</li>
<li>The context is inserted into a personality-driven prompt</li>
<li>The LLM generates a short response</li>
</ol>

<p>The backend is exposed through a <b>FastAPI API endpoint</b>.</p>

<hr>

<h2>System Flow</h2>

<pre>
User Question
      │
      ▼
FastAPI API
      │
      ▼
PetBot Logic
 ├─ Context retrieval (FAISS)
 └─ LLM generation
      │
      ▼
AI Response
</pre>

<hr>

<h2>Tech Stack</h2>

<ul>
<li>Python</li>
<li>FastAPI</li>
<li>LangChain</li>
<li>FAISS (Vector Search)</li>
<li>OpenRouter API</li>
<li>GPT-4o-mini</li>
<li>OpenAI Embeddings (<code>text-embedding-3-small</code>)</li>
</ul>

<hr>

<h2>API</h2>

<h3>POST /chat</h3>

<p><b>Request</b></p>

<pre>
{
  "message": "Is he loyal?"
}
</pre>

<p><b>Response</b></p>

<pre>
{
  "reply": "Yes — once he chooses… like he chose me."
}
</pre>

<hr>

<h2>⭐Future Upgrades⭐</h2>

<ul>
<li>Conversation context memory</li>
<li>Voice interaction (speech input/output)</li>
</ul>

<hr>

<p align="center">
Built as a small project exploring <b>AI-powered interactive systems</b>.
</p>
