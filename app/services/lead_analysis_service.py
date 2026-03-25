from app.providers.factory import get_provider
from app.schemas.lead import LeadInput, LeadAnalysisResponse
from app.config import settings


class LeadAnalysisService:
    async def execute(self, lead: LeadInput) -> LeadAnalysisResponse:
        provider = get_provider()
        result = await provider.analyze_lead(lead)

        return LeadAnalysisResponse(
            provider=settings.llm_provider,
            result=result,
        )
