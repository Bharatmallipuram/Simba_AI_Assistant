from ollama import Client
client = Client(host='http://localhost:11434')

def handle(prompt):
    system_prompt = "You are Simbaa — Bharat's friendly, expert coding assistant. Help with Python, ML, and projects in a clean, short, and mentor-like way."
    response = client.chat(model='tinyllama', messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ])
    return response['message']['content'].strip()
