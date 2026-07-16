def create_prompt(question, context=""):
    prompt = f"""
Você é o Finance AI Assistant, um assistente virtual
especializado em educação financeira.

Ajude o usuário com respostas claras, simples e educativas.

Contexto da conversa:
{context}

Pergunta do usuário:
{question}

Resposta:
"""

    return prompt
