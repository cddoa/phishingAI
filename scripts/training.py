#All of this code was run remotely using Google Colab

import json
import torch
from unsloth import FastLanguageModel
from datasets import Dataset
from trl import SFTTrainer
from transformers import TrainingArguments


def format_prompt(example): #Function to format data for training
    return f"### Input: {example['input']}\n### Output: {example['output']}<|endoftext|>"


file = json.load(open("phishing_data.json", "r"))

model_name = "unsloth/Llama-3.2-1B-Instruct-bnb-4bit"

max_seq_length = 2048  #Sequence length
dtype = None  #Auto detection

#Load model and tokenizer
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=model_name,
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=True,
)

#Format data
formatted_data = [format_prompt(item) for item in file] 
dataset = Dataset.from_dict({"text": formatted_data})

#Add LoRA adapters
model = FastLanguageModel.get_peft_model(
    model,
    r=64,  #LoRA rank
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha=128,  #LoRA scaling factor (usually 2x rank)
    lora_dropout=0,  #Supports any, but = 0 is optimized
    bias="none",     #Supports any, but = "none" is optimized
    use_gradient_checkpointing="unsloth",  # Unsloth's optimized version
    random_state=3407,
    use_rslora=False,  #Rank stabilized LoRA
    loftq_config=None, #LoftQ
)

#Training arguments optimized for Unsloth
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    dataset_num_proc=2,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,  #Effective batch size = 8
        warmup_steps=10,
        num_train_epochs=3,
        learning_rate=2e-4,
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        logging_steps=25,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir="outputs",
        save_strategy="epoch",
        save_total_limit=2,
        dataloader_pin_memory=False,
        report_to="none", #Disable Weights & Biases logging
    ),
)

#Train the model
trainer_stats = trainer.train()

