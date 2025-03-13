# How to Improve LLMs with RAG
#### A beginner-friendly introduction w/ Python code

This article is part of a [larger series](https://shawhin.medium.com/list/large-language-models-llms-8e009ae3054c) on using large language models in practice. In the
[previous post](https://towardsdatascience.com/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32), we fine-tuned Mistral-7b-Instruct to respond to
YouTube comments using QLoRA. Although the fine-tuned model successfully
captured my style when responding to viewer feedback, its responses to
technical questions didn’t match my explanations. Here, I’ll discuss how we
can improve LLM performance using retrieval augmented generation (i.e. RAG).

![](https://cdn-images-1.medium.com/max/800/1*N0Ad_oCIrAyzMYRdH3trqg.png)The
original RAG system. Image from Canva.

* * *

Large language models (LLMs) have demonstrated an impressive ability to store
and deploy vast knowledge in response to user queries. While this has enabled
the creation of powerful AI systems like ChatGPT, compressing world knowledge
in this way has **two key limitations**.

**First** , an LLM’s knowledge is static, i.e., not updated as new information
becomes available. **Second** , LLMs may have an insufficient “understanding”
of niche and specialized information that was not prominent in their training
data. These limitations can result in undesirable (and even fictional) model
responses to user queries.

One way we can mitigate these limitations is to **augment a model via a
specialized and mutable knowledge base** , e.g., customer FAQs, software
documentation, or product catalogs. This enables the creation of more robust
and adaptable AI systems.

**Retrieval augmented generation** , or **RAG** , is one such approach. Here,
I provide a high-level introduction to RAG and share example Python code for
implementing a RAG system using LlamaIndex.

### **What is RAG?**

The basic usage of an LLM consists of giving it a prompt and getting back a
response.

![](https://cdn-images-1.medium.com/max/800/1*sM1p-3FoTaGZunqx918G9A.png)Basic
usage of an LLM i.e. prompt in, response out. Image by author.

**RAG works by adding a step to this basic process**. Namely, a retrieval step
is performed where, based on the user’s prompt, the relevant information is
extracted from an external knowledge base and injected into the prompt before
being passed to the LLM.

![](https://cdn-images-1.medium.com/max/800/1*EhJZj1blu7a8EPmVAPsNcA.png)Overview of RAG
system. Image by author.

### **Why we care**

Notice that RAG does not fundamentally change how we use an LLM; it's still
_prompt-in and response-out_. RAG simply augments this process (hence the
name).

This makes **RAG a flexible and (relatively) straightforward way to improve
LLM-based systems**. Additionally, since knowledge is stored in an external
database, updating system knowledge is as simple as adding or removing records
from a table.

#### **Why not fine-tune?**

Previous articles in this series discussed [fine-tuning](https://towardsdatascience.com/fine-tuning-large-language-models-llms-23473d763b91), which adapts an existing model for a particular use case.
While this is an alternative way to endow an LLM with specialized knowledge,
empirically, **fine-tuning seems to be less effective than RAG** **at doing
this** [1].

### **How it works**

There are 2 key elements of a RAG system: a **retriever** and a **knowledge
base**.

#### **Retriever**

A retriever takes a user prompt and returns relevant items from a knowledge
base. This typically works using so-called **text embeddings** , numerical
representations of text in concept space. In other words, these are **numbers
that represent the _meaning_ of a given text**.

Text embeddings can be used to compute a similarity score between the user’s
query and each item in the knowledge base. The result of this process is a
**ranking of each item’s relevance to the input query**.

The retriever can then take the top k (say k=3) most relevant items and inject
them into the user prompt. This augmented prompt is then passed into the LLM
for generation.

![](https://cdn-images-1.medium.com/max/800/1*jpTwdBmoTlJlfPAm0oJiVQ.png)Overview of retrieval
step. Image by author.

#### **Knowledge Base**

The next key element of a RAG system is a knowledge base. This **houses all
the information you want to make available to the LLM**. While there are
countless ways to construct a knowledge base for RAG, here I’ll focus on
building one from a set of documents.

The process can be broken down into **4 key steps** [2,3].

  1. **Load docs** — This consists of gathering a collection of documents and ensuring they are in a ready-to-parse format (more on this later).
  2. **Chunk docs—** Since LLMs have limited context windows, documents must be split into smaller chunks**(e.g.,** 256 or 512 characters long).
  3. **Embed chunks** — Translate each chunk into numbers using a text embedding model.
  4. **Load into Vector DB** — Load text embeddings into a database (aka a vector database).

![](https://cdn-images-1.medium.com/max/800/1*VWG6Tr0OxCnD5Mvygm5DCA.png)Overview of knowledge
base creation. Image by author.

### **Some Nuances**

While the steps for building a RAG system are conceptually simple, several
nuances can make building one (in the real world) more complicated.

**Document preparation** —The quality of a RAG system is driven by how well
useful information can be extracted from source documents. For example, if a
document is unformatted and full of images and tables, it will be more
difficult to parse than a well-formatted text file.

**Choosing the right chunk size** —We already mentioned the need for chunking
due to LLM context windows. However, there are 2 additional motivations for
chunking.

**First** , it keeps (compute) costs down. The more text you inject into the
prompt, the more compute required to generate a completion. The **second** is
performance. Relevant information for a particular query tends to be localized
in source documents (often, just 1 sentence can answer a question). Chunking
helps minimize the amount of irrelevant information passed into the model [4].

**Improving search** — While text embeddings enable a powerful and fast way to
do search, it doesn’t always work as one might hope. In other words, it may
return results that are “similar” to the user query, yet not helpful for
answering it, e.g., “ _How’s the weather in LA?_ ” may return “ _How’s the
weather in NYC?_ ”.

The simplest way to mitigate this is through good document preparation and
chunking. However, for some use cases, additional strategies for improving
search might be necessary, such as using **meta-tags** for each chunk,
employing **hybrid search** , which combines keyword—and embedding-based
search, or using a **reranker** , which is a specialized model that computes
the similarity of 2 input pieces of text.

### **Example code: Improving YouTube Comment Responder with RAG**

With a basic understanding of how RAG works, let’s see how to use it in
practice. I will build upon the example from the [previous article](https://towardsdatascience.com/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32), where I fine-tuned Mistral-7B-Instruct to respond to
YouTube comments using QLoRA. We will use LlamaIndex to add a RAG system to
the fine-tuned model from before.

The example code is freely available in a [Colab Notebook](https://colab.research.google.com/drive/1peJukr-9E1zCo1iAalbgDPJmNMydvQms?usp=sharing),
which can run on the (free) T4 GPU provided. The source files for this example
are available at the [GitHub repository](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/rag).

🔗 [Google Colab](https://colab.research.google.com/drive/1peJukr-9E1zCo1iAalbgDPJmNMydvQms?usp=sharing) | [GitHub Repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/rag)

* * *

#### **Imports**

We start by installing and importing necessary Python libraries.

    
    
    !pip install llama-index  
    !pip install llama-index-embeddings-huggingface  
    !pip install peft  
    !pip install auto-gptq  
    !pip install optimum  
    !pip install bitsandbytes  
    # if not running on Colab ensure transformers is installed too
    
    
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding  
    from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex  
    from llama_index.core.retrievers import VectorIndexRetriever  
    from llama_index.core.query_engine import RetrieverQueryEngine  
    from llama_index.core.postprocessor import SimilarityPostprocessor

#### **Setting up Knowledge Base**

We can configure our knowledge base by defining our embedding model, chunk
size, and chunk overlap. Here, we use the ~33M parameter [bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) embedding model from
BAAI, which is available on the Hugging Face hub. Other embedding model
options are available on this [text embedding leaderboard](https://huggingface.co/spaces/mteb/leaderboard).

    
    
    # import any embedding model on HF hub  
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")  
      
    Settings.llm = None # we won't use LlamaIndex to set up LLM  
    Settings.chunk_size = 256  
    Settings.chunk_overlap = 25

Next, we load our source documents. Here, I have a folder called “[_articles_](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/rag/articles),” which contains PDF versions of 3 Medium
articles I wrote on [fat tails](https://towardsdatascience.com/pareto-power-laws-and-fat-tails-0355a187ee6a). If running this in Colab, you must download
the articles folder from the [GitHub repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/rag) and
manually upload it to your Colab environment.

For each file in this folder, the function below will read the text from the
PDF, split it into chunks (based on the settings defined earlier), and store
each chunk in a list called _documents_.

    
    
    documents = SimpleDirectoryReader("articles").load_data()

Since the blogs were downloaded directly as PDFs from Medium, they resemble a
webpage more than a well-formatted article. Therefore, some chunks may include
text unrelated to the article, e.g., webpage headers and Medium article
recommendations.

In the code block below, I refine the chunks in documents, removing most of
the chunks before or after the meat of an article.

    
    
    print(len(documents)) # prints: 71  
    for doc in documents:  
        if "Member-only story" in doc.text:  
            documents.remove(doc)  
            continue  
      
        if "The Data Entrepreneurs" in doc.text:  
            documents.remove(doc)  
      
        if " min read" in doc.text:  
            documents.remove(doc)  
      
    print(len(documents)) # prints: 61

Finally, we can store the refined chunks in a vector database.

    
    
    index = VectorStoreIndex.from_documents(documents)

#### **Setting up Retriever**

With our knowledge base in place, we can create a retriever using LlamaIndex’s
_VectorIndexRetreiver(),_ which returns the top 3 most similar chunks to a
user query.

    
    
    # set number of docs to retreive  
    top_k = 3  
      
    # configure retriever  
    retriever = VectorIndexRetriever(  
        index=index,  
        similarity_top_k=top_k,  
    )

Next, we define a query engine that uses the retriever and query to return a
set of relevant chunks.

    
    
    # assemble query engine  
    query_engine = RetrieverQueryEngine(  
        retriever=retriever,  
        node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.5)],  
    )

#### **Use Query Engine**

Now, with our knowledge base and retrieval system set up, let’s use it to
return chunks relevant to a query. Here, we’ll pass the same technical
question we asked ShawGPT (the YouTube comment responder) from the [previous article](https://medium.com/towards-data-science/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32).

    
    
    query = "What is fat-tailedness?"  
    response = query_engine.query(query)

The query engine returns a response object containing the text, metadata, and
indexes of relevant chunks. The code block below returns a more readable
version of this information.

    
    
    # reformat response  
    context = "Context:\n"  
    for i in range(top_k):  
        context = context + response.source_nodes[i].text + "\n\n"  
      
    print(context)
    
    
    Context:  
    Some of the controversy might be explained by the observation that log-  
    normal distributions behave like Gaussian for low sigma and like Power Law  
    at high sigma [2].  
    However, to avoid controversy, we can depart (for now) from whether some  
    given data fits a Power Law or not and focus instead on fat tails.  
    Fat-tailedness — measuring the space between Mediocristan  
    and Extremistan  
    Fat Tails are a more general idea than Pareto and Power Law distributions.  
    One way we can think about it is that “fat-tailedness” is the degree to which  
    rare events drive the aggregate statistics of a distribution. From this point of  
    view, fat-tailedness lives on a spectrum from not fat-tailed (i.e. a Gaussian) to  
    very fat-tailed (i.e. Pareto 80 – 20).  
    This maps directly to the idea of Mediocristan vs Extremistan discussed  
    earlier. The image below visualizes different distributions across this  
    conceptual landscape [2].  
      
    print("mean kappa_1n = " + str(np.mean(kappa_dict[filename])))  
        print("")  
    Mean κ (1,100) values from 1000 runs for each dataset. Image by author.  
    These more stable results indicate Medium followers are the most fat-tailed,  
    followed by LinkedIn Impressions and YouTube earnings.  
    Note: One can compare these values to Table III in ref [3] to better understand each  
    κ value. Namely, these values are comparable to a Pareto distribution with α  
    between 2 and 3.  
    Although each heuristic told a slightly different story, all signs point toward  
    Medium followers gained being the most fat-tailed of the 3 datasets.  
    Conclusion  
    While binary labeling data as fat-tailed (or not) may be tempting, fat-  
    tailedness lives on a spectrum. Here, we broke down 4 heuristics for  
    quantifying how fat-tailed data are.  
      
    Pareto, Power Laws, and Fat Tails  
    What they don’t teach you in statistics  
    towardsdatascience.com  
    Although Pareto (and more generally power law) distributions give us a  
    salient example of fat tails, this is a more general notion that lives on a  
    spectrum ranging from thin-tailed (i.e. a Gaussian) to very fat-tailed (i.e.  
    Pareto 80 – 20).  
    The spectrum of Fat-tailedness. Image by author.  
    This view of fat-tailedness provides us with a more flexible and precise way of  
    categorizing data than simply labeling it as a Power Law (or not). However,  
    this begs the question: how do we define fat-tailedness?  
    4 Ways to Quantify Fat Tails

#### **Adding RAG to LLM**

We start by downloading the [fine-tuned model](https://medium.com/towards-data-science/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32) from
the Hugging Face hub.

    
    
    # load fine-tuned model from hub  
    from peft import PeftModel, PeftConfig  
    from transformers import AutoModelForCausalLM, AutoTokenizer  
      
    model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"  
    model = AutoModelForCausalLM.from_pretrained(model_name,  
                                                 device_map="auto",  
                                                 trust_remote_code=False,  
                                                 revision="main")  
      
    config = PeftConfig.from_pretrained("shawhin/shawgpt-ft")  
    model = PeftModel.from_pretrained(model, "shawhin/shawgpt-ft")  
      
    # load tokenizer  
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

As a baseline, we can see how the model responds to the technical question
without any context from the articles. To do this, we create a prompt template
using a lambda function, which takes in a viewer comment and returns a prompt
for the LLM. For more details on where this prompt comes from, see the
[previous article](https://towardsdatascience.com/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32#5aad) of this series.

    
    
    # prompt (no context)  
    intstructions_string = f"""ShawGPT, functioning as a virtual data science \  
    consultant on YouTube, communicates in clear, accessible language, escalating \  
    to technical depth upon request. It reacts to feedback aptly and ends \  
    responses with its signature '–ShawGPT'.  
      
    ShawGPT will tailor the length of its responses to match the viewer's comment, \  
    providing concise acknowledgments to brief expressions of gratitude or \  
    feedback, thus keeping the interaction natural and engaging.  
      
    Please respond to the following comment.  
    """  
      
    prompt_template = lambda comment: f'''[INST] {intstructions_string} \n{comment} \n[/INST]'''  
    comment = "What is fat-tailedness?"  
      
    prompt = prompt_template(comment)  
    print(prompt)
    
    
    [INST] ShawGPT, functioning as a virtual data science consultant on YouTube, communicates in clear, accessible language, escalating to technical depth upon request. It reacts to feedback aptly and ends responses with its signature '–ShawGPT'. ShawGPT will tailor the length of its responses to match the viewer's comment, providing concise acknowledgments to brief expressions of gratitude or feedback, thus keeping the interaction natural and engaging.  
      
    Please respond to the following comment.  
       
    What is fat-tailedness?   
    [/INST]

Next, we can pass this prompt to the model using the code below.

    
    
    model.eval()  
      
    inputs = tokenizer(prompt, return_tensors="pt")  
    outputs = model.generate(input_ids=inputs["input_ids"].to("cuda"),   
                              max_new_tokens=280)  
      
    print(tokenizer.batch_decode(outputs)[0])

Here’s the model’s response (no context).

    
    
    Great question!  
      
    Fat-tailedness is a statistical property of a distribution. In simple terms,   
    it refers to the presence of extreme outliers or heavy tails in the   
    distribution.  
      
    For instance, consider the distribution of heights in a population. A normal   
    distribution would have most people clustered around an average height with a   
    few people deviating slightly from the mean. However, in a fat-tailed   
    distribution, you would observe a larger number of people being significantly   
    taller or shorter than the average.  
      
    In finance, fat-tailedness is often used to describe the presence of extreme   
    market moves or outliers in financial returns. It's an important concept in   
    risk management and financial modeling.  
      
    I hope this explanation helps! Let me know if you have any questions.  
    –ShawGPT

Although the response's style and formatting are great, the model's
explanation of fat-tailedness differs from how I defined it in my
[video](https://www.youtube.com/playlist?list=PLz-ep5RbHosVrT89BRNX-IGKHYxvx9wqi) and [blog series](https://towardsdatascience.com/pareto-power-laws-and-fat-tails-0355a187ee6a).

Let’s see what happens to the model’s response when we include the appropriate
context. To do this, we create another prompt template, which can also take in
context from the RAG system.

    
    
    # prompt (with context)  
    prompt_template_w_context = lambda context, comment: f"""[INST]ShawGPT, functioning as a virtual data science consultant on YouTube, communicates in clear, accessible language, escalating to technical depth upon request. \  
    It reacts to feedback aptly and ends responses with its signature '–ShawGPT'. \  
    ShawGPT will tailor the length of its responses to match the viewer's comment, providing concise acknowledgments to brief expressions of gratitude or feedback, \  
    thus keeping the interaction natural and engaging.  
      
    {context}  
    Please respond to the following comment. Use the context above if it is helpful.  
      
    {comment}  
    [/INST]  
    """

Next, we pass the prompt with context from the query engine and the view
comment to the model.

    
    
    prompt = prompt_template_w_context(context, comment)  
      
    inputs = tokenizer(prompt, return_tensors="pt")  
    outputs = model.generate(input_ids=inputs["input_ids"].to("cuda"), max_new_tokens=280)  
      
    print(tokenizer.batch_decode(outputs)[0])

Here’s the new response (with context).

    
    
    Great question!  
      
    Fat-tailedness is a property of a distribution that describes how much the   
    presence of extreme values (rare events) affects the overall statistics of the   
    distribution.  
      
    In the context of the video, the author discusses how Mediocristan and   
    Extremistan distributions differ in terms of fat-tailedness. Mediocristan   
    distributions have a relatively small impact from extreme values, while   
    Extremistan distributions are heavily influenced by extreme values.  
      
    The author also mentions that fat-tailedness is a more general concept than   
    specific distributions like Pareto or Power Laws. Instead, it lives on a   
    spectrum ranging from thin-tailed (Gaussian) to very fat-tailed (Pareto 80-20).  
      
    I hope that helps clarify things a bit! Let me know if you have any questions.  
    –ShawGPT

This does a much better job of capturing my explanation of fat tails than the
no-context response and even calls out the niche concepts of Mediocristan and
Extremistan.

### **What’s next?**

Here, I gave a beginner-friendly introduction to RAG and shared a concrete
example of how to implement it using LlamaIndex. RAG allows us to improve an
LLM system with updateable and domain-specific knowledge.

While much of the recent AI hype has centered around building AI assistants, a
powerful (yet less popular) innovation has come from text embeddings (i.e. the
things we used to do retrieval). In the next article of this series, I will
explore **text embeddings** in more detail, including how they can be used for
**semantic search** and **classification tasks**.