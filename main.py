import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    print("Hello from bootdev-ai!")
    parser = argparse.ArgumentParser(description="Chatbot using Gemini API")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the chatbot")
    args = parser.parse_args()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.user_prompt
    )
    if response.usage_metadata == None:
        raise RuntimeError("Usage metadata is None")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)


if __name__ == "__main__":
    main()
