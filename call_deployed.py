import requests

API_URL = "https://mdev-std.azurewebsites.net"

def chat(message):
    try:
        response = requests.post(f"{API_URL}/chat", json={"message": message})
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Erro: {e}"

if __name__ == "__main__":
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == 'quit':
            break
        print(f"Bot: {chat(pergunta)}")