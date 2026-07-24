# Arquitetura do Projeto

## Visão Geral

O FinanceAI foi desenvolvido utilizando uma arquitetura modular, onde cada arquivo possui uma responsabilidade específica. Essa organização facilita a manutenção, a reutilização de código e a escalabilidade do projeto.

---

## Estrutura do Projeto

```text
finance-ai-assistant/
│
├── assets/
│   └── images/
│
├── docs/
│   └── arquitetura.md
│
├── src/
│   ├── main.py
│   ├── chatbot.py
│   ├── conhecimento.py
│   ├── contexto.py
│   ├── calculos.py
│   ├── prompts.py
│   └── utils.py
│
├── tests/
│   ├── test_calculos.py
│   ├── test_chatbot.py
│   ├── test_conhecimento.py
│   ├── test_contexto.py
│   └── test_utils.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Responsabilidade de cada módulo

### main.py

Ponto de entrada da aplicação. Inicializa os componentes e inicia a interação com o usuário.

### chatbot.py

Controla a conversa com o usuário, interpreta as perguntas e retorna as respostas adequadas.

### conhecimento.py

Armazena a base de conhecimento do FinanceAI e busca respostas relacionadas aos temas financeiros.

### contexto.py

Mantém o histórico da conversa durante a execução do programa.

### calculos.py

Contém funções para cálculos financeiros, como:

- Juros simples
- Juros compostos
- Simulação de investimentos

### prompts.py

Centraliza os prompts utilizados pelo assistente virtual.

### utils.py

Reúne funções auxiliares para validação, formatação e organização do código.

---

## Organização dos Testes

Cada módulo principal possui um arquivo de teste correspondente utilizando o framework Pytest, garantindo maior confiabilidade do projeto.

---

## Benefícios da Arquitetura

- Código organizado
- Fácil manutenção
- Separação de responsabilidades
- Facilidade para adicionar novas funcionalidades
- Estrutura adequada para projetos em Python
