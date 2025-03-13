# Prompt Engineering: How to Trick AI into Solving Your Problems
#### 7 prompting tricks, LangChain, and Python example code

This is the fourth article in a [series on using large language
models](https://towardsdatascience.com/a-practical-introduction-to-
llms-65194dda1148) (LLMs) in practice. Here, I will discuss prompt engineering
(PE) and how to use it to build LLM-enabled applications. I start by reviewing
key PE techniques and then walk through Python example code of using LangChain
to build an LLM-based application.

![](https://cdn-images-1.medium.com/max/800/0*ZcfH-qxXT4AYAqwr)Photo by [Jason
Leung](https://unsplash.com/@ninjason?utm_source=medium&utm_medium=referral)
on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

* * *

When first hearing about prompt engineering, many technical people (including
myself) tend to scoff at the idea. We might think, “ _Prompt engineering?
Psssh, that’s lame. Tell me how to build an LLM from scratch._ ”

However, after diving into it more deeply, I’d caution developers against
writing off prompt engineering automatically. I’ll go even further and say
that **prompt engineering can realize 80% of the value** of most LLM use cases
with (relatively) very low effort.

My goal with this article is to convey this point via a practical review of
prompt engineering and illustrative examples. While there are surely gaps in
what prompt engineering can do, it opens the door to discovering simple and
clever solutions to our problems.

Supplemental Video.

### **What is Prompt Engineering?**

In the [first article of this series](https://towardsdatascience.com/a-practical-introduction-to-llms-65194dda1148), I defined **prompt engineering** as **any use of an LLM
out-of-the-box** (i.e. not training any internal model parameters). However,
there is much more that can be said about it.

  1. Prompt Engineering is “ _the means by which LLMs are programmed with prompts._ ” [[1](https://arxiv.org/abs/2302.11382)]
  2. Prompt Engineering is “a _n empirical art of composing and formatting the prompt to maximize a model’s performance on a desired task._ ” [[2](https://arxiv.org/abs/2106.09685)]
  3. _“language models… want to complete documents, and so you can trick them into performing tasks just by arranging fake documents_.” [[3](https://www.youtube.com/watch?v=bZQun8Y4L2A)]

The first definition conveys the key innovation coming from LLMs, which is
that **computers can now be programmed using plain English**. The second point
frames prompt engineering as a largely empirical endeavor, where
practitioners, tinkerers, and builders are the key explorers of this new way
of programming.

The third point (from [Andrej Karpathy](https://medium.com/u/ac9d9a35533e))
reminds us that **LLMs aren’t explicitly trained to do almost anything we ask
them to do**. Thus, in some sense, we are “tricking” these language models to
solve problems. I feel this captures the essence of prompt engineering, which
relies less on your technical skills and more on your creativity.

### **2 Levels of Prompt Engineering**

There are two distinct ways in which one can do prompt engineering, which I
called the “**easy way** ” and the “**less easy way** ” in the [first article](https://towardsdatascience.com/a-practical-introduction-to-llms-65194dda1148) of this series.

#### The Easy Way

This is how most of the world does prompt engineering, which is via ChatGPT
(or something similar). It is an intuitive, no-code, and cost-free way to
interact with an LLM.

While this is a great approach for something quick and simple, e.g.
summarizing a page of text, rewriting an email, helping you brainstorm
birthday party plans, etc., it has its downsides. A big one is that **it’s not
easy to integrate this approach into a larger automated process or software
system**. To do this, we need to go one step further.

#### The Less Easy Way

This resolves many of the drawbacks of the “easy way” by interacting with LLMs
programmatically i.e. using Python. We got a sense of how we can do this in
the previous two articles of this series, where explored [OpenAI’s Python API](https://towardsdatascience.com/cracking-open-the-openai-python-api-230e4cae7971) and the [Hugging Face Transformers library](https://towardsdatascience.com/cracking-open-the-hugging-face-transformers-library-350aa0ef0161).

While this requires more technical knowledge, **this is where the real power
of prompt engineering lies** because it allows developers to integrate LLM-
based modules into larger software systems.

A good (and perhaps ironic) example of this is ChatGPT. The core of this
product is prompting a pre-trained model (i.e. GPT-3.5-turbo) to act like a
chatbot and then wrapping it in an easy-to-use web interface.

Of course, developing GPT-3.5-turbo is the hard part, **but that’s not
something we need to worry about here**. With all the pre-trained LLMs we have
at our fingertips, almost anyone with basic programming skills can create a
powerful AI application like ChatGPT without being an AI researcher or a
machine learning Ph.D.

### **Building AI Apps with Prompt Engineering**

The less easy way unlocks a **new paradigm of programming and software
development**. No longer are developers required to define every inch of logic
in their software systems. They now have the option to offload a non-trivial
portion to LLMs. Let’s look at a concrete example of what this might look
like.

Suppose you want to create an **automatic grader for a high school history
class**. The trouble, however, is that all the questions have written
responses, so there often can be multiple versions of a correct answer. For
example, the following responses to “ _Who was the 35th president of the
United States of America?_ ” could be correct.

  * John F. Kennedy
  * JFK
  * Jack Kennedy (a common nickname)
  * John Fitzgerald Kennedy (probably trying to get extra credit)
  * John F. Kenedy (misspelled last name)

In the **traditional programming paradigm** , it was on the developer to
figure out how to account for all these variations. To do this, they might
list all possible correct answers and use an exact string-matching algorithm
or maybe even use fuzzy matching to help with misspelled words.

However, with this new **LLM-enabled paradigm** , **the problem can be solved
through simple prompt engineering**. For instance, we could use the following
prompt to evaluate student answers.

    
    
    You are a high school history teacher grading homework assignments. \  
    Based on the homework question indicated by “Q:” and the correct answer \  
    indicated by “A:”, your task is to determine whether the student's answer is \  
    correct.  
    Grading is binary; therefore, student answers can be correct or wrong.  
    Simple misspellings are okay.  
       
    Q: {question}  
    A: {correct_answer}  
       
    Student Answer: {student_answer}

We can think of this prompt as a function, where given a **_question_** ,
**_correct_answer_** , and **_student_answer_** , it generates the student's
grade. This can then be integrated into a larger piece of software that
implements the automatic grader.

In terms of time-saving, this prompt took me about 2 minutes to write, while
if I were to try to develop an algorithm to do the same thing, it would take
me hours (if not days) and probably have worse performance. **So the time
savings for tasks like this are 100–1000x**.

Of course, there are many tasks in which LLMs do not provide any substantial
benefit, and other existing methods are much better suited (e.g. predicting
tomorrow’s weather). In no way are LLMs the solution to every problem, but
they do create a new set of solutions to tasks that require processing natural
language effectively—something that has been historically difficult for
computers to do.

### **7 Tricks for Prompt Engineering**

While the prompt example from before may seem like a natural and obvious way
to frame the automatic grading task, it deliberately employed specific prompt
engineering heuristics (or “tricks,” as I’ll call them). These (and other)
tricks have emerged as reliable ways to improve the quality of LLM responses.

Although there are many tips and tricks for writing good prompts, here I
restrict the discussion to the ones that seem the most fundamental (IMO) based
on a handful of references [1,3–5]. For a deeper dive, I recommend the reader
explore the sources cited here.

#### **Trick 1: Be Descriptive (More is Better)**

A defining feature of LLMs is that they are trained on massive text corpora.
This equips them with a vast knowledge of the world and the ability to perform
an enormous variety of tasks. However, this impressive generality may hinder
performance on a specific task if the proper context is not provided.

For example, let’s compare two prompts for generating a birthday message for
my dad.

**_Without Trick_**

    
    
     Write me a birthday message for my dad.

**_With Trick_**

    
    
     Write me a birthday message for my dad no longer than 200 \  
    characters. This is a big birthday because he is turning 50. To celebrate, \  
    I booked us a boys' trip to Cancun. Be sure to include some cheeky humor, he \  
    loves that.

#### **Trick 2: Give Examples**

The next trick is to give the LLM example responses to improve its performance
on a particular task. The technical term for this is **few-shot learning,**
and has been shown to improve LLM performance significantly [6].

Let’s look at a specific example. Say we want to write a subtitle for a
Towards Data Science article. We can use existing examples to help guide the
LLM completion.

**_Without Trick_**

    
    
     Given the title of a Towards Data Science blog article, write a subtitle for it.  
      
    Title: Prompt Engineering—How to trick AI into solving your problems  
    Subtitle:

**_With Trick_**

    
    
     Given the title of a Towards Data Science blog article, write a subtitle for it.  
      
    Title: A Practical Introduction to LLMs  
    Subtitle: 3 levels of using LLMs in practice  
      
    Title: Cracking Open the OpenAI (Python) API  
    Subtitle: A complete beginner-friendly introduction with example code  
      
    Title: Prompt Engineering-How to trick AI into solving your problems  
    Subtitle:

#### **Trick 3: Use Structured Text**

Ensuring prompts follow an organized structure not only makes them easier to
read and write, but also tends to help the model generate good completions. We
employed this technique in the example for **Trick 2** , where we explicitly
labeled the _title_ and _subtitle_ for each example.

However, there are countless ways we can give our prompts structure. Here are
a handful of examples: use ALL CAPS for emphasis, use delimiters like ``` to
highlight a body of text, use markup languages like Markdown or HTML to format
text, use JSON to organize information, etc.  
  
Now, let’s see this in action.

**_Without Trick_**

    
    
     Write me a recipe for chocolate chip cookies.

**_With Trick_**

    
    
     Create a well-organized recipe for chocolate chip cookies. Use the following \  
    formatting elements:  
      
    **Title**: Classic Chocolate Chip Cookies  
    **Ingredients**: List the ingredients with precise measurements and formatting.  
    **Instructions**: Provide step-by-step instructions in numbered format, detailing the baking process.  
    **Tips**: Include a separate section with helpful baking tips and possible variations.

#### **Trick 4: Chain of Thought**

This trick was proposed by Wei et al. [7]. The basic idea is to guide an LLM
to think “step by step”. This helps break down complex problems into
manageable sub-problems, which gives the LLM “time to think” [3,5]. Zhang et
al. showed that this could be as simple as including the text “ _Let’s think
step by step_ ” in the prompt [8].

This notion can be extended to any recipe-like process. For example, if I want
to create a LinkedIn post based on my latest Medium blog, I can guide the LLM
to mirror the step-by-step process I follow.

**_Without Trick_**

    
    
     Write me a LinkedIn post based on the following Medium blog.  
      
    Medium blog: {Medium blog text}

**_With Trick_**

    
    
     Write me a LinkedIn post based on the step-by-step process and Medium blog \  
    given below.    
      
    Step 1: Come up with a one line hook relevant to the blog.   
    Step 2: Extract 3 key points from the article   
    Step 3: Compress each point to less than 50 characters.   
    Step 4: Combine the hook, compressed key points from Step 3, and a call to action \  
    to generate the final output.  
      
    Medium blog: {Medium blog text}

#### **Trick 5: Chatbot Personas**

A somewhat surprising technique that tends to improve LLM performance is to
prompt it to take on a particular persona e.g. “ _you are an expert_ ”. This
is helpful because you may not know the best way to describe your problem to
the LLM, but you may know who would help you solve that problem
[[1](https://arxiv.org/abs/2302.11382)]. Here’s what this might look like in
practice.

**_Without Trick_**

    
    
     Make me a travel itinerary for a weekend in New York City.

**_With Trick_**

    
    
     Act as an NYC native and cabbie who knows everything about the city. \  
    Please make me a travel itinerary for a weekend in New York City based on \  
    your experience. Don't forget to include your charming NY accent in your \  
    response.

#### **Trick 6: Flipped Approach**

It can be difficult to optimally prompt an LLM when **we do not know what it
knows or how it thinks**. That is where the “flipped approach” can be helpful.
This is where you prompt the LLM to ask you questions until it has a
sufficient understanding (i.e. context) of the problem you are trying to
solve.

**_Without Trick_**

    
    
     What is an idea for an LLM-based application?

**_With Trick_**

    
    
     I want you to ask me questions to help me come up with an LLM-based \  
    application idea. Ask me one question at a time to keep things conversational.

#### **Trick 7: Reflect, Review, and Refine**

This final trick prompts the model to reflect on its past responses to improve
them. Common use cases are having the model critically evaluate its own work
by asking it if it “ _completed the assignment_ ” or having it “ _explain the
reasoning and assumptions_ ” behind a response [1, 3].

Additionally, you can ask the LLM to refine not only its responses but **your
prompts**. This is a simple way to automatically rewrite prompts so that they
are easier for the model to “understand”.

**_With Trick_**

    
    
     Review your previous response, pinpoint areas for enhancement, and offer an \  
    improved version. Then explain your reasoning for how you improved the response.

### **Example Code: Automatic Grader with LangChain**

Now that we’ve reviewed several prompting heuristics let’s see how we can
apply them to a specific use case. To do this, we will return to the automatic
grader example from before.

    
    
    You are a high school history teacher grading homework assignments. \  
    Based on the homework question indicated by "Q:" and the correct answer \  
    indicated by "A:", your task is to determine whether the student's answer is \  
    correct.  
    Grading is binary; therefore, student answers can be correct or wrong.  
    Simple misspellings are okay.  
       
    Q: {question}  
    A: {correct_answer}  
       
    Student Answer: {student_answer}

On second look, a few of the previously mentioned tricks should be apparent
i.e. **Trick 6** : chatbot persona, **Trick 3** : use structured text, and
**Trick 1** : be descriptive. This is what good prompting typically looks like
in practice, namely combining multiple techniques in a single prompt.

While we could copy-paste this prompt template into ChatGPT and replace the
_question_ , _correct_answer_ , and _student_answer_ fields, **this is not a
scalable way to implement the automatic grader**. Rather, what we want is to
integrate this prompt into a larger software system so that we can build a
user-friendly application that a human can use.

#### LangChain

One way we can do this is via **LangChain** , which is **a Python library that
helps simplify building applications on top of large language models**. It
does this by providing a variety of handy abstractions for using LLMs
programmatically.

The central class that does this is called **chain** (hence the library name).
This abstracts the process of generating a prompt, sending it to an LLM, and
parsing the output so that it can be easily called and integrated into a
larger script.

Let’s see how to use LangChain for our automatic grader use case. The example
code is available on the [GitHub Repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/langchain-example) for this article.

#### Imports

We first start by importing the necessary library modules.

    
    
    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts import PromptTemplate  
    from langchain.chains import LLMChain  
    from langchain.schema import BaseOutputParser

Here we will use gpt-3.5-turbo which requires a secret key for OpenAI’s API.
If you don’t have one, I gave a step-by-step guide on how to get one in a
[past article](https://towardsdatascience.com/cracking-open-the-openai-python-api-230e4cae7971) of this series. I like to store the secret key in a separate
Python file (_sk.py_) and import it with the following line of code.

    
    
    from sk import my_sk #importing secret key from another python file

#### Our 1st chain

To define our chain, we need two core elements: the **LLM** and the
**prompt**. We start by creating an object for the LLM.

    
    
    # define LLM object  
    chat_model = ChatOpenAI(openai_api_key=my_sk, temperature=0)

LangChain has a class specifically for OpenAI (and many other) chat models. I
pass in my secret API key and set the temperature to 0. The default model here
is _gpt-3.5-turbo_ , but you can alternatively use _gpt-4_ using the
“model_name” input argument. You can further customize the chat model by
setting other [input arguments](https://api.python.langchain.com/en/latest/chat_models/langchain.chat_models.openai.ChatOpenAI.html#langchain.chat_models.openai.ChatOpenAI).

Next, we define our **prompt template**. This object allows us to generate
prompts dynamically via input strings that automatically update a base
template. Here’s what that looks like.

    
    
    # define prompt template  
    prompt_template_text = """You are a high school history teacher grading \  
    homework assignments. Based on the homework question indicated by “**Q:**” \  
    and the correct answer indicated by “**A:**”, your task is to determine \  
    whether the student's answer is correct. Grading is binary; therefore, \  
    student answers can be correct or wrong. Simple misspellings are okay.  
      
    **Q:** {question}  
    **A:** {correct_answer}  
      
    **Student's Answer:** {student_answer}  
    """  
      
    prompt = PromptTemplate(  
                input_variables=["question", "correct_answer", "student_answer"], \  
                template = prompt_template_text)

With our LLM and prompt, we can now define our chain.

    
    
    # define chain  
    chain = LLMChain(llm=chat_model, prompt=prompt)

Next, we can pass inputs to the chain and obtain a grade in one line of code.

    
    
    # define inputs  
    question = "Who was the 35th president of the United States of America?"  
    correct_answer = "John F. Kennedy"  
    student_answer =  "FDR"  
      
    # run chain  
    chain.run({'question':question, 'correct_answer':correct_answer, \  
        'student_answer':student_answer})  
      
    # output: Student's Answer is wrong. 

While this chain can perform the grading task effectively, its outputs may not
be suitable for an automated process. For instance, in the above code block,
the LLM correctly said the student’s answer of “FDR” was wrong, but it would
be better if the LLM gave us an output in a standard format that could be used
in downstream processing.

#### Output parser

This is where **output parsers** come in handy. These are functions we can
integrate into a chain to convert LLM outputs to a standard format. Let’s see
how we can make an output parser that converts the LLM response to a boolean
(i.e. _True_ or _False_) output.

    
    
    # define output parser  
    class GradeOutputParser(BaseOutputParser):  
        """Determine whether grade was correct or wrong"""  
      
        def parse(self, text: str):  
            """Parse the output of an LLM call."""  
            return "wrong" not in text.lower()

Here, we create a simple output parser that checks if the word “wrong” is in
the LLM’s output. If not, we return _True_ , indicating the student's correct
answer. Otherwise, we return _False_ , indicating the student's answer was
incorrect.

We can then incorporate this output parser into our chain to seamlessly parse
text when we run the chain.

    
    
    # update chain  
    chain = LLMChain(  
        llm=chat_model,  
        prompt=prompt,  
        output_parser=GradeOutputParser()  
    )

Finally, we can run the chain for a whole list of student answers and print
the outputs.

    
    
    # run chain in for loop  
    student_answer_list = ["John F. Kennedy", "JFK", "FDR", "John F. Kenedy", \  
                      "John Kennedy", "Jack Kennedy", "Jacquelin Kennedy", \  
                      "Robert F. Kenedy"]  
      
    for student_answer in student_answer_list:  
        print(student_answer + " - " +   
          str(chain.run({'question':question, 'correct_answer':correct_answer, \  
                        'student_answer':student_answer})))  
        print('\n')  
      
    # Output:  
    # John F. Kennedy - True  
    # JFK - True  
    # FDR - False  
    # John F. Kenedy - True  
    # John Kennedy - True  
    # Jack Kennedy - True  
    # Jacqueline Kennedy - False  
    # Robert F. Kenedy - False

### Limitations

Prompt Engineering is more than asking ChatGPT for help writing an email or
learning about Quantum Computing. It is a **_new programming paradigm that
changes how developers can build applications_**.

While this is a powerful innovation, it has its limitations. For one, optimal
prompting strategies are LLM-dependent. For example, prompting GPT-3 to “think
step-by-step” resulted in significant performance gains on simple mathematical
reasoning tasks [8]. However, for the latest version of ChatGPT, the same
strategy doesn’t seem helpful (it already thinks step-by-step).

Another limitation of Prompt Engineering is it requires large-scale general-
purpose language models such as ChatGPT, which come at significant
computational and financial costs. This may be overkill for many use cases
that are more narrowly defined e.g. string matching, sentiment analysis, or
text summarization.

We can overcome both these limitations via **fine-tuning** pre-trained
language models. This is where we **take an existing language model and tweak
it for a particular use case.** In the [next article](https://medium.com/towards-data-science/fine-tuning-large-language-models-llms-23473d763b91) of this series, we will explore popular fine-tuning
techniques supplemented with example Python code.