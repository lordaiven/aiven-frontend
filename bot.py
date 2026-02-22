import discord
import requests
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
AIVEN_API = "https://aiven-ai.onrender.com"   # your backend URL

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"AIVEN Discord Bot online as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!aiven"):
        user_input = message.content.replace("!aiven", "").strip()

        if not user_input:
            await message.reply("Speak.")
            return

        await message.channel.typing()

        try:
            res = requests.post(
                AIVEN_API,
                json={"message": user_input},
                timeout=60
            )

            data = res.json()
            reply = data.get("reply", "No response")

            await message.reply(reply[:2000])

        except Exception:
            await message.reply("AIVEN backend unreachable.")

client.run(TOKEN)
