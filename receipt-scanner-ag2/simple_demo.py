# simple_demo.py
from ag2 import AssistantAgent, UserProxyAgent
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the LLM
llm_config = {
    "config_list": [{
        "model": "gemini-2.0-flash-exp",  # or "gemini-1.5-flash" for Gemini
        "api_key": os.getenv("GEMINI_API_KEY"),
    }],
    "temperature": 0.7,
}

# Create one agent for the assistant
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="You are a helpful assistant who likes to keep things simple and concise. You crack jokes sometimes and are a bit sarcastic."
)

# Create a user proxy for the user
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",  # Don't ask for human input
    max_consecutive_auto_reply=3,  # Stop after getting 3 responses
)

# Start a conversation
user_proxy.initiate_chat(
    assistant,
    message="Hello! What's the weather in Tokyo?"
)