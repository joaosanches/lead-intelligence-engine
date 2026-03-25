from fastapi import FastAPI
from app.config import settings
from app.schemas.lead import LeadInput, LeadAnalysisResponse
from app.services.lead_analysis_service import LeadAnalysisService

app = FastAPI(title=settings.app_name)
service = LeadAnalysisService()


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.app_env, "provider": settings.llm_provider}


@app.post("/analyze", response_model=LeadAnalysisResponse)
async def analyze_lead(payload: LeadInput) -> LeadAnalysisResponse:
    return await service.execute(payload)
