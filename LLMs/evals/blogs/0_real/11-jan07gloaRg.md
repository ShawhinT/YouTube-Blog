# Cracking Open the Hugging Face Transformers Library
#### A quick-start guide to using open-source LLMs

This is the 3rd article in a [series on using large language models (LLMs)](https://towardsdatascience.com/a-practical-introduction-to-llms-65194dda1148) in practice. Here I will give a beginner-friendly guide to
the Hugging Face Transformers library, which provides an easy and cost-free
way to work with a wide variety of open-source language models. I will start
by reviewing key concepts and then dive into example Python code.

![](https://cdn-images-1.medium.com/max/800/0*Rkoquyw55K6qbFWF)Photo by [Jéan
Béller](https://unsplash.com/@chinatravelchannel?utm_source=medium&utm_medium=referral)
on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

* * *

In the [previous article](https://towardsdatascience.com/cracking-open-the-openai-python-api-230e4cae7971) of this series, we explored the OpenAI Python
API and used it to make a custom chatbot. One downside of this API, however,
is that API calls cost money, which may not scale well for some use cases.

In these scenarios, it may be advantageous to turn to open-source solutions.
One popular way to do this is via Hugging Face’s Transformers library.

### **What is Hugging Face?**

**Hugging Face** is an **AI company that has become a major hub for open-
source machine learning (ML)**. Their platform has 3 major elements which
allow users to access and share machine learning resources.

First is their rapidly growing repository of pre-trained open-source ML
**models** for things such as natural language processing (NLP), computer
vision, and more. Second is their library of **datasets** for training ML
models for almost any task. Third, and finally, is **Spaces** which is a
collection of open-source ML apps hosted by Hugging Face.

The power of these resources is that they are community generated, which
leverages all the benefits of open-source (i.e. cost-free, wide diversity of
tools, high-quality resources, and rapid pace of innovation). While these make
building powerful ML projects more accessible than before, there is another
key element of the Hugging Face ecosystem — the Transformers library.

### 🤗**Transformers**

**Transformers** is a **Python library that makes downloading and training
state-of-the-art ML models easy**. Although it was initially made for
developing language models, its functionality has expanded to include models
for computer vision, audio processing, and beyond.

Two big strengths of this library are, **one** , it easily integrates with
Hugging Face’s (previously mentioned) Models, Datasets, and Spaces
repositories, and **two** , the library supports other popular ML frameworks
such as PyTorch and TensorFlow.

This results in a simple and flexible all-in-one platform for downloading,
training, and deploying machine learning models and apps.

#### **Pipeline()**

The easiest way to start using the library is via the _pipeline()_ function,
which abstracts NLP (and other) tasks into 1 line of code. For example, if we
want to do sentiment analysis, we would need to select a model, tokenize the
input text, pass it through the model, and decode the numerical output to
determine the sentiment label (positive or negative).

While this may seem like a lot of steps, we can do all this in 1 line via the
_pipeline()_ function, as shown in the code snippet below.

    
    
    pipeline(task="sentiment-analysis")("Love this!")  
      
    # output -> [{'label': 'POSITIVE', 'score': 0.9998745918273926}]

Of course, sentiment analysis is not the only thing we can do here. Almost any
NLP task can be done in this way e.g. summarization, translation, question-
answering, feature extraction (i.e. text embedding), text generation, zero-
shot-classification, and more —  _for a full list of the built-in tasks, check
out the_[ _pipleine() documentation_](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.pipeline.task).

In the above example code, since we did not specify a model, the default model
for sentiment analysis was used (i.e. _distilbert-base-uncased-finetuned-
sst-2-english_). However, if we wanted to be more explicit, we could have used
the following line of code.

    
    
    pipeline(task="sentiment-analysis",   
            model='distilbert-base-uncased-finetuned-sst-2-english')("Love this!")  
      
    # ouput -> [{'label': 'POSITIVE', 'score': 0.9998745918273926}]

One of the greatest benefits of the Transformers library is we could have just
as easily used any of the 28,000+ text classification models on Hugging Face’s
[Models repository](https://huggingface.co/models?pipeline_tag=text-classification&sort=trending) by simply changing the model name passed into
the _pipeline()_ function.

#### **Models**

There is a massive repository of pre-trained models available on [Hugging Face](https://huggingface.co/models) (277,528 at the time of writing this).
Almost all these models can be easily used via Transformers, using the same
syntax we saw in the above code block.

However, the models on Hugging Face **aren’t only for the Transformers
library.** There are models for other popular machine learning frameworks e.g.
PyTorch, Tensorflow, Jax. This makes Hugging Face’s Models repository useful
to ML practitioners beyond the context of the Transformers library.

To see what navigating the repository looks like, let’s consider an example.
Say we want a model that can do text generation, but we want it to be
available via the Transformers library so we can use it in one line of code
(as we did above). We can easily view all models that fit these criteria using
the “Tasks” and “Libraries” filters.

A model that meets these criteria is the newly released Llama 2. More
specifically, _Llama-2–7b-chat-hf_ , which is a model in the Llama 2 family
with about 7 billion parameters, optimized for chat, and in the Hugging Face
Transformers format. We can get more information about this model via its
**model card** , which is shown in the figure below.

![](https://cdn-images-1.medium.com/max/800/1*0B5_bK2QAoNNTepbcZNFNQ.jpeg)Touring the
[Llama-2–7b-chat-hf model card](https://huggingface.co/meta-
llama/Llama-2-70b-chat-hf). Image by author.

### **Installing** 🤗**Transformers (with Conda)**

Now that we have a basic idea of the resources offered by Hugging Face and the
Transformers library let’s see how we can use them. We start by installing the
library and other dependencies.

Hugging Face provides an [installation guide](https://huggingface.co/docs/transformers/installation) on its website.
So, I won’t try to (poorly) duplicate that guide here. However, I will provide
a quick 2-step guide on **how to set up the conda environment for the example
code below**.

**Step 1)** The first step is to download the hf-env.yml file available at the
[GitHub repository](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/hugging-face). You can either download the file directly
or clone the whole repo.

**Step 2)** Next, in your terminal (or anaconda command prompt), you can
create a new conda environment based on hf-env.yml using the following
commands

    
    
    >>> cd <directory with hf-env.yml>  
      
    >>> conda env create --file hf-env.yml

This may take a couple of minutes to install, but once it’s complete, you
should be ready to go!

### **Example Code: NLP with** 🤗**Transformers**

With the necessary libraries installed, let’s jump into some example code.
Here we will survey **3 NLP use cases** , namely, **sentiment analysis,
summarization, and conversational text generation** , using the _pipeline()_
function.

Toward the end, we will use Gradio to quickly generate a User Interface (UI)
for any of these use cases and deploy it as an app on Hugging Face Spaces. All
example code is available on the [GitHub repository](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/hugging-face).

#### **Sentiment Analysis**

We start sentiment analysis. Recall from earlier when we used the pipeline
function to do something like the code block below, where we create a
classifier that can label the input text as being either positive or negative.

    
    
    from transformers import pipeline  
      
    classifier = pipeline(task="sentiment-analysis", \  
                          model="distilbert-base-uncased-finetuned-sst-2-english")  
      
    classifier("Hate this.")  
      
    # output -> [{'label': 'NEGATIVE', 'score': 0.9997110962867737}]

To go one step further, instead of processing text one by one, we can pass a
list to the classifier to process as a batch.

    
    
    text_list = ["This is great", \  
                 "Thanks for nothing", \  
                 "You've got to work on your face", \  
                 "You're beautiful, never change!"]  
      
    classifier(text_list)  
      
    # output -> [{'label': 'POSITIVE', 'score': 0.9998785257339478},  
    # {'label': 'POSITIVE', 'score': 0.9680058360099792},  
    # {'label': 'NEGATIVE', 'score': 0.8776106238365173},  
    # {'label': 'POSITIVE', 'score': 0.9998120665550232}]

However, the text classification models on Hugging Face are not limited to
just positive-negative sentiment. For example, the “ _roberta-base-
go_emotions_ ” model by SamLowe generates a suite of class labels. We can just
as easily apply this model to text, as shown in the code snippet below.

    
    
    classifier = pipeline(task="text-classification", \  
                          model="SamLowe/roberta-base-go_emotions", top_k=None)  
      
    classifier(text_list[0])  
      
    # output -> [[{'label': 'admiration', 'score': 0.9526104927062988},  
    #  {'label': 'approval', 'score': 0.03047208860516548},  
    #  {'label': 'neutral', 'score': 0.015236231498420238},  
    #  {'label': 'excitement', 'score': 0.006063772831112146},  
    #  {'label': 'gratitude', 'score': 0.005296189337968826},  
    #  {'label': 'joy', 'score': 0.004475208930671215},  
    #  ... and many more

#### **Summarization**

Another way we can use the _pipeline()_ function is for text summarization.
Although this is an entirely different task than sentiment analysis, the
syntax is almost identical.

We first load in a summarization model. Then pass in some text along with a
couple of input parameters.

    
    
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  
      
    text = """  
    Hugging Face is an AI company that has become a major hub for open-source machine learning.   
    Their platform has 3 major elements which allow users to access and share machine learning resources.   
    First, is their rapidly growing repository of pre-trained open-source machine learning models for things such as natural language processing (NLP), computer vision, and more.   
    Second, is their library of datasets for training machine learning models for almost any task.   
    Third, and finally, is Spaces which is a collection of open-source ML apps.  
      
    The power of these resources is that they are community generated, which leverages all the benefits of open source i.e. cost-free, wide diversity of tools, high quality resources, and rapid pace of innovation.   
    While these make building powerful ML projects more accessible than before, there is another key element of the Hugging Face ecosystem—their Transformers library.  
    """  
    summarized_text = summarizer(text, min_length=5, max_length=140)[0]['summary_text']  
    print(summarized_text)  
      
    # output -> 'Hugging Face is an AI company that has become a major hub for   
    # open-source machine learning. They have 3 major elements which allow users   
    # to access and share machine learning resources.' 

For more sophisticated use cases, it may be necessary to use multiple models
in succession. For example, we can apply sentiment analysis to the summarized
text to speed up the runtime.

    
    
    classifier(summarized_text)  
      
    # output -> [[{'label': 'neutral', 'score': 0.9101783633232117},    
    # {'label': 'approval', 'score': 0.08781372010707855},    
    # {'label': 'realization', 'score': 0.023256294429302216},    
    # {'label': 'annoyance', 'score': 0.006623792927712202},    
    # {'label': 'admiration', 'score': 0.004981081001460552},    
    # {'label': 'disapproval', 'score': 0.004730119835585356},    
    # {'label': 'optimism', 'score': 0.0033590723760426044},    
    # ... and many more

#### **Conversational**

Finally, we can use models developed specifically to generate conversational
text. Since conversations require past prompts and responses to be passed to
subsequent model responses, the syntax is a little different here. However, we
start by instantiating our model using the _pipeline()_ function.

    
    
    chatbot = pipeline(model="facebook/blenderbot-400M-distill")

Next, we can use the _Conversation()_ class to handle the back-and-forth. We
initialize it with a user prompt, then pass it into the chatbot model from the
previous code block.

    
    
    from transformers import Conversation  
      
    conversation = Conversation("Hi I'm Shaw, how are you?")  
    conversation = chatbot(conversation)  
    print(conversation)  
      
    # output -> Conversation id: 9248ee7d-2a58-4355-9fba-525189fae206   
    # user >> Hi I'm Shaw, how are you?   
    # bot >>  I'm doing well. How are you doing this evening? I just got home from work. 

To keep the conversation going, we can use the _add_user_input()_ method to
add another prompt to the conversation. We then pass the conversation object
back into the chatbot.

    
    
    conversation.add_user_input("Where do you work?")  
    conversation = chatbot(conversation)  
    print(conversation)  
      
    # output -> Conversation id: 9248ee7d-2a58-4355-9fba-525189fae206   
    # user >> Hi I'm Shaw, how are you?   
    # bot >>  I'm doing well. How are you doing this evening? I just got home from work.  
    # user >> Where do you work?   
    # bot >>  I work at a grocery store. What about you? What do you do for a living? 

#### **Chatbot UI with Gradio**

While we get the base chatbot functionality with the Transformer library, this
is an inconvenient way to interact with a chatbot. To make the interaction a
bit more intuitive, we can use **Gradio** to **spin up a front end in a few
lines of Python code**.

This is done with the code shown below. At the top, we initialize two lists to
store user messages and model responses, respectively. Then we define a
function that will take the user prompt and generate a chatbot output. Next,
we create the chat UI using the Gradio _ChatInterface()_ class. Finally, we
launch the app.

    
    
    message_list = []  
    response_list = []  
      
    def vanilla_chatbot(message, history):  
        conversation = Conversation(text=message, past_user_inputs=message_list, generated_responses=response_list)  
        conversation = chatbot(conversation)  
      
        return conversation.generated_responses[-1]  
      
    demo_chatbot = gr.ChatInterface(vanilla_chatbot, title="Vanilla Chatbot", description="Enter text to start chatting.")  
      
    demo_chatbot.launch()

This will spin up the UI via a local URL. If the window does not open
automatically, you can copy and paste the URL directly into your browser.

![](https://cdn-images-1.medium.com/max/800/1*okUwxEBv2oZuUYi7Pks3sw.gif)Gradio interface. GIF
by author.

#### **Hugging Face Spaces**

To go one step further, we can quickly deploy this UI via **Hugging Face
Spaces**. These are **Git repositories hosted by Hugging Face and augmented by
computational resources**. Both free and paid options are available depending
on the use case. Here we will stick with the free option.

To make a new Space, we first go to the [Spaces
page](https://huggingface.co/spaces) and click “Create new space”. Then,
configure the Space by giving it the name e.g. “my-first-space” and selecting
Gradio as the SDK. Then hit “Create Space”.

![](https://cdn-images-1.medium.com/max/800/1*3vKV5gW4sdc6qvF7mdKUcg.png)Hugging Face Space
configuration. Image by author.

Next, we need to upload app.py and requirements.txt files to the Space. The
app.py file houses the code we used to generate the Gradio UI, and the
requirements.txt file specifies the app’s dependencies. The files for this
example are available at the [GitHub repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/hugging-face/my-first-space) and the [Hugging Face Space](https://huggingface.co/spaces/shawhin/my-first-space/tree/main).

Finally, we push the code to the Space just like we would to GitHub. The end
result is a public application hosted on Hugging Face Spaces.

**App link** : <https://huggingface.co/spaces/shawhin/my-first-space>

### **Conclusion**

Hugging Face has become synonymous with open-source language models and
machine learning. The biggest advantage of their ecosystem is it gives small-
time developers, researchers, and tinkers access to powerful ML resources.

While we covered a lot of material in this post, we’ve only scratched the
surface of what the Hugging Face ecosystem can do. In future articles of this
series, we will explore more advanced use cases and cover [how to fine-tune models](https://medium.com/towards-data-science/fine-tuning-large-language-models-llms-23473d763b91) using 🤗Transformers.