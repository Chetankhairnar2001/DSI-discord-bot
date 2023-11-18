# DSI-discord-bot

## Overview
This project implements a Discord bot that integrates with the OpenAI GPT model to provide conversational responses. The bot is designed to respond to specific commands in designated channels, 
making use of the language processing capabilities of OpenAI's GPT model. 
The bot will help with most Data Science Instructors' questions.

## Setup
### Prerequisites
Python 3.8.18 or Similar

Discord API Token

OpenAI GPT API Key

### Installation
1. Clone the repository:
 
  - https://github.com/Chetankhairnar2001/DSI-discord-bot.git

2. Install dependencies:
pip install python-dotenv

- pip install openai

- pip install langchain

- pip install chromadb

- pip install tiktoken

- pip install discord.py

3. Create a '.env' file in the root directory and add the following:
- DISCORD_TOKEN=your_discord_token_here

- CHATGPT_API_KEY=your_openai_gpt_api_key_here

- OPERATIONAL_CHANNELS= {channel1,channel2}

## Usage:
Run the bot by executing:

python main.py

The bot will connect to Discord and listen for commands in the specified operational channels. Commands include /ai and /bot, triggering the OpenAI GPT model to generate responses based on user input.

## Files:
1. discord_bot.py: Contains the Discord bot implementation using the discord library.
2. chatgpt.py: Implements the OpenAI GPT integration for generating responses.
3. main.py: Entry point that initializes and runs the Discord bot.

## Contact
For questions or feedback, feel free to reach out:

Jacob Huser
- Email: jacobhuser86@gmail.com
