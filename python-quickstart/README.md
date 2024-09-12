# Python QuickStart for People Learning AI [Mini-Course]

This repo contains the supplementary example code for the "Python QuickStart for People Learning AI" YouTube video and Medium blog. It is not meant to be a comprehensive introduction to Python. Rather, it’s meant to give you just enough to code your first AI project with Python fast!

🎥 [YouTube Video](https://youtu.be/pNg2DJ4spXg) | 📰 [Medium Blog](https://medium.com/towards-data-science/python-quickstart-for-people-learning-ai-58a1b76df0f4)

### Getting Started

To run the [summarize-paper.py](https://github.com/ShawhinT/YouTube-Blog/blob/main/python-quickstart/summarize-paper.py) example, follow these steps.

1. Confirm Python is installed on your machine
2. Create a new virtual environment and activate it
```
python -m venv my-env

# mac/linux
source my-env/bin/activate 
# windows
.\my-env\Scripts\activate.bat
```
3. Install the dependencies
```
pip install -r requirements.txt
```
4. Run the code
```
python summarize-paper.py "files/attention-is-all-you-need.pdf"
```
