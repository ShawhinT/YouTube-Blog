# Evaluating (and Improving) a Video to Blog Converter with an LLM Judge
Example code for systematically improving a YouTube video to blog converter using LLM evals.

**Links:**
- [Video link](https://youtu.be/-sL7QzDFW-4)
- [Blog link](https://shawhin.medium.com/how-to-evaluate-and-improve-your-llm-apps-f7b08fb7493c)

### Main Python Files
- `generate_blog.py` - Main script for converting videos to blog posts
- `eval_blogs.py` - Script containing evaluation logic for the blog posts
- `results.py` - Script for handling results processing

### Configuration Files
- `requirements.txt` - Python package dependencies
- `.env` - Environment variables configuration (with OPENAI_API_KEY)
- `video_ids.txt` - List of YouTube video IDs to process

### Important Directories
- `blogs/` - Real and generated blog outputs
- `results/` - Evaluation results
- `prompt-templates/` - Templates for LLM prompts
- `transcripts/` - YouTube video transcripts
- `data-extract/` - Extracted data from Medium

Note: The articles in `blogs/0_real/` and  `data-extract/` are **copyrighted creative works and all rights are reserved**. These articles may not be reproduced or distributed without explicit permission.

## How to run this example

1. Clone this repo
2. Navigate to downloaded folder and create new venv
```
python -m venv eval-env
```
3. Activate venv
```
# mac/linux
source eval-env/bin/activate

# windows
.\eval-env\Scripts\activate.bat
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Launch Jupyter Lab
```
jupyter lab
```
