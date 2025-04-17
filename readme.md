# 🤖 ChatWithAPI-Discord

**ChatWithAPI-Discord** は、ユーザーが自分自身の OpenAI API キーを設定し、Botにメンションすることで GPT-4o などのモデルと対話できる Discord Bot です。

---

## 🚀 主な機能

- `/setkey` コマンドで自分の OpenAI API キーを登録
- メンションされたときだけ返信
- ユーザーごとの API キーを個別に保存（マルチユーザー対応）
- `openai>=1.0.0` に対応した最新バージョン

---

## 🛠 使用技術

- Python 3.11+
- `discord.py`
- `openai>=1.0.0`
- JSONファイルによるAPIキーの保存

---