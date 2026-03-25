# Lead Intelligence Engine

Projeto inicial para classificar leads com LLM usando:
- FastAPI
- Pydantic
- camada de provider
- fallback mock para desenvolvimento

## Objetivo
Receber dados de um lead e retornar uma análise estruturada com:
- intenção
- prioridade
- categoria
- ação sugerida
- confiança

## Estrutura
- `app/main.py`: API FastAPI
- `app/services/lead_analysis_service.py`: orquestra a análise
- `app/providers/base.py`: contrato de provider
- `app/providers/mock_provider.py`: provider local sem custo
- `app/providers/groq_provider.py`: provider pronto para Groq
- `app/schemas/lead.py`: schemas Pydantic
- `examples/sample_request.json`: exemplo de payload

## Como rodar

### 1. Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar ambiente
Copie `.env.example` para `.env`.

Para começar sem custo:
```env
LLM_PROVIDER=mock
```

Quando quiser usar Groq:
```env
LLM_PROVIDER=groq
GROQ_API_KEY=sua_chave_aqui
GROQ_MODEL=llama-3.3-70b-versatile
```

### 4. Subir API
```bash
uvicorn app.main:app --reload
```

### 5. Testar
Abra:
- `http://127.0.0.1:8000/docs`

## Próximos passos
- adicionar heurísticas antes do LLM
- criar dataset de avaliação
- versionar prompts
- adicionar score de risco/spam
- criar roteamento por tipo de lead
# lead-intelligence-engine
