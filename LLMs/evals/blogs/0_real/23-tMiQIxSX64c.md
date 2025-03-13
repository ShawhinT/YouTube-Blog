# 5 AI Projects You Can Build This Weekend (with Python)
#### From beginner-friendly to advanced

![](https://cdn-images-1.medium.com/max/800/1*YMwyctXXY6dsjyW_CVv0lQ.png)Image
from Canva.

The best way to develop your AI skills is by **building projects**. However,
figuring out _what to build_ can be difficult if you're just getting started.
Here, I share 5 AI projects you can build fast at three levels of
sophistication. I’ll break down the steps and Python libraries needed to
implement each idea.

* * *

The **number one mistake** beginners make when thinking of project ideas is
starting with the question, _"How can I use this new tech?_ " While this can
be a fine way to learn a new tool, there is a better way.

Good project ideas start with the question, _“What problem can I solve?”_ This
not only makes for a nice story when sharing with potential employers but
solving problems is how you **translate technical skills into value**.

The following projects all take this problem-first approach. You can take
these ideas and implement them directly or (even better) use them as
inspiration for solving a problem that you are personally facing.

### **1) Resume Optimization (Beginner)**

An effective yet time-consuming part of applying for jobs is adapting your
resume to different job descriptions. While automating this task would have
been an advanced project a few years ago, with today’s large language models,
it is as simple as an [API call](https://towardsdatascience.com/cracking-open-the-openai-python-api-230e4cae7971).

Here’s a step-by-step breakdown of how to implement such an automation.

  1. Create a markdown version of your resume _(Note: ChatGPT can do this for you)._
  2. Experiment with different prompt templates that take your markdown resume and a job description and output a new resume in markdown.
  3. Use OpenAI’s Python API to prompt GPT-4o-mini to rewrite your resume dynamically.
  4. Convert the markdown file to HTML and then to PDF with the [_markdown_](https://pypi.org/project/Markdown/) and [_pdfkit_](https://pypi.org/project/pdfkit/) libraries, respectively.

**_Libraries_** _:_[_openai_](https://pypi.org/project/openai/)
_,_[_markdown_](https://pypi.org/project/Markdown/)
_,_[_pdfkit_](https://pypi.org/project/pdfkit/)

While we could readily use ChatGPT for this, the upside of implementing this
with Python is that we can easily scale up the process. Here’s some starter
code for Step 3.

    
    
    import openai  
    openai.api_key = "your_sk"  
      
    # prompt (assuming md_resume and job_desciption have been defined)  
    prompt = f"""  
    I have a resume formatted in Markdown and a job description. \  
    Please adapt my resume to better align with the job requirements while \  
    maintaining a professional tone. Tailor my skills, experiences, and \  
    achievements to highlight the most relevant points for the position. \  
    Ensure that my resume still reflects my unique qualifications and strengths \  
    but emphasizes the skills and experiences that match the job description.  
      
    ### Here is my resume in Markdown:  
    {md_resume}  
      
    ### Here is the job description:  
    {job_desciption}  
      
    Please modify the resume to:  
    - Use keywords and phrases from the job description.  
    - Adjust the bullet points under each role to emphasize relevant skills and achievements.  
    - Make sure my experiences are presented in a way that matches the required qualifications.  
    - Maintain clarity, conciseness, and professionalism throughout.  
      
    Return the updated resume in Markdown format.  
      
    """  
          
    # make api call  
    response = openai.chat.completions.create(  
        model="gpt-4o-mini",  
        messages=[  
            {"role": "system", "content": "You are a helpful assistant."},  
            {"role": "user", "content": prompt}  
        ],   
        temperature = 0.25  
    )  
          
    # extract response  
    resume = response.choices[0].message.content

Note: ChatGPT is super helpful for writing short code snippets (and prompts)
like this. If you get stuck, try it for Step 4.

### **2) YouTube Lecture Summarizer (Beginner)**

Although I love adding technical talks to my YouTube “watch later” playlist,
it might be a while before I watch them (if I ever get around to it 😅). A
project that can help with this is a tool that watches the videos for me and
generates concise summaries with key points.

Here’s one way to do that:

  1. Extract YouTube video ID from video link using regex
  2. Use video ID to extract transcript using [_youtube-transcript-api_](https://pypi.org/project/youtube-transcript-api/)
  3. Experiment with different ChatGPT prompts that effectively summarize the transcript
  4. Use OpenAI’s Python API to automate the process

** _Libraries_** _:_[_openai_](https://pypi.org/project/openai/) _,_[_youtube-transcript-api_](https://pypi.org/project/youtube-transcript-api/)

From a technical perspective, this is very similar to the first project. A key
difference, however, is that we will need to automatically extract video
transcripts, which we can feed into the LLM.

Here’s some starter code for that.

    
    
    import re  
    from youtube_transcript_api import YouTubeTranscriptApi  
      
    youtube_url = "video link here"  
      
    # extract video ID with regex  
    video_id_regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'  
    match = re.search(video_id_regex, youtube_url)  
      
    if match:  
        return match.group(1)  
    else:  
        return None  
      
    # extract transcript  
    text_list = [transcript[i]['text'] for i in range(len(transcript))]  
    transcript_text = '\n'.join(text_list)

### **3) Automatically Organizing PDFs (Intermediate)**

My watch later playlist is not the only place I hoard technical information.
Another cache is my desktop, which is riddled with (118) research papers.
Since manually reviewing these papers would be (very) time-consuming, let’s
see how AI can help.

One could build a tool that analyzes the contents of each PDF on my desktop
and organize them into folders based on topics. [Text embeddings](https://towardsdatascience.com/text-embeddings-classification-and-semantic-search-8291746220be) can translate each paper into a dense vector
representation, from which similar articles could be clustered using a
traditional machine learning algorithm like K-Means.

Here’s a more detailed breakdown:

  1. Read the abstract of each research article using [_PyMuPDF_](https://pypi.org/project/PyMuPDF/)
  2. Use the [_sentence-transformers_](https://pypi.org/project/sentence-transformers/) library to translate abstracts into text embeddings and store them in a Pandas DataFrame
  3. Use your favorite clustering algorithm from sklearn to group the embeddings based on similarity
  4. Create folders for each cluster and move the files into the appropriate folder.

**_Libraries_**
_:_[_PyMuPDF_](https://pypi.org/project/PyMuPDF/),__[_sentence_transformers_](https://pypi.org/project/sentence-
transformers/) _,_[_pandas_](https://pypi.org/project/pandas/)
_,_[_sklearn_](https://pypi.org/project/scikit-learn/)

The key step for this project is generating the [text embeddings](https://towardsdatascience.com/text-embeddings-classification-and-semantic-search-8291746220be). Here’s a code snippet for doing that with
sentence_transformers.

    
    
    from sentence_transformers import SentenceTransformer  
      
    # load embedding model  
    model = SentenceTransformer("all-MiniLM-L6-v2")  
      
    # store abstracts in a list  
    abstract_list = ["abstract 1", "abstract 2"]  
      
    # calculate embeddings  
    embeddings = model.encode(abstract_list)

### **4) Multimodal Search (Intermediate)**

A couple of months ago, I helped a company create a basic
[RAG](https://towardsdatascience.com/how-to-improve-llms-with-rag-abdc132f76ac) system for a set of technical reports. One of the challenges
with searching such reports is that key information is often presented in
**plots and figures rather than text**.

One way to incorporate this visual information into the search process is to
use a [**multimodal embedding**](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f)**model** to **represent text and
images in a shared space**.

Here’s a basic breakdown:

  1. Given a PDF, chunk it into sections and extract the images using [_PyMuPDF_](https://pypi.org/project/PyMuPDF/)
  2. Use a multimodal embedding model (e.g. [nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)) to represent the chunks and images as dense vectors and store them in a dataframe
  3. Repeat for all PDFs in the knowledge base
  4. Given a user query, pass it through the same embedding model used for the knowledge base
  5. Compute the cosine similarity score between the query embedding and every item in the knowledge base
  6. Return top k results

** _Libraries_** _:_[_PyMuPDF_](https://pypi.org/project/PyMuPDF/)
_,_[_transformers_](https://pypi.org/project/transformers/)
_,_[_pandas_](https://pypi.org/project/pandas/)
_,_[_sklearn_](https://pypi.org/project/scikit-learn/)

The most important part of this project is how the PDFs are chunked. The
simplest way would be to use a fixed character count with some overlap between
chunks. It is also helpful to capture metadata such as filename and page
number for each chunk.

Here’s some basic boilerplate code to do that (courtesy of ChatGPT). If you
get stuck, try asking it to extract the images.

    
    
    import fitz  # PyMuPDF  
      
    def extract_text_chunks(pdf_path, chunk_size, overlap_size):  
        # Open the PDF file  
        pdf_document = fitz.open(pdf_path)  
        chunks = []  
      
        # Iterate through each page in the PDF  
        for page_num in range(len(pdf_document)):  
            page = pdf_document[page_num]  
            page_text = page.get_text()  
      
            # Split the text from the current page into chunks with overlap  
            start = 0  
            while start < len(page_text):  
                end = start + chunk_size  
                chunk = page_text[start:end]  
      
                # Store the page number with the chunk  
                chunks.append((page_num + 1, chunk))  
                # Move to the next chunk with the overlap  
                start += chunk_size - overlap_size  
          
        return chunks  
      
    # Parameters for extraction  
    pdf_path = "your_file.pdf"  
    chunk_size = 1000  # Size of each text chunk in characters  
    overlap_size = 200  # Overlap size in characters  
      
    text_chunks = extract_text_chunks_with_page_numbers(pdf_path, chunk_size, overlap_size)  
      
    # Display the chunks with page numbers  
    for i, (page_number, chunk) in enumerate(text_chunks):  
        print(f"Chunk {i + 1} (Page {page_number}):\n{chunk}\n{'-' * 50}")

### **5) Knowledge Base QA (Advanced)**

Over the past year, I’ve helped almost 100 businesses and individuals build AI
projects. By far, the **most common project people ask about** is a document
question-answering system. Building on the previous project, we can implement
this in a straightforward way.

If we’ve already chunked and stored our documents in a DataFrame, we can
convert the multimodal search tool into a [multimodal RAG](https://towardsdatascience.com/multimodal-rag-process-any-file-type-with-ai-e6921342c903) system.

Here are the steps:

  1. Perform a search over the knowledge base (like the one created in Project 4)
  2. Combine user query with top k search results and pass them to a multimodal model.
  3. Create a simple Gradio user interface for the QA system.

**_Libraries_** : [_PyMuPDF_](https://pypi.org/project/PyMuPDF/)
_,_[_transformers_](https://pypi.org/project/transformers/)
_,_[_pandas_](https://pypi.org/project/pandas/)
_,_[_sklearn_](https://pypi.org/project/scikit-learn/),
[_together_](https://pypi.org/project/together/)
_/_[_openai_](https://pypi.org/project/openai/)
_,_[_Gradio_](https://pypi.org/project/gradio/)

 _Note: Llama 3.2 Vision is free until 2025 via Together AI’s API_

This project essentially combines projects 2 and 4. However, it includes the
essential component of a user interface. For that, we can use a dashboarding
tool like **Gradio** , which **allows us to create a chat UI with a few lines
of code**.

Here’s an example snippet adapted from Gradio’s
[doc](https://www.gradio.app/guides/creating-a-chatbot-fast#add-multimodal-capability-to-your-chatbot) for doing this.

    
    
    import gradio as gr  
    import time  
      
    def generate_response(message, history):  
        """  
            Your code for generating a response  
        """  
        return response  
      
    demo = gr.ChatInterface(  
        fn=generate_response,   
        examples=[{"text": "Hello", "files": []}],   
        title="Echo Bot",   
        multimodal=True)  
      
    demo.launch()


### **What’s next?**

Thanks to tools like ChatGPT and [Cursor](https://www.cursor.com/), **it’s
never been easier to build AI projects _fast_**. Things that used to block me
for hours (if not days) a few years ago can now be resolved in minutes with
advanced coding assistants.

My parting advice is to use these tools to **learn faster** and **be bold** in
your project choices. For projects, find problems and time-box the
implementation into a weekend.

Drop your questions in the comments :)