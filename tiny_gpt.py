from ollama import Client

client = Client(host='http://localhost:11434')

def ask(prompt):
    response = client.chat(model='tinyllama', messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content'].strip()

# Example use
print(ask("Explain reinforcement learning like I'm 15"))
