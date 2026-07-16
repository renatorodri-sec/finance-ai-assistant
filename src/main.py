from chatbot import iniciar_chat
from contexto import Contexto
from conhecimento import Conhecimento
from prompts import criar_prompt
from calculos import *
from utils import *


def main():

    print("=" * 50)
    print("💰 FinanceAI - Assistente Virtual Inteligente")
    print("=" * 50)

    contexto = Contexto()
    conhecimento = Conhecimento()

    iniciar_chat(contexto, conhecimento)


if __name__ == "__main__":
    main()
