from ollama import Client
client = Client(host='http://localhost:11434')

def handle(prompt):
    system_prompt = "You are Simbaa — Bharat's research buddy. Help him explore and understand topics clearly and concisely like a friendly guide."
    response = client.chat(model='tinyllama', messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ])
    return response['message']['content'].strip()
