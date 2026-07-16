def calcular_juros_simples(capital, taxa, tempo):
    """
    Calcula o montante utilizando juros simples.

    Fórmula:
    M = C * (1 + i * t)
    """

    montante = capital * (1 + (taxa / 100) * tempo)

    return round(montante, 2)


def calcular_juros_compostos(capital, taxa, tempo):
    """
    Calcula o montante utilizando juros compostos.

    Fórmula:
    M = C * (1 + i) ** t
    """

    montante = capital * ((1 + (taxa / 100)) ** tempo)

    return round(montante, 2)


def simular_investimento(valor_inicial, aporte_mensal, taxa, meses):
    """
    Simula um investimento com aportes mensais.
    """

    saldo = valor_inicial

    for _ in range(meses):
        saldo *= (1 + taxa / 100)
        saldo += aporte_mensal

    return round(saldo, 2)
