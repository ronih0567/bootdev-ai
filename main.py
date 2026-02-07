import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import call_function,available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    print("Hello from bootdev-ai!")
    parser = argparse.ArgumentParser(description="Chatbot using Gemini API")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt, temperature=0,tools=[available_functions],),
        )
        if response.candidates is None:
            raise Exception("Response candidates is None")
        for candidate in response.candidates:
            if candidate.content is None:
                raise Exception("Candidate content is None")
            messages.append(candidate.content)
        if response.usage_metadata == None:
            raise RuntimeError("Usage metadata is None")
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if response.function_calls is None:
            print(response.text)
            return
        else:
            for function_call in response.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")
                function_call_result = call_function(function_call, verbose=args.verbose)
                if function_call_result.parts is None:
                    raise Exception("Function call result has no parts")
                if function_call_result.parts[0].function_response is None:
                    raise Exception("Function call result part has no function response")
                if function_call_result.parts[0].function_response.response is None:
                    raise Exception("Function call result part has no function response content")
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                messages.append(function_call_result)
                messages.append(types.Content(role="user", parts=function_call_result.parts))
    print("Error: Reached maximum model iterations")
    exit(1)

if __name__ == "__main__":
    main()
