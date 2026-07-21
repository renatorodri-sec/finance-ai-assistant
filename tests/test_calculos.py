
import sys
import os

# Permite importar os arquivos da pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from calculos import (
    calcular_juros_simples,
    calcular_juros_compostos,
    simular_investimento,
)


def test_calcular_juros_simples():
    resultado = calcular_juros_simples(1000, 10, 2)
    assert resultado == 1200.0


def test_calcular_juros_compostos():
    resultado = calcular_juros_compostos(1000, 10, 2)
    assert resultado == 1210.0


def test_simular_investimento():
    resultado = simular_investimento(1000, 100, 1, 12)
    assert resultado > 2200
