"""pytest設定とフィクスチャ

テスト全体で使用する共通のフィクスチャを定義。
"""

from typing import Generator

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    """FastAPIテストクライアント

    Yields:
        テストクライアントインスタンス
    """
    with TestClient(app) as test_client:
        yield test_client
