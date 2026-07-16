class Conhecimento:
    def __init__(self):
        self.base_conhecimento = {
            "economizar": "Para economizar dinheiro, organize seus gastos, crie um orçamento mensal e evite despesas desnecessárias.",
            
            "investir": "Antes de investir, monte uma reserva de emergência e conheça seu perfil de investidor. Existem opções como renda fixa e fundos de investimento.",
            
            "juros": "Juros são valores cobrados pelo uso de dinheiro emprestado ou ganhos sobre um investimento. Nos juros compostos, os juros geram novos juros.",
            
            "cartao": "Use o cartão de crédito com planejamento. Evite gastar mais do que pode pagar e acompanhe sempre sua fatura.",
            
            "orcamento": "Um orçamento financeiro ajuda a controlar entradas e saídas de dinheiro, permitindo planejar melhor seus objetivos.",
            
            "dividas": "Para organizar dívidas, liste todos os débitos, priorize os mais caros e crie um plano de pagamento."
        }

    def buscar_resposta(self, pergunta):
        pergunta = pergunta.lower()

        for palavra, resposta in self.base_conhecimento.items():
            if palavra in pergunta:
                return resposta

        return None
