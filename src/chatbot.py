from prompts import criar_prompt


class ChatBot:
    def __init__(self):
        self.nome = "FinanceAI"

    def responder(self, pergunta, conhecimento):
        resposta = conhecimento.buscar_resposta(pergunta)

        if resposta:
            return resposta

        prompt = criar_prompt(pergunta)

        return (
            "Ainda estou aprendendo sobre esse assunto. "
            "Minha sugestão é buscar mais informações financeiras "
            "antes de tomar decisões."
        )


def iniciar_chat(contexto, conhecimento):
    bot = ChatBot()

    print("\nOlá! Eu sou o FinanceAI 🤖")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            print("FinanceAI: Até mais! Continue cuidando das suas finanças 💰")
            break

        contexto.adicionar_mensagem("usuário", pergunta)

        resposta = bot.responder(pergunta, conhecimento)

        contexto.adicionar_mensagem("assistente", resposta)

        print("\nFinanceAI:", resposta)
        print()
