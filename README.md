# phishingAI - Phishing detection with LLaMA 3.2
A fine-tuned LLaMA 3.2 model using Unsloth.ai to detect phishing messages with a Flask web interface.
  



## Overview
- **Base Model:** unsloth/Llama-3.2-1B-Instruct-bnb-4bit
- **Training Library:** Unsloth.ai
- **Precision:** 4-bit quantization
- **LoRa adapters:** Enabled
- **Output Format:** Binary classification - "Phishing email" or "Safe email"
  
## Dataset
- Dataset Phishing_validation_emails.csv is from https://zenodo.org/records/13474746
- Converted Phishing_validation_emails.csv to JSON format
- Format: "input": raw message, "output": "Phishing" or "Safe"
- Training Data: Labeled dataset consisting of both safe and phishing messages
  
<img width="940" height="528" alt="image" src="https://github.com/user-attachments/assets/b2bf137c-30c5-4694-b735-f6740d049429" />


## Prerequisites
- Python 3.8+
- Ollama
- Flask dependencies

## Installing and Using Model Locally
- Install the model here: https://huggingface.co/cddoan/phishingAI
- After installing the model, the model file and Ollama run: ollama create phishingAI -f modelFile
- Run web application using app.py and access through http://localhost:5000

## Testing 
<img width="882" height="798" alt="image" src="https://github.com/user-attachments/assets/10ec0896-cdeb-414c-b32b-1b84509c93ec" />
  
Dectection tested with sample phishing email.
  
<img width="846" height="780" alt="image" src="https://github.com/user-attachments/assets/d2cee0c3-b363-4d10-87c2-c6362ebbe71f" />
  
Dectection tested with a real password reset email


