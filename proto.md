git worktree

```sh
git worktree add ../backend-worktree feature/backend-api
```
../backend-worktree ではfeature/backend-api(=remoteのブランチ名)ブランチが開いています、という意味

backend-worktree でコードを修正
git commit 
git push origin feature/backend 
リモートの feature/backend ブランチに反映されます

図解するとこうなります

【リモート (GitHub)】
   [main] [feature/backend] [feature/frontend]

          ▲           ▲            ▲
          │           │            │ (git push / pull)
          └─────┬─────┴────────────┘
                │
【ローカルPC（1つのリポジトリ本体）】
      (.git フォルダに全ての履歴がある)
                │
    ┌───────────┼───────────┐ (worktreeで展開)
    ▼           ▼           ▼
 [main/ フォルダ] [backend/ フォルダ] [frontend/ フォルダ]
 (mainブランチ)   (backendブランチ)   (frontendブランチ)

注意点：ブランチの「重複」はできない
ここが唯一の制約です。
「worktree-A」で main ブランチを開いている時、「worktree-B」で main ブランチを開くことはできません。必ず、それぞれのフォルダには別々のブランチを割り当てる必要があります。


worktree コマンド
# main から派生させて一気に作るのがおすすめです。main ブランチにいる状態で
git worktree add ../backend-worktree -b feature/backend-task
git worktree add ../frontend-worktree -b feature/frontend-task
git worktree add ../frontend-worktree -b feature/playwrite-task

git worktree add ../backend-worktree feature/backend-api
../backend-worktree で feature/backend-api(=remoteのブランチ名)ブランチを開く
git worktree list　
現在どのパスにどのブランチが展開されているか一覧表示
⚠️git worktree remove <パス>　
作業が終わったワークツリー（フォルダ）を削除します。
⚠️git worktree prune　
フォルダを直接手動削除してしまった場合、Git側の管理情報をクリーンアップ

Claude Code並列処理

Claude Code は「現在のディレクトリ」をコンテキストとして認識するため、ターミナルを複数開いて claude するのが最適です。

ターミナル1 (backend-worktree)：claude を起動。バックエンドのコードのみを対象に修正・レビューを依頼。
```sh
cd path/to/backend-worktree
```
ターミナル2 (frontend-worktree)：claude を起動。フロントエンドのコードに集中。
```sh
cd path/to/frontend-worktree
```
