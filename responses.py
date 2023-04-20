import openai
import os

openai.api_key = os.environ['API_KEY']
def handle_response(message) -> str:

    model_engine = "text-davinci-002"
    prompt = f"{message}\n"
    
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    ).choices[0].text
    
    return response