# Fine-tuning Text Embedding Models
Based on the example from [here](https://sbert.net/docs/sentence_transformer/training_overview.html#trainer)

**Links:**
- [Video link](https://youtu.be/hOLBrIjRAj4)
- [Blog link](https://shawhin.medium.com/fine-tuning-text-embeddings-f913b882b11c)
- [Original Dataset](https://huggingface.co/datasets/datastax/linkedin_job_listings) | [Final Dataset](https://huggingface.co/datasets/shawhin/ai-job-embedding-finetuning)
- [Original Model](https://huggingface.co/sentence-transformers/all-distilroberta-v1) | [Fine-tuned Model](https://huggingface.co/shawhin/distilroberta-ai-job-embeddings)

## How to run this example

1. Clone this repo
2. Navigate to downloaded folder and create new venv
```
python -m venv eft-env
```
3. Activate venv
```
# mac/linux
source eft-env/bin/activate

# windows
.\eft-env\Scripts\activate.bat
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Launch Jupyter Lab
```
jupyter lab
```
