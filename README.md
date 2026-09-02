These are the steps that I did to start the project.
Step 1 — Check your laptop's capacity
RAM: 8GB minimum, 16GB comfortable. Small models (0.5B–3B params) run fine on CPU-only laptops.
GPU: optional. Not required — SLMs are specifically small enough to run on CPU, just slower.
Disk: 2–5GB free per model.
Step 2 — Install Ollama

Ollama handles downloading, quantizing, and serving the model as a local API — it's the least fiddly way to run an SLM.

Go to https://ollama.com → download for your OS (Windows/Mac/Linux) → install like any app.
Verify it worked by opening a terminal and running:
ollama --version
Step 3 — Pull and run a small model

In a terminal:

ollama run phi3:mini

This downloads (~2.3GB) and drops you into an interactive chat. Try it, then type /bye to exit.

Other good SLM options to try the same way:

ollama run qwen2.5:1.5b
ollama run llama3.2:3b
ollama run gemma2:2b
Step 4 — Set up VS Code
Install VS Code from https://code.visualstudio.com if you don't have it.
Install the Python extension (Microsoft) from the Extensions panel.
Install Python itself if needed (python.org, or winget install Python.Python.3.12 on Windows, brew install python on Mac).
Step 5 — Create a project and call the model from Python

Open a folder in VS Code, then in the integrated terminal (Ctrl+`):

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install ollama

Create chat.py:

python
import ollama

response = ollama.chat(
    model="phi3:mini",
    messages=[{"role": "user", "content": "Explain what a small language model is, in 2 sentences."}]
)

print(response["message"]["content"])

Run it in VS Code (Run ▶ button, or python chat.py in the terminal). Ollama's local server (it runs on localhost:11434 automatically after install) handles the actual inference.
