# バックエンド開発環境セットアップガイド

## 概要

このプロジェクトはUV（高速なPythonパッケージマネージャー）を使用したFastAPIバックエンドです。

## 前提条件

- Python 3.12以上
- UV（インストール方法は後述）

## UVのインストール

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## プロジェクトのセットアップ

### 1. Pythonバージョンの設定

```bash
cd backend
uv python install 3.12
uv python pin 3.12
```

### 2. 仮想環境の作成と依存関係のインストール

```bash
# プロダクション依存関係のインストール
uv add -r requirements.txt

# 開発依存関係のインストール
uv add --dev mypy
uv add --dev pylint
uv add --dev pytest
uv add --dev pytest-asyncio
uv add --dev httpx
```

または、pyproject.tomlから直接インストール:

```bash
uv sync
```

### 3. VS Codeでのインタプリタ設定

1. コマンドパレットを開く（Ctrl+Shift+P / Cmd+Shift+P）
2. "Python: Select Interpreter" を選択
3. `.venv/bin/python` を選択

## 開発コマンド

### アプリケーションの起動

```bash
# 開発サーバー起動（ホットリロード有効）
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

# または、短縮形
uv run uvicorn main:app --reload
```

アクセス:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 型チェック（mypy）

```bash
# プロジェクト全体の型チェック
uv run mypy .

# 特定のファイルのみ
uv run mypy main.py

# 詳細出力
uv run mypy . --show-error-codes --show-column-numbers
```

### コード品質チェック（pylint）

```bash
# プロジェクト全体のチェック
uv run pylint .

# 特定のファイルのみ
uv run pylint main.py

# 評価スコアを表示
uv run pylint . --score=y
```

出力の意味:
- C: Convention（規約違反）
- W: Warning（警告）
- E: Error（エラー）
- R: Refactor（リファクタリング推奨）
- F: Fatal（致命的エラー）

### テスト実行

```bash
# すべてのテストを実行
uv run pytest

# カバレッジ付きで実行
uv run pytest --cov=. --cov-report=html

# 特定のテストファイルのみ
uv run pytest tests/test_main.py

# 詳細出力
uv run pytest -v
```

### 依存関係の管理

```bash
# パッケージの追加
uv add package-name

# 開発依存関係の追加
uv add --dev package-name

# パッケージの削除
uv remove package-name

# パッケージの更新
uv add package-name --upgrade-package package-name

# すべての依存関係を更新
uv sync --upgrade
```

## プロジェクト構成

```
backend/
├── pyproject.toml           # プロジェクト設定（mypy, pylint含む）
├── requirements.txt         # プロダクション依存関係
├── requirements-dev.txt     # 開発依存関係
├── .python-version          # Pythonバージョン指定
├── main.py                  # アプリケーションエントリポイント
├── .venv/                   # 仮想環境（自動生成）
└── tests/                   # テストファイル（作成予定）
```

## コーディング規約

### 型ヒント

すべての関数に型ヒントを付与してください（mypy strictモード有効）:

```python
from typing import Dict

async def get_user(user_id: int) -> Dict[str, str]:
    return {"id": str(user_id), "name": "John"}
```

### Docstring

Google スタイルのDocstringを使用してください:

```python
def calculate_total(items: list[int], tax_rate: float) -> float:
    """合計金額を計算する

    Args:
        items: 商品価格のリスト
        tax_rate: 税率（0.0-1.0）

    Returns:
        税込み合計金額

    Raises:
        ValueError: tax_rateが不正な範囲の場合
    """
    if not 0 <= tax_rate <= 1:
        raise ValueError("税率は0.0から1.0の範囲で指定してください")
    subtotal = sum(items)
    return subtotal * (1 + tax_rate)
```

### 命名規則

- 変数・関数・属性: `snake_case`
- クラス: `PascalCase`
- 定数: `UPPER_CASE`
- データベース: `snake_case`（テーブル、カラム、制約名）

## トラブルシューティング

### UV関連

問題: `uv: command not found`
解決: PATHを更新してください
```bash
# シェル設定を再読み込み
source ~/.bashrc  # または ~/.zshrc
```

### 仮想環境関連

問題: パッケージがインストールされない
解決: 仮想環境を再作成してください
```bash
rm -rf .venv
uv sync
```

### mypy関連

問題: `Cannot find implementation or library stub`
解決: pyproject.tomlで `ignore_missing_imports = true` が設定されていることを確認

### pylint関連

問題: 大量の警告が表示される
解決: pyproject.tomlの `[tool.pylint.messages_control]` セクションで必要に応じてルールを無効化

## CI/CDでの使用

```yaml
# GitHub Actions の例
- name: Setup UV
  uses: astral-sh/setup-uv@v1

- name: Install dependencies
  run: uv sync

- name: Run type checking
  run: uv run mypy .

- name: Run linting
  run: uv run pylint .

- name: Run tests
  run: uv run pytest --cov
```

## 参考資料

- [UV Documentation](https://docs.astral.sh/uv/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [pylint Documentation](https://pylint.pycqa.org/)
