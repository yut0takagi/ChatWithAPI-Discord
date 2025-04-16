import discord
import os
from openai import OpenAI

# トークン類
TOKEN = os.environ.get('TOKEN')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# OpenAI クライアント初期化（新API対応）
client_openai = OpenAI(api_key=OPENAI_API_KEY)

# Discord クライアント設定
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログイン成功: {client.user}（ID: {client.user.id}）')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Bot自身のメッセージは無視

    # Botへのメンションがあるかチェック
    if client.user in message.mentions:
        prompt = message.content.replace(f"<@{client.user.id}>", "").strip()
        
        if not prompt:
            await message.channel.send("✋ メンションありがとう！何か話しかけてね。")
            return

        try:
            response = client_openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
            await message.channel.send(reply)

        except Exception as e:
            print(f"エラー: {e}")
            await message.channel.send("⚠️ エラーが発生しました。ログを確認してください。")

client.run(TOKEN)