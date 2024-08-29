import ollama
import json
import random

with open('intents.json') as f:
    dataset = json.load(f)

def get_response(userInput: str) -> str:
    userInput = userInput.lower()
    
    for intent in dataset['intents']:
        patterns = [p.lower() for p in intent['patterns']]
        responses = intent['responses']

        for pattern in patterns:
            if pattern == userInput or userInput in pattern:
                return random.choice(responses)

    AIResponse = ollama.chat(
        model='llama3:8b',
        messages=[
                {
                    'role': 'user',
                    'content': userInput,
                },
        ],
    )
    if len(AIResponse['message']['content']) < 2000:
        return AIResponse['message']['content']
    else:
        response_content = AIResponse['message']['content']
        chunk_size = 1999
        response_chunks = []
    
    # Calculate the number of chunks needed
        num_chunks = len(response_content) // chunk_size + (1 if len(response_content) % chunk_size > 0 else 0)
    
        for i in range(num_chunks):
            start_index = i * chunk_size
            end_index = start_index + chunk_size
            chunk = response_content[start_index:end_index]
            response_chunks.append(chunk)
    
        return response_chunks
    
