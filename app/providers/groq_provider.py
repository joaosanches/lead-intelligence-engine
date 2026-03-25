import json
import httpx

from app.config import settings
from app.providers.base import BaseLLMProvider
from app.schemas.lead import LeadInput, LeadAnalysis


class GroqProvider(BaseLLMProvider):
    base_url = "https://api.groq.com/openai/v1/chat/completions"

    async def analyze_lead(self, lead: LeadInput) -> LeadAnalysis:
        if not settings.groq_api_key:
            raise ValueError("GROQ_API_KEY não configurada.")

        system_prompt = (
            "Você classifica leads de forma objetiva. "
            "Responda apenas em JSON válido com os campos: "
            "intent, priority, category, suggested_action, confidence, reasoning."
        )

        user_prompt = f'''
Classifique o lead abaixo.

Regras:
- intent: high_purchase_intent | information_request | support_request | spam_or_low_quality | unknown
- priority: low | medium | high
- category: financing | insurance | credit | support | other
- suggested_action: immediate_contact | send_information | route_to_support | discard_or_review | manual_review
- confidence: número entre 0 e 1
- reasoning: texto curto, objetivo, em português

Lead:
{lead.model_dump_json(indent=2)}
'''

        payload = {
            "model": settings.groq_model,
            "temperature": 0.2,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }

        headers = {
            "Authorization": f"Bearer {settings.groq_api_key}",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

        content = data["choices"][0]["message"]["content"]
        parsed = json.loads(content)

        return LeadAnalysis(**parsed)
