# phishingAI - Phishing detection with LLaMA 3.2
A fine-tuned LLaMA 3.2 model using Unsloth.ai to detect phishing messages with a Flask web interface.
  



## Overview
- **Base Model:** unsloth/Llama-3.2-1B-Instruct-bnb-4bit
- **Training Library:** Unsloth.ai
- **Precision:** 4-bit quantization
- **LoRa adapters:** Enabled
- **Output Format:** Classification - "Phishing email" or "Safe email" and Explanation - details from the message that indicate the message's classfication 
  
## Dataset
- Original dataset Phishing_validation_emails.csv is from https://zenodo.org/records/13474746
- Converted Phishing_validation_emails.csv to JSON format and added explanations
- Format: "input": raw message, "output": "Label: (phishing or safe) \n Explanation: (explanation of why the message is phishing or safe)"

  
<img width="940" height="528" alt="image" src="https://github.com/user-attachments/assets/b2bf137c-30c5-4694-b735-f6740d049429" />
  
phishingAI's web UI

## Prerequisites
- Python 3.8+
- Ollama
- Flask dependencies

## Installing and Using Model Locally
- Install the model here: https://huggingface.co/cddoan/phishingAI
- After installing the model, the model file and Ollama navigate to the model's directory and run: ollama create phishingAI -f modelFile
- Run web application using app.py and access through http://localhost:5000

## Testing 
<img width="895" height="778" alt="image" src="https://github.com/user-attachments/assets/50f4857d-3e2d-4ebc-9265-373e43a7d2a4" />
  
Dectection tested with sample phishing email. The model detected requests for personal information and the impersonation of an official institution to classify the message as phishing.
  
#
<img width="818" height="734" alt="image" src="https://github.com/user-attachments/assets/683092bc-c08b-4a5a-9ec9-d4c3bba64aaf" />
  
Dectection tested with a real password reset email. The model detected that the message was a legitimate service notification.


