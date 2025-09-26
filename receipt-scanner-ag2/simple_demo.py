# simple_demo.py
from autogen import AssistantAgent, UserProxyAgent
import os
from dotenv import load_dotenv

load_dotenv()

# Configure for Gemini - note the specific format needed
llm_config = {
    "config_list": [{
        "model": "gemini-2.0-flash-exp",  # or gemini-1.5-pro, gemini-1.0-pro
        "api_key": os.getenv("GEMINI_API_KEY"),
        "api_type": "google"  # Important: specify this for Gemini
    }],
    "temperature": 0.7,
}

# Create one agent
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="You are a helpful assistant who likes to keep things simple. You crack jokes and are a bit sarcastic."
)

# Create a user proxy
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",  # Don't ask for human input
    max_consecutive_auto_reply=0,  # Stop after getting one response
    code_execution_config=False,  # Disable code execution for now
)

# Start a conversation
user_proxy.initiate_chat(
    assistant,
    message="Hello! What's the weather in Tokyo?"
)