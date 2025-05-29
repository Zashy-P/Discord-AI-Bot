import ollama,json,random,asyncio

conversation_histories = {}

with open('intents.json') as f:
    dataset = json.load(f)

async def get_response(userInput: str, userID: str) -> str:
    userInput = userInput.lower()
    
    for intent in dataset['intents']:
        patterns = [p.lower() for p in intent['patterns']]
        responses = intent['responses']

        for pattern in patterns:
            if pattern == userInput or userInput in pattern:
                return random.choice(responses)

    # add the user's input to the conversation history    
    history = conversation_histories.get(userID, [])
    history.append({'role': 'user', 'content': userInput})           

    AIResponse = await asyncio.to_thread(ollama.chat, model='llama3:8b', messages=history)
    #print(f"Received AI response: {AIResponse}") #uncomment to see the response 

    # add the ai's response to the history
    assistant_reply = AIResponse['message']['content']
    history.append({'role': 'assistant', 'content': assistant_reply})
    conversation_histories[userID] = history


    if len(assistant_reply) < 2000:
        return assistant_reply
    else:
        chunk_size = 1999
        response_chunks = []
    
        # Calculate the number of chunks needed
        num_chunks = len(assistant_reply) // chunk_size + (1 if len(assistant_reply) % chunk_size > 0 else 0)
    
        for i in range(num_chunks):
            start_index = i * chunk_size
            end_index = start_index + chunk_size
            chunk = assistant_reply[start_index:end_index]
            response_chunks.append(chunk)
    
        return response_chunks
    
