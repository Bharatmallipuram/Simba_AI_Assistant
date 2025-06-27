import yaml
import json
import os

from dotenv import load_dotenv
from ollama import Client

from skills import coding, research, writing, project_helper

# === Load Config ===
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# === Load Memory (Optional) ===
try:
    with open("memory.json", "r") as f:
        content = f.read().strip()
        memory = json.loads(content) if content else []
except (FileNotFoundError, json.JSONDecodeError):
    memory = []

# === Connect to Ollama (local LLM) ===
client = Client(host='http://localhost:11434')
llm_model = config.get("model", "tinyllama")

# === System Prompt for fallback ===
system_prompt = f"{config['personality']['role']} {config['personality']['style']}"

# === Simbaa Fallback LLM Handler ===
def call_simbaa(prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    response = client.chat(model=llm_model, messages=messages)
    return response['message']['content'].strip()

# === Task Router ===
def handle_task(user_input):
    task = user_input.lower()

    if "code" in task or "debug" in task:
        return coding.handle(user_input)
    elif "paper" in task or "research" in task:
        return research.handle(user_input)
    elif "email" in task or "write" in task or "report" in task:
        return writing.handle(user_input)
    elif "project" in task or "idea" in task:
        return project_helper.handle(user_input)
    else:
        return call_simbaa(user_input)

# === Main Loop ===
def main():
    print("🦁 Hello! I’m Simbaa, your personal AI sidekick.\nAsk me anything: code, research, writing, or project help!\n(Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("🦁 Simbaa: See you soon, Bharat! Keep building. 🚀")
            break

        reply = handle_task(user_input)
        print("Simbaa 🦁:", reply)

        # Save to memory
        memory.append({"user": user_input, "assistant": reply})
        with open("memory.json", "w") as f:
            json.dump(memory, f, indent=2)

if __name__ == "__main__":
    main()
