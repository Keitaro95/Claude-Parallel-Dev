"""FastAPI アプリケーションのエントリポイント

基本的なCORS設定とヘルスチェックエンドポイントを提供するFastAPIアプリケーション。
"""

from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> Dict[str, str]:
    """ルートエンドポイント

    Returns:
        メッセージを含む辞書
    """
    return {"message": "Hello from FastAPI"}


@app.get("/api/health")
async def health() -> Dict[str, str]:
    """ヘルスチェックエンドポイント

    Returns:
        ステータスを含む辞書
    """
    return {"status": "ok"}
