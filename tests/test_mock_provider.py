import pytest
from app.providers.mock_provider import MockProvider
from app.schemas.lead import LeadInput


@pytest.mark.asyncio
async def test_mock_provider_high_purchase_intent():
    provider = MockProvider()
    lead = LeadInput(
        source="landing_page",
        message="Quero saber preço do financiamento urgente",
    )

    result = await provider.analyze_lead(lead)

    assert result.intent == "high_purchase_intent"
    assert result.priority == "high"
