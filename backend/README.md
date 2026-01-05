# FastAPI バックエンド

高品質なFastAPIバックエンドアプリケーション。UV、mypy、pylintを使用した厳格な開発環境を提供します。

## クイックスタート

```bash
# 1. 依存関係のインストール
make dev

# 2. 開発サーバーの起動
make run

# 3. 型チェックとlintの実行
make check

# 4. テストの実行
make test-cov
```

## 主な特徴

- **FastAPI**: 高速で現代的なPython Webフレームワーク
- **UV**: 超高速なPythonパッケージマネージャー
- **厳格な型チェック**: mypyのstrictモード有効
- **コード品質**: pylintによる包括的なチェック
- **テスト**: pytestによる自動テスト
- **自動ドキュメント**: OpenAPI/Swaggerによる自動生成

## ドキュメント

詳細なセットアップ手順とコマンドについては [SETUP.md](./SETUP.md) を参照してください。

## 利用可能なコマンド

```bash
make help          # すべてのコマンドを表示
make dev           # 開発環境のセットアップ
make run           # サーバーを起動
make test          # テストを実行
make test-cov      # カバレッジ付きテスト
make type-check    # 型チェック
make lint          # コード品質チェック
make check         # 型チェック + lint
make clean         # キャッシュクリア
```

## API エンドポイント

起動後、以下のURLでアクセス可能:

- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 利用可能なエンドポイント

- `GET /` - ルートエンドポイント
- `GET /api/health` - ヘルスチェック

## 開発ワークフロー

1. **コードを書く**: 型ヒントとDocstringを必ず付与
2. **型チェック**: `make type-check` で検証
3. **Lint**: `make lint` でコード品質を確認
4. **テスト**: `make test` で動作確認
5. **実行**: `make run` で動作確認

## プロジェクト構成

```
backend/
├── pyproject.toml       # プロジェクト設定
├── Makefile             # 便利コマンド
├── main.py              # アプリケーション本体
├── tests/               # テストファイル
│   ├── conftest.py
│   └── test_main.py
└── .venv/               # 仮想環境
```

## 技術スタック

- **Python**: 3.12+
- **FastAPI**: 0.115.0
- **uvicorn**: 0.32.0
- **mypy**: 型チェック
- **pylint**: コード品質
- **pytest**: テストフレームワーク

## ライセンス

このプロジェクトのライセンスについては、プロジェクトルートのLICENSEファイルを参照してください。
