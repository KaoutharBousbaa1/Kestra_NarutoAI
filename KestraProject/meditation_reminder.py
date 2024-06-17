import openai
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9,
    )
    return response.choices[0].message["content"]


instructions = f" character "Naruto". Write an SMS to me.
Telling me to chill for 10 min and meditate for a while.
Say something inspiring  and encouraging. 
The greeting should be very short like "Hi Tina!".
The message should be between 80 and 160 characters long.
Sign the message at the end with "Naruto"""
You are the anime.
"""
message = get_completion(instructions)
print(message)