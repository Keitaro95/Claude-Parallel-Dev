.PHONY: help install dev run test lint type-check format clean

help: ## ヘルプを表示
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## プロダクション依存関係をインストール
	uv sync --no-dev

dev: ## 開発依存関係を含めてすべてインストール
	uv sync

run: ## 開発サーバーを起動（ホットリロード有効）
	uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

test: ## テストを実行
	uv run pytest -v

test-cov: ## カバレッジ付きでテストを実行
	uv run pytest --cov=. --cov-report=html --cov-report=term

lint: ## pylintでコード品質をチェック
	uv run pylint .

type-check: ## mypyで型チェック
	uv run mypy .

check: type-check lint ## 型チェックとlintを両方実行

clean: ## キャッシュと一時ファイルを削除
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf htmlcov .coverage

upgrade: ## すべての依存関係を最新バージョンに更新
	uv sync --upgrade
