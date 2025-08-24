from src.llm_call import llm_call

def main():
    print("LLM Chat - Digite 'quit' para sair\n")
    
    while True:
        try:
            # Receber input do usuário
            user_input = input("Você: ").strip()
            
            # Verificar se quer sair
            if user_input.lower() in ['quit', 'exit', 'sair']:
                print("Tchau! 👋")
                break
            
            # Pular inputs vazios
            if not user_input:
                continue
            
            # Chamar o LLM
            response = llm_call(user_input)
            print(f"LLM: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nTchau! 👋")
            break
        except Exception as e:
            print(f"Erro: {e}\n")

if __name__ == "__main__":
    main()