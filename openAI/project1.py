import openai

# Set your OpenAI API key
openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletionCompletion.create(
        # engine="text-davinci-002",
        # prompt=prompt,
        # max_tokens=100,
        # temperature=0.7,
        # n=1,
        # stop=["\n"]
        model = "gpt-3.5-turbo",
        messages = [{"role" : "user", "content": prompt}]
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_input = input("Enter your message: ")
    chat_gpt_response = chat_with_gpt(user_input)
    print("ChatGPT response:", chat_gpt_response)


