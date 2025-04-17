import discord
import os
import json
from openai import OpenAI

TOKEN = os.environ.get('TOKEN')

# キー保存用ファイル
KEY_FILE = "user_keys.json"

# キーファイルを読み込み（なければ空辞書）
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "r") as f:
        user_keys = json.load(f)
else:
    user_keys = {}

# Discordクライアント初期化
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ ログイン成功: {client.user}（ID: {client.user.id}）')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_id = str(message.author.id)

    # 🔑 APIキー登録コマンド
    if message.content.startswith("!setkey "):
        key = message.content.replace("!setkey ", "").strip()
        if not key:
            await message.channel.send("⚠️ APIキーが空です。")
            return

        user_keys[user_id] = key
        with open(KEY_FILE, "w") as f:
            json.dump(user_keys, f)

        await message.channel.send("✅ OpenAI APIキーを登録しました。")
        return

    # 📣 メンションされてるかチェック
    if client.user in message.mentions:
        if user_id not in user_keys:
            await message.channel.send("🔐 まず `!setkey <あなたのAPIキー>` でOpenAIキーを登録してください。")
            return

        prompt = message.content.replace(f"<@{client.user.id}>", "").strip()
        if not prompt:
            await message.channel.send("✋ メンションありがとう！何か話しかけてね。")
            return

        try:
            # ユーザーごとのクライアント作成
            client_openai = OpenAI(api_key=user_keys[user_id])

            response = client_openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
            await message.channel.send(reply)

        except Exception as e:
            print(f"エラー: {e}")
            await message.channel.send("⚠️ エラーが発生しました。APIキーが無効かもしれません。")

client.run(TOKEN)