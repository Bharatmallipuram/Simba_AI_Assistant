# 🦁 Simbaa - Your Personal AI Sidekick

Simbaa is a friendly, expert-level AI assistant designed especially for **Bharat** to help with coding, research, writing, project planning, and more — all through a sleek local interface using **Streamlit** and **TinyLlama** running on **Ollama**.

---

## ✨ Features

- 🧠 Personalized replies with mentor-style guidance
- 💬 Supports tasks like:
  - Coding assistance
  - Research help
  - Report or email writing
  - Project ideas & support
- 🖥️ Streamlit-based interactive UI
- 💾 Persistent memory (via `memory.json`)
- 🗣️ (Coming soon!) Voice input/output

---

## ⚙️ Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) (for running local LLMs like TinyLlama)
- Streamlit
- `dotenv`, `json`, `yaml`

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Bharatmallipuram/Simba_AI_Assistant.git
cd Simba_AI_Assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Ollama and pull the model
```bash
ollama run tinyllama
```
### 4. Create .env file
```bash
# .env
OLLAMA_HOST=http://localhost:11434
```
### 🚀 Launch Simbaa (UI)
```bash
streamlit run simbaa_app.py
```
Then open your browser to:
👉 http://localhost:8501

### 📂 Project Structure
```bash
Simba_AI_Assistant/
├── simbaa_app.py          # Streamlit UI logic
├── skills/                # Task modules (coding, research, etc.)
├── memory.json            # Saves chat history
├── .env                   # Local secrets (ignored from Git)
├── .gitignore
└── README.md
```

### 🙏 Credits
Streamlit
Ollama
TinyLlama Model

### 🐾 Made with ❤️ by Bharat and Simbaa

