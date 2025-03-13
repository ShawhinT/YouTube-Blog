# 3 AI Use Cases (That Are Not a Chatbot)
#### **Feature engineering, structuring unstructured data, and lead scoring**

The most common request I’ve received from (AI consulting) clients is “ _Build
me a custom chatbot_.” While this is a great solution to some problems, it is
far from a cure-all. In this article, I share three alternative ways
businesses can use AI to generate value in the context of sales. The
approaches span Generative AI, Deep Learning, and Machine Learning.

![](https://cdn-images-1.medium.com/max/800/1*UAA9jQVdqMXnwzYiz8Q53Q.png)Image
from Canva.

* * *

Large language models (LLMs) have taken over the business world, and now every
company is trying to use Generative AI. Although tools like ChatGPT are
clearly powerful, it is not clear how businesses can reliably use this
technology to **drive value**.

For most businesses I’ve interacted with, “ _using AI_ ” means building a
chatbot, co-pilot, AI agent, or AI assistant. However, as the initial
excitement about these solutions wanes, organizations are realizing the key
challenges of building systems around LLMs.

### **This is harder than I thought…**

A central challenge is that LLMs are inherently unpredictable (even more so
than traditional machine learning systems). Therefore, it is **not easy to get
them to solve a specific problem predictably**.

For instance, one solution to the hallucination problem is to have “judge”
LLMs review system responses for accuracy and appropriateness. However,
increasing the number of LLMs increases the system's cost, complexity, and
uncertainty.

### **Solving the Right Problem**

This is not to say that Generative AI (and friends) are not worth pursuing. AI
has made countless companies very rich, and I don’t think that will stop
anytime soon.

The key point is that value is generated through solving problems, not using
AI (in itself). AI's promise is realized when businesses **identify the
_right_ problems to solve**, e.g., Netflix’s personalized recommendations,
UPS’s delivery route optimization, Walmart’s inventory management, and many
others.

### **3 AI Sales Use Cases**

While “solving the right problem” is easy to say, it is not easy to do. To
help with that, here I share 3 AI use cases for something every business cares
about — sales. My hope is to get your imagination going and demonstrate how to
implement them with concrete examples.

The three use cases are:

  1. **Feature Engineering** — Extracting features from text
  2. **Structuring Unstructured Data** — Making text analytics-ready
  3. **Lead Scoring** — Identifying your greatest opportunities

![](https://cdn-images-1.medium.com/max/800/1*oc6qkytffi5EsrofEej9Fg.png)3 AI
Use Cases. Image by author.

### **Use Case 1: Feature Engineering**

**Featuring engineering** consists of **creating variables that can be used to
train machine learning models** or perform some analysis. For example, given a
set of LinkedIn profiles, extracting things like the current job title, years
of experience, and industry, and then representing them numerically.

![](https://cdn-images-1.medium.com/max/800/1*A-QTDzljazKvtaz1xsFryg.png)Extracting Years of
Experience and Industry from Resume Text. Image by author.

Traditionally, this is done in two ways. 1) you manually create features, or
2) you buy features from a 3rd party (e.g., credit scores from FICO, company
revenue from D&B). However, **LLMs have created a third way** to do this.

#### **Example: Extracting Features from Resumes**

Suppose you are qualifying leads for a SaaS offering. The software helps
protect mid-market corporations against cybersecurity threats. The target
customers are IT leaders who decide which vendors suit their companies.

You have a stack of 100,000 professional profiles and resumes gathered from
various sources based on the tags “IT,” “Cybersecurity,” “leader,” “VP,” and
several others. The problem, however, is that the leads are low quality, often
including non-IT leaders, entry-level IT professionals, and others who don’t
fit the customer profile.

To ensure that sales efforts are focused on the right customers, **the goal is
to filter down the leads only to include IT leaders**. Here are a few ways to
solve this problem.

  * **Idea 1** : Review all the 100,000 leads manually. **Problem** : Impractical for a single person or small sales team
  * **Idea 2** : Write rule-based logic to filter resumes. **Problem** : Resumes come in a wide variety of formats, so logic performs poorly.
  * **Idea 3** : Pay a data vendor for this information. **Problem** : This significantly increases the cost of customer acquisition (~$0.10 per lead)

Given the issues with the ideas above, let’s consider how we could solve this
problem with a large language model. A simple strategy is to craft a prompt
that instructs an LLM to extract the desired information from a resume. An
example is given below.

    
    
    Analyze the following text extracted from a resume and determine whether the   
    person works in the IT industry. Return a `0` if the person does not work in   
    theIT industry, and a `1` if they do. Then, provide a brief explanation for   
    your conclusion.  
      
    Resume Text:  
    {resume text}

This solution is a perfect blend of the three ideas above. It (1) reviews each
lead looking for specific information like a person, (2) is automated by a
computer program, and (3) you pay less money (~$0.001 per lead).

**_**Bonus**_**_:_ _For those interested in implementing something like this,
I share an example Python script_[**_here_**](https://youtu.be/3JsgtpX_rpU?si=WG1X-tvKmXLQLkEY&t=446) _that
extracts Years of Experience from a LinkedIn Profile using the OpenAI API._

### **Use Case 2: Structuring Unstructured Data**

Data from emails, support tickets, customer reviews, social media profiles,
and call transcriptions are all examples of **unstructured data**. This simply
means **it is not organized in rows and columns** like an Excel spreadsheet or
.csv file.

![](https://cdn-images-1.medium.com/max/800/1*b_EE6yZg3MsS9cjjYnurwg.png)Structured vs
Unstructured data. Image by author.

The problem with unstructured data is that it is not analytics-ready, making
it difficult to gain insights. This contrasts with **structured data** (i.e.,
**numbers organized in rows and columns**). Translating unstructured data into
a structured format is another area in which recent advances in natural
language processing (NLP) and deep learning can help.

#### **Example: Translating Resumes into (Meaningful) Numbers**

Consider the same business case from the previous example. Suppose we
successfully picked out 10,000 IT leaders from the 100,000 leads. While your
sales guy could start picking up the phone and crafting emails, you first want
to see if you can **distill the list** **to prioritize leads** **similar to
past customers**.

One way to do this is to define additional features that provide more
granularity to the ideal customer profile (e.g., industry, compliance
requirements, tech stack, geographical location), which could be extracted
similarly to Use Case 1. However, **identifying such indicators might be
challenging** , and developing additional automated processes comes at a cost.

An alternative approach is to use so-called **text embeddings**. A text
embedding is simply **a numerical representation of a chunk of text** that is
semantically meaningful. Think of this like translating a resume into a set of
numbers.

![](https://cdn-images-1.medium.com/max/800/1*EcjKnZiksL2Vp01rEsWTKQ.png)Converting text to
text embeddings. Image by author.

The value of text embeddings is that they translate unstructured text into a
structured table of numbers, which is much more amenable to traditional
analytical and computational approaches. For example, in this context, one can
use text embeddings to **mathematically evaluate which leads are most similar
to past customers** and which are most different.

### **Use Case 3: Lead Scoring**

The final use case is **lead scoring** , which consists of **evaluating the
quality of a lead** based on key predictors (e.g., job title, company revenue,
customer behavior, etc.). While this is nothing new, recent advances in AI
have enabled a better ability to parse unstructured data that can be fed into
lead-scoring models.

#### **Example: Grading Leads Based on Quality**

To conclude our ongoing business case, let’s discuss how we can **use text
embeddings to prioritize potential customers**. Suppose we have a list of
1,000 past leads, 500 of whom bought and 500 of whom didn’t. For each lead, we
have a profile that includes key information such as job title, work
experience, current company, industry, and key skills.

These leads can be used to train a predictive model that estimates the
probability that a customer will buy the product based on their profile. While
there are many nuances to developing a model like this, the basic idea is that
**we can use the predictions from this model to define grades for each lead**
(e.g., A, B, C, D), which can be used to categorize and prioritize the 10,000
new ones.

**_**Bonus**_** : For the more technical readers seeking to implement these
approaches, I walk through all three use cases applied to real-world sales
data from my business in this [**video**](https://youtu.be/3JsgtpX_rpU).
Additionally, the example code is freely available on
[**GitHub**](https://github.com/ShawhinT/YouTube-Blog/tree/main/ai-for-business/3-sales-use-cases).

### **Recap**

AI holds tremendous potential for businesses. However, realizing that
potential requires identifying the _right_ problems to solve with it.

With the ubiquity of tools like ChatGPT, solution ideas can easily be limited
to the AI assistant paradigm. To help expand the space of possibilities, I
shared 3 practical AI use cases that use alternative approaches.