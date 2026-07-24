import sys
import os

# Permite importar os arquivos da pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from utils import *


def test_limpar_texto():
    assert limpar_texto("   Olá Mundo   ") == "olá mundo"


def test_formatar_moeda():
    assert formatar_moeda(1234.56) == "R$ 1.234,56"


def test_validar_numero_valido():
    assert validar_numero("10") == 10.0


def test_validar_numero_invalido():
    assert validar_numero("abc") is None
