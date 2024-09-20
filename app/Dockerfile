# ベースイメージとしてPythonの公式イメージを使用
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt requirements.txt

# 依存パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコンテナにコピー
COPY . .

# Flaskアプリケーションを起動
CMD ["python", "app.py"]
