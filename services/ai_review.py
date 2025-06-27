from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_code(code_diff):
    prompt = f"""
You are a senior code reviewer. Analyze the following GitHub pull request diff and identify:
1. Bugs and errors
2. Security issues
3. Code smells
4. Suggestions for improvement

Code diff:
{code_diff}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content
