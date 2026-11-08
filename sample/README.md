# sample: Confluence 自動ドキュメント生成

`sample/` 配下の Python コードを `main` に push すると、GitHub Actions
（`.github/workflows/confluence-docs.yml`）が Claude Code と Confluence MCP サーバ
（[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)、設定は `/.mcp.json`）を使い、
Confluence にコードのドキュメントページを自動作成・更新します。

## 流れ

1. `sample/**/*.py` を変更して `main` に push
2. ユニットテスト実行（失敗したらここで止まる）
3. Claude がコードを読み、Confluence MCP 経由で
   「[Learn_CICD] sample/<ファイル名>」ページを作成（既存なら更新）

## 事前設定（GitHub リポジトリの Settings → Secrets and variables → Actions）

| 種類 | 名前 | 値 |
| --- | --- | --- |
| Secret | `CLAUDE_CODE_OAUTH_TOKEN` | ローカルで `claude setup-token` を実行して発行（Claude Pro/Max） |
| Secret | `CONFLUENCE_URL` | `https://<your-site>.atlassian.net/wiki` |
| Secret | `CONFLUENCE_USERNAME` | Atlassian アカウントのメールアドレス |
| Secret | `CONFLUENCE_API_TOKEN` | https://id.atlassian.com/manage-profile/security/api-tokens で発行 |
| Variable | `CONFLUENCE_SPACE_KEY` | ページを作るスペースのキー（例: `DEV`） |

## ローカルで Claude Code から使う場合

同じ `.mcp.json` がローカルの Claude Code でも読み込まれます。環境変数を設定して起動してください。

```bash
export CONFLUENCE_URL=https://<your-site>.atlassian.net/wiki
export CONFLUENCE_USERNAME=you@example.com
export CONFLUENCE_API_TOKEN=xxxxx
export CONFLUENCE_SPACE_KEY=DEV
claude
```

## サンプルの実行

```bash
cd sample
python calculator.py
python -m unittest -v
```
