# 使用するPythonのバージョン
FROM python:3.11-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 残りのファイルをコピー
COPY . .

# 環境変数の読み込み（dotenv対応している場合）
ENV PYTHONUNBUFFERED=1

# Botの起動コマンド
CMD ["python", "bot.py"]