import requests

# URL da sua API
API_URL = "https://mdev-std.azurewebsites.net"

def chat(message):
    """Envia mensagem para a API"""
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={"message": message}
        )
        print(f"📊 Status Code: {response.status_code}")
        print(f"📋 Response Text: {response.text}")
        print(f"🔗 Headers: {response.headers}")
        
        response.raise_for_status()  # Lança erro se status HTTP for erro
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return "Erro na API"
    except KeyError as e:
        print(f"❌ Erro no formato da resposta: {e}")
        print(f"📋 Resposta recebida: {response.text}")
        return "Erro no formato da resposta"
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return "Erro inesperado"

# Teste simples
if __name__ == "__main__":
    # Teste 1
    resposta = chat("Olá!")
    print(f"🤖 {resposta}")
    
    # Teste 2
    resposta = chat("Como você está?")
    print(f"🤖 {resposta}")
    
    # Chat interativo
    print("\n💬 Digite suas mensagens (ou 'quit' para sair):")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == 'quit':
            break
        resposta = chat(pergunta)
        print(f"🤖 {resposta}\n")