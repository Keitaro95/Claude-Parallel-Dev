型チェックmypy
型ヒント（type hints）を使って、型の不一致や型関連のバグをコードを実行せずに検出。大きめの API や型安全性を重視するなら特に強力

uv add --dev mypy
[tool.mypy] 型定義のない外部パッケージのインポートエラーを無視する設定です（LangChainなど一部ライブラリに型情報が無い場合があります ignore_missing_imports = True strict = True

型チェック
uv run mypy .
linter
Pylint: Pylint は、Python コードのエラーをチェックし、コーディング標準を適用し、コードの潜在的バグを検出する 高度な構成が可能なオープンソースツールです。Pylint を使用して、特定のユースケース向けのカスタムプラグインを作成することもできます。

uv add --dev pylint
pylint --generate-rcfile > .pylintrc
uv run pylint api  # 自作モジュール名（apiディレクトリ）を指定
C=Convention, W=Warning, E=Error, R=Refactor, F=Fatal

必要に応じてルールを緩める プリコミットに組み込むことも可能

環境設定ファイル
それよりも、settings.pyをおき pathを取得する .resolve()だと、絶対パスになるのあかんやて。 https://note.nkmk.me/python-pathlib-absolute-relative/

backend local deploy: uvicorn
ASGI（Asynchronous Server Gateway Interface） ネットワークプロトコルとPythonアプリケーションを繋ぐインターフェースです。

uv run uvicorn api.main:app --reload --host 0.0.0.0 --port 8000