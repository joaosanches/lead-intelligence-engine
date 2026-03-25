from fastapi.testclient import TestClient

from app.main import app


def main() -> None:
    client = TestClient(app)

    health = client.get("/health")
    assert health.status_code == 200, f"/health status inesperado: {health.status_code}"

    payload = {
        "source": "landing_page",
        "message": "Quero saber o valor do financiamento urgente",
    }
    analyze = client.post("/analyze", json=payload)
    assert analyze.status_code == 200, f"/analyze status inesperado: {analyze.status_code}"

    body = analyze.json()
    assert "provider" in body, "campo 'provider' ausente"
    assert "result" in body, "campo 'result' ausente"

    result = body["result"]
    expected_fields = [
        "intent",
        "priority",
        "category",
        "suggested_action",
        "confidence",
        "reasoning",
    ]
    missing = [field for field in expected_fields if field not in result]
    assert not missing, f"campos ausentes em result: {missing}"

    print("Smoke test OK")
    print(f"health={health.json()}")
    print(
        "analyze_summary="
        f"intent={result['intent']}, priority={result['priority']}, "
        f"category={result['category']}, suggested_action={result['suggested_action']}"
    )


if __name__ == "__main__":
    main()
