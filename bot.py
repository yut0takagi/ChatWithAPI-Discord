# bot.py
import discord
import openai
import os
TOKEN = os.environ.get('TOKEN')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログイン成功: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Bot自身のメッセージには反応しない

    prompt = message.content

    response = openai.ChatCompletion.create(
        model="gpt-4o",  # または gpt-4
        messages=[{"role": "user", "content": prompt}]
    )

    await message.channel.send(response['choices'][0]['message']['content'])

client.run(TOKEN)