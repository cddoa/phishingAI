import ollama


#Initializing ollama client
client = ollama.Client()

model = "phishingAI"

userInput = input("> ")

prompt = f"### Input: Determine if the following is a phishing attack or not:\n{userInput} \n### Output:"

#Send query to model and generate response
response = client.generate(model=model, 
                           prompt=prompt,
                            options={
                            "temperature": 0.7,
                            "top_p": 0.9,
                            "stop": ["<|endoftext|>", "###"],
                                }) 

#Print the response
print(response["response"].strip()) 