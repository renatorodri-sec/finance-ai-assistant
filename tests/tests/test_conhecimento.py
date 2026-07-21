import sys
import os

# Permite importar os arquivos da pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from conhecimento import Conhecimento


def test_buscar_resposta_economizar():
    conhecimento = Conhecimento()

    resposta = conhecimento.buscar_resposta("Como posso economizar dinheiro?")

    assert resposta is not None
    assert "organize seus gastos" in resposta.lower()


def test_buscar_resposta_juros():
    conhecimento = Conhecimento()

    resposta = conhecimento.buscar_resposta("O que são juros?")

    assert resposta is not None
    assert "juros" in resposta.lower()


def test_buscar_resposta_inexistente():
    conhecimento = Conhecimento()

    resposta = conhecimento.buscar_resposta("Qual é a capital do Brasil?")

    assert resposta is None
