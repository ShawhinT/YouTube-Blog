# Direct Policy Optimization (DPO) For YouTube Title Preferences
Example code for fine-tuning Qwen2.5–0.5B-Instruct to generate YouTube titles based on my preferences using DPO.

**Links:**
- [Video link](https://youtu.be/bbVoDXoPrPM)
- [Blog link](https://shawhin.medium.com/fine-tuning-llms-on-human-feedback-rlhf-dpo-1c693dbc4cbf)
- [Dataset](https://huggingface.co/datasets/shawhin/youtube-titles-dpo)
- [Fine-tuned Model](https://huggingface.co/shawhin/Qwen2.5-0.5B-DPO)

## How to run this example

1. Clone this repo
2. Navigate to downloaded folder and create new venv
```
python -m venv dpo-env
```
3. Activate venv
```
# mac/linux
source dpo-env/bin/activate

# windows
.\dpo-env\Scripts\activate.bat
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Launch Jupyter Lab
```
jupyter lab
```
