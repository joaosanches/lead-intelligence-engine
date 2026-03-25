import json

import pytest

from app.config import settings
from app.providers.groq_provider import GroqProvider
from app.schemas.lead import LeadInput


class _FakeResponse:
    def __init__(self, payload: dict):
        self._payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict:
        return self._payload


class _FakeAsyncClient:
    def __init__(self, response_payload: dict):
        self._response_payload = response_payload

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def post(self, *args, **kwargs):
        return _FakeResponse(self._response_payload)


@pytest.mark.asyncio
async def test_groq_provider_returns_valid_lead_analysis(monkeypatch):
    monkeypatch.setattr(settings, "groq_api_key", "test-key")
    monkeypatch.setattr(settings, "groq_model", "llama-test")

    content = json.dumps(
        {
            "intent": "high_purchase_intent",
            "priority": "high",
            "category": "financing",
            "suggested_action": "immediate_contact",
            "confidence": 0.91,
            "reasoning": "Lead demonstra urgência e intenção de compra.",
        }
    )
    payload = {"choices": [{"message": {"content": content}}]}

    from app.providers import groq_provider as module

    monkeypatch.setattr(module.httpx, "AsyncClient", lambda timeout: _FakeAsyncClient(payload))

    provider = GroqProvider()
    lead = LeadInput(source="landing_page", message="Quero fechar hoje, qual valor?")
    result = await provider.analyze_lead(lead)

    assert result.intent == "high_purchase_intent"
    assert result.priority == "high"
    assert result.confidence == 0.91


@pytest.mark.asyncio
async def test_groq_provider_raises_when_api_key_missing(monkeypatch):
    monkeypatch.setattr(settings, "groq_api_key", None)
    provider = GroqProvider()
    lead = LeadInput(source="landing_page", message="Quero saber mais.")

    with pytest.raises(ValueError, match="GROQ_API_KEY não configurada"):
        await provider.analyze_lead(lead)


@pytest.mark.asyncio
async def test_groq_provider_raises_on_invalid_json(monkeypatch):
    monkeypatch.setattr(settings, "groq_api_key", "test-key")

    payload = {"choices": [{"message": {"content": "not-json"}}]}

    from app.providers import groq_provider as module

    monkeypatch.setattr(module.httpx, "AsyncClient", lambda timeout: _FakeAsyncClient(payload))

    provider = GroqProvider()
    lead = LeadInput(source="landing_page", message="Mensagem qualquer")

    with pytest.raises(ValueError, match="Resposta inválida do provider Groq"):
        await provider.analyze_lead(lead)
