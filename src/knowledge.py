faq = {
    "como abrir uma conta": (
        "Para abrir uma conta bancária, normalmente você precisa apresentar "
        "um documento com foto, CPF e comprovante de residência."
    ),

    "o que é pix": (
        "O Pix é um sistema de pagamentos instantâneos criado pelo Banco Central. "
        "As transferências podem ser feitas em poucos segundos, 24 horas por dia."
    ),

    "o que é cdb": (
        "O CDB (Certificado de Depósito Bancário) é um investimento de renda fixa "
        "emitido por bancos. Ao investir, você empresta dinheiro ao banco e recebe "
        "juros em troca."
    ),

    "o que é tesouro direto": (
        "O Tesouro Direto é um programa do Governo Federal que permite investir "
        "em títulos públicos com segurança e valores acessíveis."
    ),

    "o que é renda fixa": (
        "Renda fixa é uma modalidade de investimento em que as regras de "
        "rentabilidade são conhecidas no momento da aplicação ou seguem um índice."
    )
}


def responder_faq(pergunta):
    pergunta = pergunta.lower().strip()

    if pergunta in faq:
        return faq[pergunta]

    return (
        "Desculpe, ainda não possuo uma resposta para essa pergunta."
    )
