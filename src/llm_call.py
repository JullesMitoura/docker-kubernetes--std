from src.prompts import Prompts

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
os.environ["OPENAI_API_KEY"] = os.getenv("DEEP_SEEK_API")
client = OpenAI(base_url="https://api.deepseek.com")

def llm_call(prompt):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": Prompts.get_system_message()},
            {"role": "user", "content": prompt},
    ],
    stream=False)

    return response.choices[0].message.content