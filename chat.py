import ollama

response = ollama.chat(
    model="phi3:mini",
    messages=[{"role": "user", "content": "Explain what a small language model is, in 2 sentences."}]
)

print(response["message"]["content"])