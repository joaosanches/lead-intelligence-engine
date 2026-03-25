from app.config import settings
from app.providers.base import BaseLLMProvider
from app.providers.mock_provider import MockProvider
from app.providers.groq_provider import GroqProvider


def get_provider() -> BaseLLMProvider:
    provider_name = settings.llm_provider.lower()

    if provider_name == "mock":
        return MockProvider()

    if provider_name == "groq":
        return GroqProvider()

    raise ValueError(f"Provider não suportado: {provider_name}")
