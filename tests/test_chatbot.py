import sys
import os

# Permite importar os arquivos da pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from chatbot import ChatBot
from conhecimento import Conhecimento


def test_resposta_economizar():
    bot = ChatBot()
    conhecimento = Conhecimento()

    resposta = bot.responder("Como economizar dinheiro?", conhecimento)

    assert resposta is not None
    assert "economizar" in resposta.lower() or "organize seus gastos" in resposta.lower()


def test_resposta_juros():
    bot = ChatBot()
    conhecimento = Conhecimento()

    resposta = bot.responder("O que são juros?", conhecimento)

    assert "juros" in resposta.lower()


def test_resposta_desconhecida():
    bot = ChatBot()
    conhecimento = Conhecimento()

    resposta = bot.responder("Quem ganhou a Copa do Mundo de 1970?", conhecimento)

    assert "ainda estou aprendendo" in resposta.lower()
