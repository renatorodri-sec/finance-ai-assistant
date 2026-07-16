def limpar_texto(texto):
    """
    Remove espaços extras e deixa o texto padronizado.
    """
    return texto.strip().lower()


def formatar_moeda(valor):
    """
    Formata valores para padrão monetário brasileiro.
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def mostrar_separador():
    """
    Exibe uma linha para organizar a interface.
    """
    print("=" * 50)


def validar_numero(valor):
    """
    Verifica se o valor informado é um número.
    """
    try:
        return float(valor)
    except ValueError:
        return None
