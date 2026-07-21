import sys
import os

# Permite importar os arquivos da pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from contexto import Contexto


def test_adicionar_mensagem():
    contexto = Contexto()

    contexto.adicionar_mensagem("Renato", "Olá!")

    historico = contexto.obter_historico()

    assert len(historico) == 1
    assert historico[0]["usuario"] == "Renato"
    assert historico[0]["mensagem"] == "Olá!"


def test_limpar_historico():
    contexto = Contexto()

    contexto.adicionar_mensagem("Renato", "Teste")
    contexto.limpar()

    assert contexto.obter_historico() == []
