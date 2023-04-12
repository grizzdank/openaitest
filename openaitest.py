from dotenv import load_dotenv
load_dotenv()
import openai
import os


def chat_with_gpt(prompt):
    openai.organization = os.getenv('OPENAI_ORG_ID')
    openai.api_key = os.getenv('OPENAI_API_KEY')

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )

    return response.choices[0].message['content'].strip()

def main():
    while True:
        prompt = input('What is your question? > ')
        response = chat_with_gpt(prompt)
        print(response)
        again = input('Quit or ask again? > ').strip().lower()
        if again.startswith('q'):
            break

if __name__ == "__main__":
    main()

