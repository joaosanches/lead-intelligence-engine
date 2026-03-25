# 🚀 Lead Intelligence Engine

Projeto de IA aplicada para classificação de leads utilizando LLMs, com foco em saídas estruturadas, validação com Pydantic e workflows determinísticos.

---

## 🎯 Objetivo

Este projeto demonstra como utilizar modelos de linguagem (LLMs) para resolver um problema real de negócio: **classificação e priorização de leads**.

A proposta é transformar texto não estruturado (mensagens de leads) em decisões estruturadas e acionáveis.

---

## 🧠 Problema

Leads chegam com mensagens livres, por exemplo:

> "Quero saber o valor do financiamento e preciso fechar hoje"

Sem estrutura, fica difícil:
- priorizar atendimento
- automatizar decisões
- escalar operação

---

## ⚙️ Solução

Pipeline de classificação com LLM:

1. Recebe dados do lead
2. Processa e estrutura entrada
3. Classifica via LLM (ou heurística local)
4. Valida saída com Pydantic
5. Retorna decisão padronizada

---

## 📦 Exemplo

### Entrada

```json
{
  "message": "Quero saber o valor do financiamento urgente",
  "source": "landing_page"
}
```

### Saída

```json
{
  "intent": "high_purchase_intent",
  "priority": "high",
  "category": "financing",
  "suggested_action": "immediate_contact",
  "confidence": 0.86
}
```

---

## 🏗️ Arquitetura

- FastAPI: camada de API
- Pydantic: validação e contratos de dados
- Provider Layer: abstração de LLM (`mock`, `groq`, `openai-ready`)
- Service Layer: orquestração da análise

---

## 🔌 Providers suportados

- `mock`: sem custo, baseado em heurística (para desenvolvimento)
- `groq`: integração com LLM real
- `openai`: preparado para futura integração

---

## 🛠️ Setup do ambiente (uv)

Este projeto utiliza `uv`, uma ferramenta moderna para gerenciamento de dependências Python.

### 📦 Instalar uv

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

ou:

```bash
pip install uv
```

### 🧱 Criar ambiente virtual

```bash
uv venv
```

Ativar:

```bash
source .venv/bin/activate
```

### 📥 Instalar dependências

```bash
uv sync
```

Para instalar dependências de desenvolvimento:

```bash
uv sync --group dev
```

Dependências de desenvolvimento configuradas no projeto:

```toml
[dependency-groups]
dev = [
    "pytest",
    "pytest-asyncio"
]
```

---

## ⚙️ Configuração

Crie um arquivo `.env` baseado no `.env.example`:

```env
LLM_PROVIDER=mock
```

---

## ▶️ Executando a aplicação

```bash
uv run uvicorn app.main:app --reload
```

Acesse:

👉 http://127.0.0.1:8000/docs

---

## 🧪 Testes

```bash
PYTHONPATH=. uv run pytest -q
```

---

## 🧠 Conceitos aplicados

- LLM aplicado a problema real
- Saída estruturada (structured output)
- Validação de resposta (Pydantic)
- Abstração de provider
- Workflow determinístico
- Separação de responsabilidades

---

## 🚧 Próximos passos

- Implementar roteamento por tipo de lead (routing)
- Criar dataset de avaliação
- Adicionar métricas de qualidade
- Comparar providers (Groq vs outros)
- Implementar fallback heurístico
- Melhorar score de confiança

---

## 📌 Motivação

Este projeto foi criado como parte da transição para atuação em IA aplicada, com foco em:

- confiabilidade de sistemas baseados em LLM
- qualidade de respostas
- integração com sistemas reais

---

## 👨‍💻 Autor

João Paulo Gonçalves Sanches  
Senior Software Engineer / Tech Lead
