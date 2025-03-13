# How to Build an AI Assistant with OpenAI + Python
#### Step-by-step guide on using the Assistants API & Fine-tuning

![](https://cdn-images-1.medium.com/max/800/1*Nfv158mYjlryAvAd2q07eg.png)Image
from Canva.

One of the most common asks I get from clients is, “How can I make a custom
chatbot with my data?” While 6 months ago, this could take months to
develop, today, that is not necessarily the case. In this article, I present a
step-by-step guide on how to create a custom AI using OpenAI’s Assistants and
Fine-tuning APIs. Python [example code](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/ai-assistant-openai) is provided for each approach.

* * *

### **Chatbot vs. Assistant**

Before diving into the example code, I want to briefly differentiate an AI
chatbot from an assistant. While these terms are often used interchangeably,
here, I use them to mean different things.

A **chatbot** is **an AI you can have a conversation with** , while an **AI
assistant** is **a chatbot that can use tools**. A tool can be things like web
browsing, a calculator, a Python interpreter, or anything else that expands
the capabilities of a chatbot [1].

For example, if you use the free version of ChatGPT, that’s a chatbot because
it only comes with a basic chat functionality. However, if you use the premium
version of ChatGPT, that’s an assistant because it comes with capabilities
such as web browsing, knowledge retrieval, and image generation.

### **Assistants API**

While building AI assistants (i.e., AI agents) is not a new idea, OpenAI’s new
Assistants API provides a straightforward way to create these types of AIs.
Here, I’ll use the API to make a YouTube comment responder equipped with
knowledge retrieval (i.e. RAG) from one of my Medium articles. The following
example code is available at this post’s [GitHub repository](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/ai-assistant-openai).

#### **Vanilla Assistant**

We start by importing Python libraries and setting up communication with the
OpenAI API.

    
    
    from openai import OpenAI  
    from sk import my_sk # import secret key from .py file  
      
    client = OpenAI(api_key=my_sk)

Note that for this step, you need an OpenAI API key. If you don’t have an API
key or don’t know how to get one, I walk through how to do that in a [previous article](https://medium.com/towards-data-science/cracking-open-the-openai-python-api-230e4cae7971). Here, I have my secret key defined in a separate
Python file called sk.py, which was imported in the above code block.

Now we can create a basic assistant (_technically a chatbot since no tools
yet_). This can be done in one line of code, but I use a few more for
readability.

    
    
    intstructions_string = "ShawGPT, functioning as a virtual data science \  
    consultant on YouTube, communicates in clear, accessible language, escalating \  
    to technical depth upon request. \  
    It reacts to feedback aptly and concludes with its signature '–ShawGPT'. \  
    ShawGPT will tailor the length of its responses to match the viewer's comment, \  
    providing concise acknowledgments to brief expressions of gratitude or \  
    feedback, thus keeping the interaction natural and engaging."  
      
    assistant = client.beta.assistants.create(  
        name="ShawGPT",  
        description="Data scientist GPT for YouTube comments",  
        instructions=intstructions_string,  
        model="gpt-4-0125-preview"  
    )

As shown above, we can set the assistant _name_ , _description_ ,
_instructions_ , and _model_. The inputs most relevant to the assistant’s
performance are the _instructions_ and _model_. Developing good instructions
(i.e. [prompt engineering](https://medium.com/towards-data-science/prompt-engineering-how-to-trick-ai-into-solving-your-problems-7ce1ed3b553f)) is an
iterative process but worth spending some time on. Additionally, I use the
latest available version of GPT-4. However, older (and cheaper) models are
also [available](https://platform.openai.com/docs/models/continuous-model-upgrades) [2].

With the “assistant” set up, we can send it a message to generate a response.
This is done in the code block below.

    
    
    # create thread (i.e. object that handles conversation between user and assistant)  
    thread = client.beta.threads.create()  
      
    # add a user message to the thread  
    message = client.beta.threads.messages.create(  
        thread_id=thread.id,  
        role="user",  
        content="Great content, thank you!"  
    )  
      
    # send message to assistant to generate a response  
    run = client.beta.threads.runs.create(  
      thread_id=thread.id,  
      assistant_id=assistant.id,  
    )

A few things are happening in the above code block. **First** , we create a
thread object. This handles message passing between user and assistant, thus
avoiding the need for us to write boilerplate code to do that. **Next** , we
add a user message to the thread. These are the YouTube comments for our use
case. **Then** , finally, we send the thread to the assistant to generate a
response via the run object.

After a few seconds, we get the following response from the assistant:

    
    
    You're welcome! I'm glad you found it helpful. If you have any more questions   
    or topics you're curious about, feel free to ask. –ShawGPT

While this might seem like a nice response, it’s not something I would ever
say. Let’s see how we can improve the assistant via so-called few-shot
prompting.

#### **Few-shot Prompting**

Few-shot prompting is where **we include input-output examples in the
assistant’s instructions from which it can learn**. Here, I append 3 (real)
comments and responses to the previous instruction string.

    
    
    intstructions_string_few_shot = """ShawGPT, functioning as a virtual data \  
    science consultant on YouTube, communicates in clear, accessible language, \  
    escalating to technical depth upon request. \  
    It reacts to feedback aptly and concludes with its signature '–ShawGPT'. \  
    ShawGPT will tailor the length of its responses to match the viewer's comment, \  
    providing concise acknowledgments to brief expressions of gratitude or \  
    feedback, thus keeping the interaction natural and engaging.  
      
    Here are examples of ShawGPT responding to viewer comments.  
      
    Viewer comment: This was a very thorough introduction to LLMs and answered many questions I had. Thank you.  
    ShawGPT: Great to hear, glad it was helpful :) -ShawGPT  
      
    Viewer comment: Epic, very useful for my BCI class  
    ShawGPT: Thanks, glad to hear! -ShawGPT  
      
    Viewer comment: Honestly the most straightforward explanation I've ever watched. Super excellent work Shaw. Thank you. It's so rare to find good communicators like you!  
    ShawGPT: Thanks, glad it was clear -ShawGPT"""

Notice that I added the sign-off “ _— ShawGPT_ ” to each example (even though
those weren’t part of my _actual_ response). This is important to get the
desired behavior from the assistant.

With the updated instructions, we can create a new assistant in the same way
as before.

    
    
    assistant = client.beta.assistants.create(  
        name="ShawGPT",  
        description="Data scientist GPT for YouTube comments",  
        instructions=intstructions_string_few_shot,  
        model="gpt-4-0125-preview"  
    )

Passing the same test comment (i.e. “ _Great content, thank you!_ ”) to this
assistant as before, we now get the following response:

    
    
    You're welcome, happy to hear you found it useful! -ShawGPT

Although this is (still) a little longer than my typical response, it is much
better than what we saw with the vanilla assistant.

Let’s try another (more technical) question. We can use the same syntax as
before to pass the user message to the assistant, but now let’s ask, “ _What
is fat-tailedness?_ ”

Here’s the assistant response.

    
    
    Fat-tailedness is a concept from statistics that refers to the properties of a   
    particular type of probability distribution. In a fat-tailed distribution, the   
    tails (the far ends of the distribution, representing extreme values far from   
    the mean) are heavier or "fatter" than they would be in a normal (Gaussian)   
    distribution. This means there's a higher likelihood of extreme outcomes   
    occurring compared to what you would expect if the data followed a normal   
    distribution.  
      
    In practical terms, if a dataset is described as having a fat-tailed   
    distribution, it indicates that rare, extreme events (the ones in the tails)   
    happen more frequently than would be predicted by models based on normal   
    distributions. This concept is extremely important in fields like finance,   
    economics, and risk management, where underestimating the likelihood of extreme  
    events can have significant consequences.  
      
    Fat-tailed distributions contrast with thin-tailed distributions, like the   
    normal distribution, where extreme values are less likely, and most of the   
    probabilities are concentrated around the mean. Understanding whether a dataset  
    follows a fat-tailed distribution can significantly impact how we model and   
    predict phenomena, especially when it comes to assessing risks and anticipating  
    rare but impactful events. -ShawGPT

While (again) this response is reasonable, it reads more like something from
ChatGPT than what I would say. Namely, it uses a different definition of fat
tails (i.e. a distribution with heavier tails than a normal distribution) than
the one I use in [my series](https://towardsdatascience.com/pareto-power-laws-and-fat-tails-0355a187ee6a) on the topic (i.e. a distribution driven by extreme events).

To improve this aspect of the assistant’s responses, we can give it the
ability to access knowledge from a [Medium article](https://medium.com/towards-data-science/4-ways-to-quantify-fat-tails-with-python-10ce62c0ada1) I’ve written on fat-tailedness.

#### **Knowledge Retrieval**

While setting up a RAG system consists of a handful of nontrivial steps (i.e.
chunking documents, setting up vector database, building semantic search
function, fusing search results into context window), the **entire process is
reduced to 2 steps** in the Assistants API.

**First** , we upload our documents for retrieval. **Second** , we added the
retrieval capability to our assistant.

In the code block below, I upload my article on [quantifying fat tails](https://towardsdatascience.com/4-ways-to-quantify-fat-tails-with-python-10ce62c0ada1) to my OpenAI account. To do this, we need to specify the
file path/name and the purpose of the file. Here, we set the purpose as “
_assistants_ ”. The other option is “ _fine-tune_ ”, which we will see soon.

    
    
    file = client.files.create(  
      file=open("articles/4 Ways to Quantify Fat Tails with Python _ by Shaw Talebi _ Towards Data Science.pdf", "rb"),  
      purpose="assistants"  
    )

Next, we can create a new assistant similar to before, but now enabling
retrieval and specifying the files available to the assistant. While I only
use one document for retrieval here, **we can specify up to 20 files** by
including the associated file IDs in the _file_ids_ list.

    
    
    assistant = client.beta.assistants.create(  
        name="ShawGPT",  
        description="Data scientist GPT for YouTube comments",  
        instructions=intstructions_string_few_shot,  
        tools=[{"type": "retrieval"}],  
        file_ids=[file.id],  
        model="gpt-4-0125-preview"  
    )

Passing the same technical question to the assistant, we get the following
response.

    
    
    Fat-tailedness describes the degree to which rare events significantly   
    contribute to the aggregate statistics of a distribution. This concept   
    highlights that in certain distributions, a small number of observations can   
    disproportionately influence the overall picture. A classic example is the   
    Pareto distribution, often referenced in the context of wealth distribution,   
    where a small proportion of individuals can hold the majority of wealth. In   
    statistical terms, distributions range from thin-tailed (e.g., Gaussian, where   
    extreme events are highly improbable) to very fat-tailed (e.g., Pareto, where   
    extreme events are less rare than in Gaussian distributions).  
      
    Fat-tailedness is not about a binary categorization of distributions as either   
    "Power Law" or not but recognizes a continuum or spectrum of "tail heaviness."   
    This understanding offers a more nuanced view, allowing for more accurate and   
    precise categorization of data distributions. Identifying and quantifying the   
    fat-tailed nature of a dataset is important in fields like finance, insurance,   
    risk management, and social sciences, where understanding the likelihood and   
    impact of extreme events is crucial.  
      
    In practical terms, fat-tailedness can be quantified using different heuristics,  
    which may involve mathematical computations such as the Power Law Tail Index,   
    Kurtosis, Log-normal's σ, and Taleb's κ metric. Each of these measures offers   
    a different lens through which to assess the fat-tailed nature of a   
    distribution, thereby providing useful insights into the behavior of extreme   
    events within the dataset -ShawGPT

This response is much closer to the way I think about (and explain) [fat-tailedness](https://towardsdatascience.com/pareto-power-laws-and-fat-tails-0355a187ee6a). The assistant did a seamless job of incorporating key
concepts from [the article](https://towardsdatascience.com/4-ways-to-quantify-fat-tails-with-python-10ce62c0ada1) into its response. For instance, defining
fat-tailedness in terms of rare events, fat-tailedness living on a spectrum,
and four heuristics for measuring them.

Up to this point, we’ve gotten pretty far using [**prompt
engineering**](https://medium.com/towards-data-science/prompt-engineering-how-to-trick-ai-into-solving-your-problems-7ce1ed3b553f) and **knowledge
retrieval** to create our assistant. However, the responses still don’t
entirely read like something I would write. To further improve this aspect of
the assistant, we can turn to fine-tuning.

### **Fine-tuning API**

While [prompt engineering](https://medium.com/towards-data-science/prompt-engineering-how-to-trick-ai-into-solving-your-problems-7ce1ed3b553f) can be an
easy way to program an assistant, it is **not always obvious how to best
instruct the model** to demonstrate the desired behavior. In these situations,
it can be advantageous to fine-tune the model.

[**Fine-tuning**](https://medium.com/towards-data-science/fine-tuning-large-language-models-llms-23473d763b91) is when we**train a pre-existing model with
additional examples for a particular task**. In the OpenAI Fine-tuning API
this consists of providing example user-assistant message pairs [3].

For the YouTube comment responder use case, this means gathering pairs of
viewer comments (i.e., user message) and their associated responses (i.e.,
assistant message).

Although this additional data-gathering process makes fine-tuning more work
upfront, it **can lead to significant improvements** in model performance [3].
Here, I walk through the fine-tuning process for this particular use case.

#### **Data Preparation**

To generate the user-assistant message pairs, I manually went through past
YouTube comments and copy-pasted them into a spreadsheet. I then exported this
spreadsheet as a .csv file (available at the [GitHub
repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/ai-assistant-openai)).

While this .csv file has all the critical data needed for fine-tuning, **it
cannot be used directly**. We must first transform it into a particular format
to pass it into the OpenAI API.

More specifically, we need to generate a **.jsonl file** , a text file where
each line corresponds to a training example in the JSON format. If you are a
Python user unfamiliar with JSON, you can think of it like a dictionary (i.e.
a data structure consisting of key-value pairs) [4].

To get our .csv into the necessary .jsonl format, I first create Python lists
for each type of comment. This is done by reading the raw .csv file line by
line and storing each message in the appropriate list.

    
    
    import csv  
    import json  
    import random  
      
    comment_list = []  
    response_list = []  
      
    with open('data/YT-comments.csv', mode ='r') as file:  
        file = csv.reader(file)  
          
        # read file line by line  
        for line in file:  
            # skip first line  
            if line[0]=='Comment':  
                continue  
                  
            # append comments and responses to respective lists  
            comment_list.append(line[0])  
            response_list.append(line[1] + " -ShawGPT")

Next, to create the .jsonl file, we must create a list of dictionaries where
each element corresponds to a training example. The **key** for each of these
dictionaries is “ _messages_ ”, and the **value** is (yet another) _list of
dictionaries_ corresponding to the system, user, and assistant messages,
respectively. A visual overview of this data structure is given below.

![](https://cdn-images-1.medium.com/max/800/1*yBNfKblgoHUQ8CyIedJtdw.png)Overview of fine-
tuning training data format [4]. Image by author.

The Python code for taking our _comment_list_ and _response_list_ objects and
creating the list of examples is given below. This is done by going through
_comment_list_ and _response_list_ , element by element, and creating three
dictionaries at each step.

These correspond to the system, user, and assistant messages, respectively,
where the system message is the same instructions we used to make our
assistant via few-shot prompting, and the user/assistant messages come from
their respective lists. These dictionaries are then stored in a list that
serves as the value for that particular training example.

    
    
    example_list = []  
      
    for i in range(len(comment_list)):  
        # create dictionaries for each role/message      
        system_dict = {"role": "system", "content": intstructions_string_few_shot}  
        user_dict = {"role": "user", "content": comment_list[i]}  
        assistant_dict = {"role": "assistant", "content": response_list[i]}  
          
        # store dictionaries into list  
        messages_list = [system_dict, user_dict, assistant_dict]  
          
        # create dictionary for ith example and add it to example_list  
        example_list.append({"messages": messages_list})

At the end of this process, we have a list with 59 elements corresponding to
59 user-assistant example pairs. Another step that helps evaluate model
performance is to split these 59 examples into two datasets, one for
**training the model** and the other for **evaluating its performance**.

This is done in the code block below, where I randomly sample 9 out of 59
examples from _example_list_ and store them in a new list called
_validation_data_list_. These examples are then removed from _example_list_ ,
which will serve as our training dataset.

    
    
    # create train/validation split  
    validation_index_list = random.sample(range(0, len(example_list)-1), 9)  
      
    validation_data_list = [example_list[index] for index in validation_index_list]  
      
    for example in validation_data_list:  
        example_list.remove(example)

Finally, with our training and validation datasets prepared, we can write them
to .jsonl files. This can be done in the following way.

    
    
    # write examples to file  
    with open('data/training-data.jsonl', 'w') as training_file:  
        for example in example_list:  
            json.dump(example, training_file)  
            training_file.write('\n')  
      
    with open('data/validation-data.jsonl', 'w') as validation_file:  
        for example in validation_data_list:  
            json.dump(example, validation_file)  
            validation_file.write('\n')

#### **Fine-tuning job**

With the data preparation done, we can run the fine-tuning job in 2 steps.
**First** , we upload the training and validation files to our OpenAI account.
**Second** , we run the training process [3].

We upload files like we did when setting up document retrieval for an
assistant, but now setting the file purpose as “ _fine-tune_ ”. This is done
for both the training and validation datasets below.

    
    
    # upload fine-tuning files  
    training_file = client.files.create(  
      file = open("data/training-data.jsonl", "rb"),  
      purpose = "fine-tune"  
    )  
      
    validation_file = client.files.create(  
      file = open("data/validation-data.jsonl", "rb"),  
      purpose = "fine-tune"  
    )

Now, we can run the fine-tuning job. For this, we need to specify the training
files and model we wish to fine-tune. The most advanced model available for
fine-tuning is _gpt-3.5-turbo_ , which I use here. I also set a suffix that
adds a user-defined string to the fine-tuned model’s ID. The code for this is
shown below.

    
    
    client.fine_tuning.jobs.create(  
        training_file = training_file.id,  
        validation_file = validation_file.id,  
        suffix = "ShawGPT",  
        model = "gpt-3.5-turbo"  
    )

The training process will take around 15 minutes. When complete, we can use
the fine-tuned model via the completions API, as shown below.

    
    
    test_comment = "Great content, thank you!"  
      
    response = client.chat.completions.create(  
        model="ft:gpt-3.5-turbo-0613:personal:shawgpt:8mUeVreo",  
        messages=[  
        {"role": "system", "content": intstructions_string_few_shot},  
        {"role": "user", "content": test_comment}  
        ]  
    )

Notice how we generated the response in the code block above differs from how
we did it previously. This is because fine-tuned models are **not currently
supported in the Assistants API**.

The biggest downside is that if we want to augment the fine-tuned model with
tools (i.e. make it an assistant), we must build out those functionalities via
libraries like LangChain or LlamaIndex (for example).

While this makes developing a fine-tuned assistant more work, the responses we
see out of the box **are closer to something that I would say**. Here are a
few responses to the test comment.

    
    
    Thanks, I appreciate it! -ShawGPT  
    Thanks, glad you liked it! -ShawGPT  
    Glad it was helpful! -ShawGPT

Let’s see how it handles the same technical question as before i.e. “ _What is
fat-tailedness?_ ”

    
    
    Good question! The fat tail phenomenon represents the size of outlier (extreme)   
    events relative to a normal (Gaussian) distribution. In other words, there's a   
    greater probability of extreme events occurring compared to a normal   
    distribution. -ShawGPT

Although the model defines fat tails in different terms than I would, the
length and style of the response are much better than what we saw with the
Assistants API pre-RAG. This suggests that if we were to add RAG to this fine-
tuned model, it would generate significantly better responses than what we saw
before.

### **What’s Next?**

Building a custom AI assistant is easier than ever before. Here, we saw a
simple way to create an AI assistant via OpenAI’s Assistant’s API and how to
fine-tune a model via their Fine-tuning API.

While OpenAI currently has the most advanced models for developing the type of
AI assistant discussed here, these models are locked behind their API, which
limits what/how we can build with them.

A natural question, therefore, is how might we develop similar systems using
open-source solutions. This will be covered in the next articles of this
series, where I will discuss how to [fine-tune a model using
QLoRA](https://towardsdatascience.com/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32) and augment a chatbot via
[RAG](https://medium.com/towards-data-science/how-to-improve-llms-with-rag-abdc132f76ac).