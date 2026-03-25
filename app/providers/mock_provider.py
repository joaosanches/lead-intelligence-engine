from app.providers.base import BaseLLMProvider
from app.schemas.lead import LeadInput, LeadAnalysis


class MockProvider(BaseLLMProvider):
    async def analyze_lead(self, lead: LeadInput) -> LeadAnalysis:
        text = lead.message.lower()

        if any(word in text for word in ["urgente", "quero contratar", "preço", "valor"]):
            return LeadAnalysis(
                intent="high_purchase_intent",
                priority="high",
                category="credit" if "crédito" in text else "financing",
                suggested_action="immediate_contact",
                confidence=0.86,
                reasoning="Mensagem indica intenção comercial clara e necessidade rápida de contato.",
            )

        if any(word in text for word in ["duvida", "informação", "como funciona", "quero saber"]):
            return LeadAnalysis(
                intent="information_request",
                priority="medium",
                category="other",
                suggested_action="send_information",
                confidence=0.78,
                reasoning="Mensagem pede esclarecimento e pode avançar após retorno com informações.",
            )

        if any(word in text for word in ["suporte", "erro", "problema", "não consigo"]):
            return LeadAnalysis(
                intent="support_request",
                priority="medium",
                category="support",
                suggested_action="route_to_support",
                confidence=0.84,
                reasoning="Conteúdo aparenta pedido de ajuda operacional ou suporte.",
            )

        if any(word in text for word in ["ganhe dinheiro", "clique aqui", "promoção imperdível"]):
            return LeadAnalysis(
                intent="spam_or_low_quality",
                priority="low",
                category="other",
                suggested_action="discard_or_review",
                confidence=0.91,
                reasoning="Texto apresenta padrões típicos de spam ou baixa qualidade.",
            )

        return LeadAnalysis(
            intent="unknown",
            priority="low",
            category="other",
            suggested_action="manual_review",
            confidence=0.55,
            reasoning="Mensagem ambígua; recomenda-se revisão manual.",
        )
