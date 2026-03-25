from typing import Literal
from pydantic import BaseModel, Field


IntentType = Literal[
    "high_purchase_intent",
    "information_request",
    "support_request",
    "spam_or_low_quality",
    "unknown",
]

PriorityType = Literal["low", "medium", "high"]
CategoryType = Literal["financing", "insurance", "credit", "support", "other"]
ActionType = Literal[
    "immediate_contact",
    "send_information",
    "route_to_support",
    "discard_or_review",
    "manual_review",
]


class LeadInput(BaseModel):
    source: str = Field(..., examples=["landing_page"])
    name: str | None = Field(default=None, examples=["João"])
    email: str | None = Field(default=None, examples=["joao@email.com"])
    phone: str | None = Field(default=None, examples=["14999999999"])
    message: str = Field(..., examples=["Quero saber preço de financiamento urgente"])
    created_at: str | None = Field(default=None, examples=["2026-03-25T10:00:00Z"])


class LeadAnalysis(BaseModel):
    intent: IntentType
    priority: PriorityType
    category: CategoryType
    suggested_action: ActionType
    confidence: float = Field(..., ge=0, le=1)
    reasoning: str = Field(..., max_length=500)


class LeadAnalysisResponse(BaseModel):
    provider: str
    result: LeadAnalysis
