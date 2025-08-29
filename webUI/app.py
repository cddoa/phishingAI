import ollama
from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# initializing ollama client
client = ollama.Client()
model = "phishingAIv2"


# analyze user input and return model's response
def analyzeMessage(userInput):
    # if model does not load
    if not client:
        return {"error": "Model not available"}

    try:
        prompt = f"### Input: Determine if the following is a phishing attack or not:\n{userInput} \n### Output:"

        # send query to model and generate response
        response = client.generate(model=model, 
                                prompt=prompt,
                                    options={
                                    "temperature": 0.3,
                                    "top_p": 0.9,
                                    "stop": ["."],
                                        }) 

        # return response
        result = response["response"].strip()
        result = result.split("email")
        classification = result[0]
        explanation = result[1]

        print(f'classification: {classification}')
        print(f'explanation:  {explanation}')

        return {"classification": classification, "explanation": explanation , "error": None}
    
    except:
        return {"error": "Analysis failed"}
    

    
# web ui frontend
@app.route('/')
def index():
    # main page
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    # api endpoint for analyzing user input
        data = request.get_json()

        # if no text is detected in json
        if not data or "text" not in data:
            return jsonify({"error": "No text detected in json"}), 400
        
        userInput = data['text'].strip()

        # if user does not enter any text
        if not userInput:
            return jsonify({"error": "No text detected"}), 400
        # if user input > 5000
        if len(userInput) > 5000:
            return jsonify({"error": "Text is too long - 5000 character max"})
        
        # analyze message
        result = analyzeMessage(userInput)
        return jsonify(result)



@app.route('/health')
def health():
    #health check endpoint
    status = "healthy" if client else "unhealthy"

    return jsonify({"status": status, "model": model})


if __name__ == "__main__":
    app.run(debug=True, port=5000)




