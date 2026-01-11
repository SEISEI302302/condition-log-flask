![コンディションログ](https://github.com/user-attachments/assets/4d26f9e0-ba5c-445d-a965-29d5a31b5294)


※実際にローカル環境で動作している様子です。
#Condition Log App
日々の体調やメンタルを「簡単に」「継続して」記録できるツールが欲しいと考え、
Flask を用いたシンプルな CRUD アプリケーションとして制作しました。
バックエンド処理とフロントエンドの連携を意識しながら、
可読性と拡張性を重視して実装しています。

## 機能
- 体調（energy）とメンタル（mind）の数値記録
- コメントの追加
- 記録の編集・削除
- SQLite によるデータ保存

## 使用技術
- Python
- Flask
- SQLite
- HTML / CSS
- Git / GitHub

## 起動方法
```bash
python app.py
ブラウザで http://127.0.0.1:5000 にアクセスしてください。
```

## 今後の改善案

ユーザーごとのログイン機能

カレンダー表示

スマートフォン対応UI

記録データの可視化（グラフ表示）
---

### ② 変更をGitHubに反映

```bash
git add README.md
git commit -m "Update README"
git push
