from dotenv import load_dotenv
import discord
import os
from app.gpt import chatgpt_response
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
operational_channels = os.getenv('OPERATIONAL_CHANNELS')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully login in as ",self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        command, user_message = None, None

        if not message.channel.name in operational_channels:
            return

        for text in ['/ai','/bot']:
            if message.content.startswith(text):
                command= message.content.split(' ')[0]
                user_message = message.content.replace(text, "")
                print(command, user_message)

        if command == '/ai' or command == '/bot':
            async with message.channel.typing():
                bot_response = chatgpt_response(prompt = user_message)
                await message.reply(f"{bot_response}")

intents = discord.Intents.default()
intents.message_content= True
client = MyClient(intents=intents)
