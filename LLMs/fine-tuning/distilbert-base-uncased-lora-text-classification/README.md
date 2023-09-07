---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-lora-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-lora-text-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0684
- Accuracy: {'accuracy': 0.879}

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy            |
|:-------------:|:-----:|:----:|:---------------:|:-------------------:|
| No log        | 1.0   | 250  | 0.4266          | {'accuracy': 0.87}  |
| 0.4232        | 2.0   | 500  | 0.4260          | {'accuracy': 0.88}  |
| 0.4232        | 3.0   | 750  | 0.5071          | {'accuracy': 0.885} |
| 0.2213        | 4.0   | 1000 | 0.7424          | {'accuracy': 0.875} |
| 0.2213        | 5.0   | 1250 | 0.7885          | {'accuracy': 0.881} |
| 0.067         | 6.0   | 1500 | 0.9312          | {'accuracy': 0.872} |
| 0.067         | 7.0   | 1750 | 0.9669          | {'accuracy': 0.874} |
| 0.0238        | 8.0   | 2000 | 1.0856          | {'accuracy': 0.874} |
| 0.0238        | 9.0   | 2250 | 1.0637          | {'accuracy': 0.88}  |
| 0.0066        | 10.0  | 2500 | 1.0684          | {'accuracy': 0.879} |


### Framework versions

- Transformers 4.32.1
- Pytorch 2.0.1
- Datasets 2.14.4
- Tokenizers 0.13.2
