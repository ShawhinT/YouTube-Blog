# Fine-tuning Text Embedding Models
Based on the example from [here](https://sbert.net/docs/sentence_transformer/training_overview.html#trainer)

**Links:**
- Video link (coming soon!)
- Blog link (coming soon!)
- [Original Dataset](https://huggingface.co/datasets/datastax/linkedin_job_listings) | [Final Dataset](https://huggingface.co/datasets/shawhin/ai-job-embedding-finetuning)
- [Original Model](https://huggingface.co/sentence-transformers/all-distilroberta-v1) | [Fine-tuned Model](https://huggingface.co/shawhin/distilroberta-ai-job-embeddings)

## How to run this example

1. Clone this repo
2. Navigate to downloaded folder and create new venv
```
python -m venv s5-env
```
3. Activate venv
```
# mac/linux
source s5-env/bin/activate

# windows
.\s5-env\Scripts\activate.bat
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Launch Jupyter Lab
```
jupyter lab
```
