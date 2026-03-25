from abc import ABC, abstractmethod
from app.schemas.lead import LeadInput, LeadAnalysis


class BaseLLMProvider(ABC):
    @abstractmethod
    async def analyze_lead(self, lead: LeadInput) -> LeadAnalysis:
        raise NotImplementedError
