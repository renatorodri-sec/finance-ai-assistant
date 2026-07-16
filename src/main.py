from chatbot import iniciar_chat


def main():
    print("=" * 50)
    print("💰 FinanceAI - Assistente Virtual Inteligente")
    print("=" * 50)

    iniciar_chat()


if __name__ == "__main__":
    main()
from chatbot import ChatBot
from contexto import Contexto
from conhecimento import Conhecimento
from prompts import criar_prompt
from calculos import *
from utils import *
bot = ChatBot()
contexto = Contexto()
