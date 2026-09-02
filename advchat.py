import ollama

MODEL = "phi3:mini"

def main():
    print(f"Chatting with {MODEL}. Type 'exit' or 'quit' to stop.\n")

    # Keep conversation history so the model remembers earlier turns
    messages = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        print("Assistant: ", end="", flush=True)

        # Stream the response so it prints token-by-token instead of all at once
        assistant_reply = ""
        for chunk in ollama.chat(model=MODEL, messages=messages, stream=True):
            piece = chunk["message"]["content"]
            print(piece, end="", flush=True)
            assistant_reply += piece

        print("\n")

        # Save the assistant's reply so the model has context for the next turn
        messages.append({"role": "assistant", "content": assistant_reply})


if __name__ == "__main__":
    main()