"""メインアプリケーションのテスト

基本的なエンドポイントの動作を検証。
"""

from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient) -> None:
    """ルートエンドポイントが正しいレスポンスを返すことを確認

    Args:
        client: FastAPIテストクライアント
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI"}


def test_health_endpoint(client: TestClient) -> None:
    """ヘルスチェックエンドポイントが正しいレスポンスを返すことを確認

    Args:
        client: FastAPIテストクライアント
    """
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_cors_headers(client: TestClient) -> None:
    """CORSヘッダーが正しく設定されていることを確認

    Args:
        client: FastAPIテストクライアント
    """
    response = client.options(
        "/",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
