# Fluxo de Funcionamento do FinanceAI

## Visão Geral

O FinanceAI segue um fluxo simples e organizado para atender às solicitações do usuário.

---

## Fluxograma da Aplicação

```text
Início
   │
   ▼
Executa main.py
   │
   ▼
Inicializa Contexto
   │
   ▼
Inicializa Conhecimento
   │
   ▼
Inicializa ChatBot
   │
   ▼
Exibe mensagem de boas-vindas
   │
   ▼
Usuário digita uma pergunta
   │
   ▼
Pergunta é salva no histórico
   │
   ▼
Conhecimento procura uma resposta
   │
   ├──────────────► Encontrou?
   │                     │
   │               Sim   │   Não
   │                     │
   ▼                     ▼
Retorna resposta     Resposta padrão
   │                     │
   └──────────────┬──────┘
                  ▼
Resposta é exibida ao usuário
                  │
                  ▼
Usuário deseja sair?
                  │
           Não ───┴─── Sim
                  │
                  ▼
             Nova pergunta
                  │
                  ▼
                 Fim
```

---

## Etapas da Execução

### 1. Inicialização

O arquivo `main.py` inicia o programa e cria as instâncias necessárias para o funcionamento do assistente.

---

### 2. Conversa

O usuário envia uma pergunta pelo terminal.

---

### 3. Processamento

O ChatBot consulta a base de conhecimento para encontrar uma resposta adequada.

---

### 4. Resposta

Caso exista uma resposta cadastrada, ela é apresentada ao usuário.

Caso contrário, o sistema retorna uma mensagem padrão informando que ainda está aprendendo sobre aquele assunto.

---

### 5. Encerramento

Ao digitar `sair`, o programa encerra a execução de forma organizada.
