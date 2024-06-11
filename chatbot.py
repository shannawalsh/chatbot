from openai import OpenAI

client = OpenAI()

def get_response_from_openai_chatbot(model, messages):
    api_response = client.chat.completions.create(
            model = model,
            messages = messages
        )

    #extract the message content 
    response_content = api_response.choices[0].message.content

    #return the response text 
    return response_content
    
# ask the user for input
user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

messages = [
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
    ]

response_for_user = get_response_from_openai_chatbot(model, messages)

print("\n" + response_for_user + "\n")
