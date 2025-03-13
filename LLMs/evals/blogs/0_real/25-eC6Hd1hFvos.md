# Fine-Tuning Large Language Models (LLMs)

## A Conceptual Overview with Example Python Code

This is the 5th article in a [series on using Large Language Models](https://medium.com/towards-data-science/a-practical-introduction-to-llms-65194dda1148) (LLMs) in practice. In this post, we will discuss how to fine-tune (FT) a pre-trained LLM. We start by introducing key FT concepts and techniques, then finish with a concrete example of how to fine-tune a model (locally) using Python and Hugging Face’s software ecosystem.

![Tuning a language model](https://cdn-images-1.medium.com/max/800/1*YHNrnuaHtS2meh39gGmCCw.png)
*Tuning a language model. Image by author.*

## What is Fine-Tuning?

**Fine-tuning** is taking a pre-trained model and **training at least one internal model parameter** (i.e. weights). In the context of LLMs, what this typically accomplishes is transforming a general-purpose base model (e.g. GPT-3) into a specialized model for a particular use case (e.g. ChatGPT).

The **key upside** of this approach is that models can achieve better performance while requiring (far) fewer manually labeled examples compared to models that solely rely on supervised training.

## Why Fine-Tune?

Fine-tuning not only improves the performance of a base model, but **a smaller (fine-tuned) model can often outperform larger (more expensive) models** on the set of tasks on which it was trained. This was demonstrated by OpenAI with their first-generation “InstructGPT” models, where the 1.3B parameter InstructGPT model completions were preferred over the 175B parameter GPT-3 base model despite being 100x smaller.

## 3 Ways to Fine-Tune

There are **three generic ways** one can fine-tune a model:

### Self-Supervised Learning

Self-supervised learning consists of **training a model based on the inherent structure of the training data**. In LLMs, this typically involves predicting the next token given a sequence of tokens.

### Supervised Learning

Supervised learning involves **training a model on input-output pairs** for a particular task. An example is **instruction tuning**, which aims to improve model performance in answering questions or responding to user prompts.

### Reinforcement Learning

Reinforcement Learning (RL) **uses a reward model to guide training**. This method was used in OpenAI’s InstructGPT models, where RL was applied after supervised fine-tuning to refine responses based on human preferences.

## Example Code: Fine-Tuning an LLM Using LoRA

In this example, we will use the Hugging Face ecosystem to fine-tune a language model to classify text as ‘positive’ or ‘negative’ using **LoRA (Low-Rank Adaptation)**.

### Imports

```python
from datasets import load_dataset
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
)
from peft import LoraConfig, get_peft_model
import torch
import numpy as np
```

### Load Dataset

```python
dataset = load_dataset("shawhin/imdb-truncated")
```

### Tokenization

```python
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, max_length=512)
tokenized_dataset = dataset.map(tokenize_function, batched=True)
```

### Model Setup

```python
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)
```

### Apply LoRA

```python
peft_config = LoraConfig(task_type="SEQ_CLS", r=4, lora_alpha=32, lora_dropout=0.01, target_modules=["q_lin"])
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()
```

### Training Setup

```python
training_args = TrainingArguments(
    output_dir="distilbert-base-uncased-lora-text-classification",
    learning_rate=1e-3,
    per_device_train_batch_size=4,
    num_train_epochs=10,
    weight_decay=0.01,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    tokenizer=tokenizer,
)
trainer.train()
```

## Conclusions

Fine-tuning an existing model requires more computational resources and technical expertise than using one out-of-the-box. However, smaller fine-tuned models can outperform larger pre-trained models for specific use cases. Furthermore, with open-source LLM resources, fine-tuning models for custom applications has never been easier.