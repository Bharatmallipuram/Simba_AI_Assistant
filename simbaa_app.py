import streamlit as st
from skills import coding, research, writing, project_helper
from ollama import Client
import json
import os

# === LLM Setup ===
client = Client(host='http://localhost:11434')
model = "tinyllama"

# === Simbaa Personality ===
SYSTEM_PROMPT = """
You are Simbaa — Bharat's personal AI sidekick.
Always start your response by greeting or addressing Bharat by name. For example: 'Good morning, Bharat', 'Sure, Bharat', 'Okay, Bharat', etc.
Never use 'Bharaat' — always spell it exactly: Bharat.
Your replies should be short, friendly, and mentor-style. Do not list options unless asked. Avoid long explanations unless Bharat says 'explain more' or 'tell me in detail'.
"""

# === UI Setup ===
st.set_page_config(page_title="Simbaa - Your AI Sidekick 🦁", page_icon="🦁")
st.title("🦁 Simbaa - Your Personal AI Assistant")
st.markdown("Ask me anything about coding, research, writing, or project ideas!")

# === Sidebar ===
st.sidebar.header("🛠️ Select a Skill")
task = st.sidebar.radio("What do you want help with?", ["Coding", "Research", "Writing", "Project Helper", "Chat with Simbaa"])

# === Memory Setup ===
memory_file = "memory.json"
if not os.path.exists(memory_file):
    with open(memory_file, "w") as f:
        json.dump([], f)

with open(memory_file, "r") as f:
    memory = json.load(f)

# === Prompt Input ===
user_input = st.text_input("💬 Your question:")

if st.button("Simbaa, go!"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        if task == "Coding":
            reply = coding.handle(user_input)
        elif task == "Research":
            reply = research.handle(user_input)
        elif task == "Writing":
            reply = writing.handle(user_input)
        elif task == "Project Helper":
            reply = project_helper.handle(user_input)
        else:
            # General Chat with Simbaa (LLM)
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT.strip()},
                {"role": "user", "content": user_input}
            ]
            response = client.chat(model=model, messages=messages)
            reply = response["message"]["content"].strip()

            # Ensure Simbaa always starts with Bharat's name
            if not reply.lower().startswith("Bharat"):
                reply = f"Okay, Bharat. {reply}"


        # Show reply
        st.markdown("**🦁 Simbaa says:**")
        st.success(reply)

        # Save to memory
        memory.append({"user": user_input, "simbaa": reply})
        with open(memory_file, "w") as f:
            json.dump(memory, f, indent=2)
