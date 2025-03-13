# Multimodal RAG: Process Any File Type with AI
#### A beginner-friendly guide with example (Python) code

This is the third article in a [larger series](https://shawhin.medium.com/list/multimodal-ai-fe9521d0e77a) on
multimodal AI. In the previous posts, we discussed [multimodal LLMs](https://towardsdatascience.com/multimodal-models-llms-that-can-see-and-hear-5c6737c981d3) and [embedding models](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f), respectively. In this article, we will combine
these ideas to enable the development of multimodal RAG systems. I’ll start by
reviewing key concepts and then share example code for implementing such a
system.

![](https://cdn-images-1.medium.com/max/800/1*KUfCT0odhqkTsPzf1ljx6A.png)Image
from Canva.

* * *

Language models like GPT, LLaMA, and Claude learn a tremendous amount of world
knowledge via their pre-training. This makes them powerful tools for solving
custom problems and answering complex questions.

However, **there is knowledge that even the most advanced language models are
ignorant of**. This includes proprietary information within organizations,
events that occurred after a model's pre-training data collection, and
specialized knowledge that is not prevalent on the internet.

Although this ignorance limits a model’s out-of-the-box capabilities, there is
**a popular technique to overcome these limitations** : retrieval augmented
generation (or RAG for short).

### **What is RAG?**

**RAG** is an approach for**improving a model’s response quality by
dynamically providing the relevant context** for a given prompt. Here’s an
example of when this might be helpful.

Say, I forgot the name of a Python library a colleague mentioned in
yesterday’s meeting. This isn’t something ChatGPT can help me with because it
does not know the meeting’s contents.

However, RAG could help with this by taking my question (e.g. “What was the
name of that Python library that Rachel mentioned in yesterday’s meeting?”),
automatically pulling the meeting transcript, then providing my original query
and the transcript to an LLM.

![](https://cdn-images-1.medium.com/max/800/1*STVyqpJkhoKZWYdR-2-xqA.png)Basic
design of a RAG system. Image by author.

### **Multimodal RAG**

Although improving LLMs with RAG unlocks several practical use cases, there
are some situations where relevant information exists in non-text formats,
e.g., images, videos, charts, and tables. In such cases, we can go one step
further and build **multimodal RAG systems** , **AI systems capable of
processing text and non-text data**.

Multimodal RAG enables more sophisticated inferences beyond what is conveyed
by text alone. For example, it could analyze someone’s facial expressions and
speech tonality to give a richer context to a meeting’s transcription.

![](https://cdn-images-1.medium.com/max/800/1*mqRCTYThFcZmGcVtw6s1cw.png)Basic
design of a Multimodal RAG system. Image by author.

### **3 Levels of MRAG**

While there are several ways to implement a multimodal RAG (MRAG) system, here
I will focus on three basic strategies at increasing levels of sophistication.

  1. Translate modalities to text.
  2. Text-only retrieval + MLLM
  3. Multimodal retrieval + MLLM

The following discussion assumes **you already have a basic understanding of
RAG and multimodal models**. The following articles discussed these topics:
[RAG](https://towardsdatascience.com/how-to-improve-llms-with-rag-abdc132f76ac), [Multimodal LLMs](https://towardsdatascience.com/multimodal-models-llms-that-can-see-and-hear-5c6737c981d3), and [Multimodal Embeddings](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f).

#### **Level 1: Translate modalities to text**

A simple way to make a RAG system multimodal is by **translating new
modalities to text before storing them in the knowledge base**. This could be
as simple as converting meeting recordings into text transcripts, using an
existing multimodal LLM (MLLM) to generate image captions, or converting
tables to a readable text format (e.g., .csv or .json).

![](https://cdn-images-1.medium.com/max/800/1*7QqhRIlnU7TQsCMnVDb6KA.png)Visual overview of
Level 1 of MRAG. Image by author.

The key upside of this approach is that it **requires minimal changes to an
existing RAG system**. Additionally, by explicitly generating text
representations of non-text modalities, one has better control over the
features of the data to extract. For instance, captions of analytical figures
may include both a description and key insights.

Of course, the downside of this strategy is that the **model’s responses
cannot directly use non-textual data** , which means that the translation
from, say, image to text can create a critical information bottleneck.

#### **Level 2: Text-only retrieval + MLLM**

Another approach is to generate text representations of all items in the
knowledge base, e.g., descriptions and meta-tags, for retrieval, but to **pass
the original modality to a multimodal LLM (MLLM)**. For example, image
metadata is used for the retrieval step, and the associated image is passed to
a model for inference.

![](https://cdn-images-1.medium.com/max/800/1*JoUZLYezY3q95zngSmDJIA.png)Visual overview of
Level 2 of MRAG. Image by author.

This maintains many of the benefits of Level 1 while mitigating its
limitations. Namely, text features of items in the knowledge base can be
optimized for search, but the downstream model can use the full richness of
each item’s original modality.

The key difference with this approach is that it requires an **MLLM** , which
is **an LLM capable of processing non-text data**. This unlocks more advanced
reasoning capabilities, as demonstrated by models like GPT-4o or LLaMA 3.2
Vision.

#### **Level 3: Multimodal retrieval + MLLM**

Although we could use keyword-based search in the retrieval processes for
Level 1 and Level 2, it is a common practice to use so-called **vector
search**. This consists of **generating vector representations (i.e.,
embeddings)** of items in the knowledge base and then **performing a search by
computing similarity scores** between an input query and each item in the
knowledge base.

Traditionally, this requires that the query and knowledge base items are text-
based. However, as we saw in the [previous article](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f) of this series, there exist **multimodal embedding
models** that **generate aligned vector representations of both text and non-
text data**.

Therefore, we can use multimodal embeddings to perform multimodal retrieval.
This works the same way as text-based vector search, but now the embedding
space co-locates similar concepts independent of its original modality. The
results of such a retrieval strategy can then be passed directly to a MLLM.

![](https://cdn-images-1.medium.com/max/800/1*YwMdXXTGBMj9QSjAwkojdA.png)Visual overview of
Level 3 of MRAG. Image by author.

### **Example Code: Multimodal Blog Question-Answering Assistant**

With a basic understanding of how Multimodal RAG works, let’s see how we can
build such a system. Here, I will create a question-answering assistant that
can access the text and figures from the previous two blogs in this series.

The Python code for this example is freely available at the [GitHub repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/multimodal-ai/3-multimodal-rag).

* * *

#### Imports & Data Loading

We start by importing a few handy libraries and modules.

    
    
    import json  
    from transformers import CLIPProcessor, CLIPTextModelWithProjection  
    from torch import load, matmul, argsort  
    from torch.nn.functional import softmax

Next, we’ll import text and image chunks from the [Multimodal LLMs](https://towardsdatascience.com/multimodal-models-llms-that-can-see-and-hear-5c6737c981d3) and [Multimodal Embeddings](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f) blog posts. These are saved in .json files, which
can be loaded into Python as a list of dictionaries.

    
    
    # load text chunks  
    with open('data/text_content.json', 'r', encoding='utf-8') as f:  
            text_content_list = json.load(f)  
      
    # load images  
    with open('data/image_content.json', 'r', encoding='utf-8') as f:  
            image_content_list = json.load(f)

While I won’t review the data preparation process here, the code I used is on
the [GitHub repo](https://github.com/ShawhinT/YouTube-Blog/blob/main/multimodal-ai/3-multimodal-rag/1-data_prep.ipynb).

We will also load the multimodal embeddings (from CLIP) for each item in
_text_content_list_ and _image_content_list_. These are saved as pytorch
tensors.

    
    
    # load embeddings  
    text_embeddings = load('data/text_embeddings.pt', weights_only=True)  
    image_embeddings = load('data/image_embeddings.pt', weights_only=True)  
      
    print(text_embeddings.shape)  
    print(image_embeddings.shape)  
      
    # >> torch.Size([86, 512])  
    # >> torch.Size([17, 512])

Printing the shape of these tensors, we see they are represented via
512-dimensional embeddings. And we have 86 text chunks and 17 images.

#### Multimodal Search

With our knowledge base loaded, we can now define a query for vector search.
This will consist of translating an input query into an embedding using CLIP.
We do this similarly to the examples from the [previous post](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f).

    
    
    # query  
    query = "What is CLIP's contrastive loss function?"  
      
    # embed query (4 steps)  
    # 1) load model  
    model = CLIPTextModelWithProjection.from_pretrained("openai/clip-vit-base-patch16")  
    # 2) load data processor  
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")  
    # 3) pre-process text  
    inputs = processor(text=[text], return_tensors="pt", padding=True)  
    # 4) compute embeddings with CLIP  
    outputs = model(**inputs)  
      
    # extract embedding  
    query_embed = outputs.text_embeds  
    print(query_embed.shape)  
      
    # >> torch.Size([1, 512])

Printing the shape, we see we have a single vector representing the query.

To perform a vector search over the knowledge base, we need to do the
following.

  1. Compute similarities between the query embedding and all the text and image embeddings.
  2. Rescale the similarities to range from 0 to 1 via the softmax function.
  3. Sort the scaled similarities and return the top k results.
  4. Finally, filter the results to only keep items above a pre-defined similarity threshold.

Here’s what that looks like in code for the text chunks.

    
    
    # define k and simiarlity threshold  
    k = 5  
    threshold = 0.05  
      
    # multimodal search over articles  
    text_similarities = matmul(query_embed, text_embeddings.T)  
      
    # rescale similarities via softmax  
    temp=0.25  
    text_scores = softmax(text_similarities/temp, dim=1)  
      
    # return top k filtered text results  
    isorted_scores = argsort(text_scores, descending=True)[0]  
    sorted_scores = text_scores[0][isorted_scores]  
      
    itop_k_filtered = [idx.item()   
                        for idx, score in zip(isorted_scores, sorted_scores)   
                        if score.item() >= threshold][:k]  
    top_k = [text_content_list[i] for i in itop_k_filtered]  
      
    print(top_k)
    
    
    # top k results  
      
    [{'article_title': 'Multimodal Embeddings: An Introduction',  
      'section': 'Contrastive Learning',  
      'text': 'Two key aspects of CL contribute to its effectiveness'}]

Above, we see the top text results. Notice we only have one item, even though
_k_ =5. This is because the 2nd-5th items were below the 0.1 threshold.

Interestingly, this item doesn’t seem helpful to our initial query of _“What
is CLIP’s contrastive loss function?”_ This highlights **one of the key
challenges of vector search** : _items similar to a given query may not
necessarily help answer it_.

One way we can mitigate this issue is having less stringent restrictions on
our search results by increasing _k_ and lowering the similarity _threshold_ ,
then hoping the LLM can work out what’s helpful vs. not.

To do this, I’ll first package the vector search steps into a Python function.

    
    
    def similarity_search(query_embed, target_embeddings, content_list,   
                          k=5, threshold=0.05, temperature=0.5):  
        """  
           Perform similarity search over embeddings and return top k results.  
        """  
        # Calculate similarities  
        similarities = torch.matmul(query_embed, target_embeddings.T)  
          
        # Rescale similarities via softmax  
        scores = torch.nn.functional.softmax(similarities/temperature, dim=1)  
          
        # Get sorted indices and scores  
        sorted_indices = scores.argsort(descending=True)[0]  
        sorted_scores = scores[0][sorted_indices]  
          
        # Filter by threshold and get top k  
        filtered_indices = [  
            idx.item() for idx, score in zip(sorted_indices, sorted_scores)   
            if score.item() >= threshold  
        ][:k]  
          
        # Get corresponding content items and scores  
        top_results = [content_list[i] for i in filtered_indices]  
        result_scores = [scores[0][i].item() for i in filtered_indices]  
          
        return top_results, result_scores

Then, set more inclusive search parameters.

    
    
    # search over text chunks  
    text_results, text_scores = similarity_search(query_embed, text_embeddings,   
                        text_content_list, k=15, threshold=0.01, temperature=0.25)  
      
    # search over images  
    image_results, image_scores = similarity_search(query_embed, image_embeddings,   
                        image_content_list, k=5, threshold=0.25, temperature=0.5)

This results in 15 text results and 1 image result.

    
    
    1 - Two key aspects of CL contribute to its effectiveness  
    2 - To make a class prediction, we must extract the image logits and evaluate   
    which class corresponds to the maximum.  
    3 - Next, we can import a version of the clip model and its associated data   
    processor. Note: the processor handles tokenizing input text and image   
    preparation.  
    4 - The basic idea behind using CLIP for 0-shot image classification is to   
    pass an image into the model along with a set of possible class labels. Then,   
    a classification can be made by evaluating which text input is most similar to   
    the input image.  
    5 - We can then match the best image to the input text by extracting the text   
    logits and evaluating the image corresponding to the maximum.  
    6 - The code for these examples is freely available on the GitHub repository.  
    7 - We see that (again) the model nailed this simple example. But let’s try   
    some trickier examples.  
    8 - Next, we’ll preprocess the image/text inputs and pass them into the model.  
    9 - Another practical application of models like CLIP is multimodal RAG, which   
    consists of the automated retrieval of multimodal context to an LLM. In the   
    next article of this series, we will see how this works under the hood and   
    review a concrete example.  
    10 - Another application of CLIP is essentially the inverse of Use Case 1.   
    Rather than identifying which text label matches an input image, we can   
    evaluate which image (in a set) best matches a text input (i.e. query)—in   
    other words, performing a search over images.  
    11 - This has sparked efforts toward expanding LLM functionality to include   
    multiple modalities.  
    12 - GPT-4o — Input: text, images, and audio. Output: text.FLUX — Input: text.   
    Output: images.Suno — Input: text. Output: audio.  
    13 - The standard approach to aligning disparate embedding spaces is   
    contrastive learning (CL). A key intuition of CL is to represent different   
    views of the same information similarly [5].  
    14 - While the model is less confident about this prediction with a 54.64%   
    probability, it correctly implies that the image is not a meme.  
    15 - [8] Mini-Omni2: Towards Open-source GPT-4o with Vision, Speech and Duplex   
    Capabilities

![](https://cdn-images-1.medium.com/max/800/1*rq89PAcqQ_lHgkYhkf5T4g.png)Image
search result.

#### Prompting MLLM

Although most of these text item results do not seem helpful to our query, the
image result is exactly what we’re looking for. Nevertheless, given these
search results, let’s see how LLaMA 3.2 Vision responds to this query.

We first will structure the search results as well-formatted strings.

    
    
    text_context = ""  
    for text in text_results:  
        if text_results:  
            text_context = text_context + "**Article title:** "   
                                                  + text['article_title'] + "\n"  
            text_context = text_context + "**Section:**  "   
                                                  + text['section'] + "\n"  
            text_context = text_context + "**Snippet:** "   
                                                  + text['text'] + "\n\n"
    
    
    image_context = ""  
    for image in image_results:  
        if image_results:  
            image_context = image_context + "**Article title:** "   
                                              + image['article_title'] + "\n"  
            image_context = image_context + "**Section:**  "   
                                              + image['section'] + "\n"  
            image_context = image_context + "**Image Path:**  "   
                                              + image['image_path'] + "\n"  
            image_context = image_context + "**Image Caption:** "   
                                              + image['caption'] + "\n\n"

Note the metadata that accompanies each text and image item. This will help
the LLaMA better understand the context of the content.

Next, we interleave the text and image results in a prompt.

    
    
    # construct prompt template  
    prompt = f"""Given the query "{query}" and the following relevant snippets:  
      
    {text_context}  
    {image_context}  
      
    Please provide a concise and accurate answer to the query, incorporating   
    relevant information from the provided snippets where possible.  
      
    """

The final prompt is quite long, so I won’t print it here. However, it is fully
displayed in the [example notebook](https://github.com/ShawhinT/YouTube-Blog/blob/main/multimodal-ai/3-multimodal-rag/2-mrag_example.ipynb) on GitHub.

Finally, we can use [ollama](https://ollama.com/) to pass this prompt to LLaMA
3.2 Vision.

    
    
    ollama.pull('llama3.2-vision')  
      
    response = ollama.chat(  
        model='llama3.2-vision',  
        messages=[{  
            'role': 'user',  
            'content': prompt,  
            'images': [image["image_path"] for image in image_results]  
        }]  
    )  
      
    print(response['message']['content'])
    
    
    The image depicts a contrastive loss function for aligning text and image   
    representations in multimodal models. The function is designed to minimize the   
    difference between the similarity of positive pairs (text-image) and negative   
    pairs (text-text or image-image). This loss function is commonly used in CLIP,   
    which stands for Contrastive Language-Image Pre-training.  
      
    **Key Components:**  
      
    *   **Positive Pairs:** Text-image pairs where the text describes an image.  
    *   **Negative Pairs:** Text-text or image-image pairs that do not belong to   
    the same class.  
    *   **Contrastive Loss Function:** Calculates the difference between positive   
    and negative pairs' similarities.  
      
    **How it Works:**  
      
    1.  **Text-Image Embeddings:** Generate embeddings for both text and images   
    using a multimodal encoder (e.g., CLIP).  
    2.  **Positive Pair Similarity:** Calculate the similarity score between each   
    text-image pair.  
    3.  **Negative Pair Similarity:** Calculate the similarity scores between all   
    negative pairs.  
    4.  **Contrastive Loss Calculation:** Compute the contrastive loss by   
    minimizing the difference between positive and negative pairs' similarities.  
      
    **Benefits:**  
      
    *   **Multimodal Alignment:** Aligns text and image representations for better   
    understanding of visual content from text descriptions.  
    *   **Improved Performance:** Enhances performance in downstream tasks like   
    image classification, retrieval, and generation.

The model correctly picks up that the image contains the information it needs
and explains the general intuition of how it works. However, it
**misunderstands the meaning of positive and negative pairs** , thinking that
a negative pair corresponds to a pair of the same modality.

While we went through the implementation details step-by-step, I packaged
everything into a nice UI using Gradio in this
[notebook](https://github.com/ShawhinT/YouTube-Blog/blob/main/multimodal-ai/3-multimodal-rag/3-mrag_UI.ipynb) on the GitHub repo.

### Conclusion

Multimodal RAG systems can synthesize knowledge stored in a variety of
formats, expanding what’s possible with AI. Here, we reviewed 3 simple
strategies for developing such a system and then saw an example implementation
of a multimodal blog QA assistant.

Although the example worked well enough for this demonstration, there are
clear limitations to the search process. A few techniques that may improve
this include using a **reranker to refine similarity search** results and to
improve search quality via **fine-tuned multimodal embeddings**.

If you want to see future posts on these topics, let me know in the comments
:)