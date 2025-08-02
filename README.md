# phishingAI - Phishing detection with LLaMA 3.2
A fine-tuned LLaMA 3.2 model using Unsloth.ai to detect phishing messages

## Overview
- **Base Model:** unsloth/Llama-3.2-1B-Instruct-bnb-4bit
- **Training Library:** Unsloth.ai
- **Precision:** 4-bit quantization
- **LoRa adapters:** Enabled
- LLaMA model was trained using a labeled dataset consisting of both safe and phishing messages
- Trained on an NVIDIA GPU using Google Colab
  
## Dataset
- Dataset Phishing_validation_emails.csv is from https://zenodo.org/records/13474746
- Converted Phishing_validation_emails.csv to JSON format
- Format: "input": raw message, "output": "Phishing" or "Safe"
  
## Adding the model to Ollama
- Install the model here: https://huggingface.co/cddoan/phishingAI
- After installing the model, the model file and Ollama run: ollama create phishingAI -f modelFile
- Run the model through app.py 
