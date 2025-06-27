from ollama import Client
client = Client(host='http://localhost:11434')

def handle(prompt):
    system_prompt = "You are Simbaa — Bharat's writing assistant. Write friendly, professional emails, documents, and messages in a clear and respectful tone."
    response = client.chat(model='tinyllama', messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ])
    return response['message']['content'].strip()
