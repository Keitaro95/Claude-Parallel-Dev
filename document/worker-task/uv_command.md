uv python install 3.12
uv python update-shell
uv add -r requirements.txt 
. .venv/bin/activate
uv pip install . // プロジェクト用の仮想環境にpipで現在のディレクトリをインストールする
installできない場合 VS CodeでPylanceが正しいPythonインタプリタを参照しているか確認：

VS Codeを開き、コマンドパレット（Ctrl+Shift+P）を開く。
Python: Select Interpreterを選択。
uvで作成した仮想環境のPythonパス（例：.venv/bin/python）を選択
uvコマンドでinstall uvエラー解消

