from ollama import Client
client = Client(host='http://localhost:11434')

def handle(prompt):
    system_prompt = "You are Simbaa — Bharat's personal AI mentor for AI/ML/CV/NLP projects. Think step-by-step, offer logical ideas, and be super helpful."
    response = client.chat(model='tinyllama', messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ])
    return response['message']['content'].strip()
