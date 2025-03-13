# Python QuickStart for People Learning AI
#### A beginner-friendly guide

![](https://cdn-images-1.medium.com/max/800/1*-mbIMdku5V3kilFWTRHuLQ.png)Image
from Canva.

Python has become the de facto programming language for AI and data science.
Although no-code solutions exist, learning how to code is still essential to
build fully custom AI projects and products. In this article, I share a
beginner QuickStart guide to AI development with Python. I’ll cover the basics
and then share a concrete example with code.

* * *

**Python** is a programming language, i.e., **a way to give computers precise
instructions to do things we can’t or don’t want to do** [1].

This is handy when **automating a unique task without an off-the-shelf
solution**. For example, if I wanted to automate writing and sending
personalized meeting follow-ups, I could write a Python script to do this.

With tools like ChatGPT, it’s easy to imagine a future where one could
describe _any_ bespoke task in plain English, and the computer would just do
it. However, such a consumer product does not exist right now. Until such
products become available, there is tremendous value in knowing (at least a
little) Python.

### **Coding is Easier Than Ever**

While current AI products (e.g. ChatGPT, Claude, Gemini) haven’t made
programming obsolete (yet), they have made it easier than ever to learn how to
code. We all now have a competent and patient coding assistant who is always
available to help us learn.

Combined with the “traditional” approach of Googling all your problems,
**programmers can now move faster**. For instance, I generously use ChatGPT to
write example code and explain error messages. This accelerates my progress
and gives me more confidence when navigating new technology stacks.

### **Who This is For**

I’m writing this with a particular type of reader in mind: those **trying to
get into AI and have done a little coding** (e.g., JS, HTML/CSS, PHP, Java,
SQL, Bash/Powershell, VBA) **but are new to Python**.

I’ll start with Python fundamentals, then share example code for a simple AI
project. This is not meant to be a comprehensive introduction to Python.
Rather, it’s **meant to give you just enough to code your first AI project
with Python fast**.

_About me — I’m a data scientist and self-taught Python programmer (5 years).
While there’s still much for me to learn about software development, here I
cover what I think are the bare essentials of Python for AI/data science
projects based on my personal experience._

* * *

### **Installing Python**

Many computers come with Python pre-installed. To see if your machine has it,
go to your Terminal (Mac/Linux) or Command Prompt (Windows), and simply enter
“python”.

![](https://cdn-images-1.medium.com/max/800/1*WLRwkH-uTeg1b2ndgVFERQ.png)Using
Python in Terminal. Image by author.

If you don’t see a screen like this, you can download Python manually
([Windows](https://docs.python.org/3/using/windows.html)/
[Mac](https://docs.python.org/3/using/mac.html)). Alternatively, one can
install [Anaconda](https://www.anaconda.com/download/success), a popular
Python package system for AI and data science. If you run into installation
issues, **ask your favorite AI assistant for help!**

With Python running, we can now start writing some code. **I recommend running
the examples on your computer as we go along**. You can also download all the
example code from the [GitHub repo](https://github.com/ShawhinT/YouTube-
Blog/tree/main/python-quickstart).

### **1) Data Types**

#### **Strings & Numbers**

A **data type** (or just “type”) is **a way to classify data so that it can be
processed appropriately and efficiently in a computer**.

Types are defined by a possible set of values and operations. For example,
**strings** are **arbitrary character sequences** (i.e. text) that can be
manipulated in specific ways. Try the following strings in your command line
Python instance.

    
    
    "this is a string"  
    >> 'this is a string'
    
    
    'so is this:-1*!@&04"(*&^}":>?'  
    >> 'so is this:-1*!@&04"(*&^}":>?'
    
    
    """and  
        this is  
            too!!11!"""  
    >> 'and\n    this is\n        too!!11!'
    
    
    "we can even " + "add strings together"  
    >> 'we can even add strings together'

Although strings can be added together (i.e. concatenated), they can’t be
added to **numerical data types** like **int (i.e. integers)** or **float
(i.e. numbers with decimals)**. If we try that in Python, we will get an error
message because operations are only defined for compatible types.

    
    
    # we can't add strings to other data types (BTW this is how you write comments in Python)  
    "I am " + 29  
    >> TypeError: can only concatenate str (not "int") to str
    
    
    # so we have to write 29 as a string  
    "I am " + "29"  
    >> 'I am 29'

#### **Lists & Dictionaries**

Beyond the basic types of strings, ints, and floats, Python has types for
structuring larger collections of data.

One such type is a **list** , an **ordered collection of values**. We can have
lists of strings, numbers, strings **+** numbers, or even lists of lists.

    
    
    # a list of strings  
    ["a", "b", "c"]  
      
    # a list of ints  
    [1, 2, 3]  
      
    # list with a string, int, and float  
    ["a", 2, 3.14]  
      
    # a list of lists  
    [["a", "b"], [1, 2], [1.0, 2.0]]

Another core data type is a **dictionary** , which consists of **key-value
pair sequences** where **keys are strings** and **values can be any data
type**. This is a great way to represent data with multiple attributes.

    
    
    # a dictionary  
    {"Name":"Shaw"}  
      
    # a dictionary with multiple key-value pairs  
    {"Name":"Shaw", "Age":29, "Interests":["AI", "Music", "Bread"]}  
      
    # a list of dictionaries  
    [{"Name":"Shaw", "Age":29, "Interests":["AI", "Music", "Bread"]},   
     {"Name":"Ify", "Age":27, "Interests":["Marketing", "YouTube", "Shopping"]}]  
      
    # a nested dictionary  
    {"User":{"Name":"Shaw", "Age":29, "Interests":["AI", "Music", "Bread"]},   
     "Last_login":"2024-09-06",   
     "Membership_Tier":"Free"}

### **2) Variables**

So far, we’ve seen some basic Python data types and operations. However, we
are still missing an essential feature: variables.

**Variables** provide **an abstract representation of an underlying data type
instance**. For example, I might create a variable called user_name, which
represents a string containing my name, “Shaw.” This enables us to write
flexible programs not limited to specific values.

    
    
    # creating a variable and printing it  
    user_name = "Shaw"  
    print(user_name)  
      
    #>> Shaw

We can do the same thing with other data types e.g. ints and lists.

    
    
    # defining more variables and printing them as a formatted string.   
    user_age = 29  
    user_interests = ["AI", "Music", "Bread"]  
      
    print(f"{user_name} is {user_age} years old. His interests include {user_interests}.")  
      
    #>> Shaw is 29 years old. His interests include ['AI', 'Music', 'Bread'].

### **3) Creating Scripts**

Now that our example code snippets are getting longer, let’s see how to create
our first script. This is how we **write and execute more sophisticated
programs from the command line**.

To do that, create a new folder on your computer. I’ll call mine _python-
quickstart_. If you have a favorite **IDE (e.g., the Integrated Development
Environment)** , use that to open this new folder and create a new Python
file, e.g., my-script.py. There, we can write the ceremonial “Hello, world”
program.

    
    
    # ceremonial first program  
    print("Hello, world!")

If you don’t have an IDE (not recommended), you can use a basic text editor
(e.g. Apple’s Text Edit, Window’s Notepad). In those cases, you can **open the
text editor and save a new text file using the .py extension instead of
.txt.** _Note: If you use TextEditor on Mac, you may need to put the
application in plain text mode via Format > Make Plain Text._

We can then run this script using the Terminal (Mac/Linux) or Command Prompt
(Windows) by navigating to the folder with our new Python file and running the
following command.

    
    
    python my-script.py

Congrats! You ran your first Python script. Feel free to **expand this program
by copy-pasting the upcoming code examples and rerunning the script** to see
their outputs.

### **4) Loops and Conditions**

Two fundamental functionalities of Python (or any other programming language)
are loops and conditions.

**Loops** allow us to **run a particular chunk of code multiple times**. The
most popular is the **for loop** , which runs the same code while iterating
over a variable.

    
    
    # a simple for loop iterating over a sequence of numbers  
    for i in range(5):  
        print(i) # print ith element  
      
      
    # for loop iterating over a list  
    user_interests = ["AI", "Music", "Bread"]  
      
    for interest in user_interests:  
        print(interest) # print each item in list  
      
      
    # for loop iterating over items in a dictionary  
    user_dict = {"Name":"Shaw", "Age":29, "Interests":["AI", "Music", "Bread"]}  
      
    for key, value in user_dict.items():  
        print(key, "=", value) # print each key and corresponding value

The other core function is **conditions** , such as if-else statements, which
**enable us to program logic**. For example, we may want to check if the user
is an adult or evaluate their wisdom.

    
    
    # check if user is 18 or older  
    if user_dict["Age"] >= 18:  
        print("User is an adult")  
      
    # check if user is 1000 or older, if not print they have much to learn  
    if user_dict["Age"] >= 1000:  
        print("User is wise")  
    else:  
        print("User has much to learn")

It’s common to **use conditionals within for loops** to apply different
operations based on specific conditions, such as counting the number of users
interested in bread.

    
    
    # count the number of users interested in bread  
    user_list = [{"Name":"Shaw", "Age":29, "Interests":["AI", "Music", "Bread"]},   
                 {"Name":"Ify", "Age":27, "Interests":["Marketing", "YouTube", "Shopping"]}]  
    count = 0 # intialize count  
      
    for user in user_list:  
        if "Bread" in user["Interests"]:  
            count = count + 1 # update count  
      
    print(count, "user(s) interested in Bread")

### **5) Functions**

**Functions** are **operations we can perform on specific data types**.

We’ve already seen a basic function _print()_ , which is defined for any
datatype. However, there are a few other handy ones worth knowing.

    
    
    # print(), a function we've used several times already  
    for key in user_dict.keys():  
        print(key, ":", user_dict[key])  
      
      
    # type(), getting the data type of a variable  
    for key in user_dict.keys():  
        print(key, ":", type(user_dict[key]))  
      
    # len(), getting the length of a variable  
    for key in user_dict.keys():  
        print(key, ":", len(user_dict[key]))  
    # TypeError: object of type 'int' has no len()

We see that, unlike _print()_ and _type()_ , _len()_ is not defined for all
data types, so it throws an error when applied to an int. There are several
other **type-specific functions** like this.

    
    
    # string methods  
    # --------------  
    # make string all lowercase  
    print(user_dict["Name"].lower())  
      
    # make string all uppercase  
    print(user_dict["Name"].upper())  
      
    # split string into list based on a specific character sequence  
    print(user_dict["Name"].split("ha"))  
      
    # replace a character sequence with another  
    print(user_dict["Name"].replace("w", "whin"))
    
    
    # list methods  
    # ------------  
    # add an element to the end of a list  
    user_dict["Interests"].append("Entrepreneurship")  
    print(user_dict["Interests"])  
      
    # remove a specific element from a list  
    user_dict["Interests"].pop(0)  
    print(user_dict["Interests"])  
      
    # insert an element into a specific place in a list  
    user_dict["Interests"].insert(1, "AI")  
    print(user_dict["Interests"])
    
    
    # dict methods  
    # ------------  
    # accessing dict keys  
    print(user_dict.keys())  
      
    # accessing dict values  
    print(user_dict.values())  
      
    # accessing dict items  
    print(user_dict.items())  
      
    # removing a key  
    user_dict.pop("Name")  
    print(user_dict.items())  
      
    # adding a key  
    user_dict["Name"] = "Shaw"  
    print(user_dict.items())

While the core Python functions are helpful, the real power comes from
creating **user-defined functions** to **perform custom operations**.
Additionally, custom functions allow us to write much cleaner code. For
example, here are some of the previous code snippets repackaged as user-
defined functions.

    
    
    # define a custom function  
    def user_description(user_dict):  
        """  
            Function to return a sentence (string) describing input user  
        """  
        return f'{user_dict["Name"]} is {user_dict["Age"]} years old and is interested in {user_dict["Interests"][0]}.'  
      
    # print user description  
    description = user_description(user_dict)  
    print(description)  
      
    # print description for a new user!  
    new_user_dict = {"Name":"Ify", "Age":27, "Interests":["Marketing", "YouTube", "Shopping"]}  
    print(user_description(new_user_dict))
    
    
    # define another custom function  
    def interested_user_count(user_list, topic):  
        """  
            Function to count number of users interested in an arbitrary topic  
        """  
        count = 0  
      
        for user in user_list:  
            if topic in user["Interests"]:  
                count = count + 1  
          
        return count  
      
    # define user list and topic  
    user_list = [user_dict, new_user_dict]  
    topic = "Shopping"  
      
    # compute interested user count and print it  
    count = interested_user_count(user_list, topic)  
    print(f"{count} user(s) interested in {topic}")

### **6) Libraries, pip, & venv**

Although we could implement an arbitrary program using core Python, this can
be incredibly time-consuming for some use cases. One of Python's key benefits
is its **vibrant developer community and a robust ecosystem of software
packages**. Almost anything you might want to implement with core Python
(probably) already exists as an open-source library.

We can install such packages using **Python’s native package manager, pip**.
To install new packages, we run pip commands from the command line. Here is
how we can install **numpy** , **an essential data science library** that
implements basic mathematical objects and operations.

    
    
    pip install numpy

After we’ve installed numpy, we can import it into a new Python script and use
some of its data types and functions.

    
    
    import numpy as np  
      
    # create a "vector"  
    v = np.array([1, 3, 6])  
    print(v)  
      
    # multiply a "vector"  
    print(2*v)  
      
    # create a matrix  
    X = np.array([v, 2*v, v/2])  
    print(X)  
      
    # matrix multiplication  
    print(np.matmul(X,v))

The previous pip command added numpy to our base Python environment.
Alternatively, it’s a best practice to create so-called **virtual
environments**. These are **collections of Python libraries that can be
readily interchanged for different projects**.

Here’s how to create a new virtual environment called _my-env_.

    
    
    python -m venv my-env

Then, we can activate it.

    
    
    # mac/linux  
    source my-env/bin/activate  
      
    # windows  
    .\my-env\Scripts\activate.bat

Finally, we can install new libraries, such as numpy, using pip.

    
    
    pip install numpy

 _Note: If you’re using Anaconda, check out this_[ _handy
cheatsheet_](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) _for creating a new conda environment._

Several other libraries are commonly used in AI and data science. Here is a
**non-comprehensive overview of some helpful ones for building AI projects**.

![](https://cdn-images-1.medium.com/max/800/1*j-6e7IPbjeLiN9kd52n-0Q.png)A
non-comprehensive overview of Python libs for data science and AI. Image by
author.

### **Example Code: Extracting summary and keywords from research papers**

Now that we have been exposed to the basics of Python, let’s see how we can
use it to implement a simple AI project. Here, I will use the OpenAI API to
create a research paper summarizer and keyword extractor.

Like all the other snippets in this guide, the example code is available at
the [GitHub repository](https://github.com/ShawhinT/YouTube-Blog/tree/main/python-quickstart).

* * *

#### Install Dependencies

We start by installing a few helpful libraries. You can use the same _my-env_
environment we created earlier or make a new one. Then, you can install all
the required packages using the _requirements.txt_ file from the [GitHub
repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/python-quickstart).

    
    
    pip install -r requirements.txt

This line of code scans each library listed in _requirements.txt_ and installs
each.

#### Imports

Next, we can create a new Python script and import the needed libraries.

    
    
    import fitz  # PyMuPDF  
    import openai  
    import sys

Next, to use OpenAI’s Python API, we will need to import an AI key. Here’s one
way to do that.

    
    
    from sk import my_sk  
      
    # Set up your OpenAI API key  
    openai.api_key = my_sk

Note that _sk_ is not a Python library. Rather, it is a separate Python script
that defines a single variable, **_my_sk_** , which is a **string consisting
of my OpenAI API key** i.e. a unique (and secret) token allowing one to use
OpenAI’s API.

I shared a beginner-friendly introduction to APIs, OpenAI’s API, and setting
up an API key in a [previous article](https://towardsdatascience.com/cracking-
open-the-openai-python-api-230e4cae7971).

#### Read PDF

Next, we will create a function that, given the path to a research paper saved
as a .pdf file, will extract the abstract from the paper.

    
    
    # Function to read the first page of a PDF and extract the abstract  
    def extract_abstract(pdf_path):  
      
        # Open the PDF file and grab text from the 1st page  
        with fitz.open(pdf_path) as pdf:  
            first_page = pdf[0]  
            text = first_page.get_text("text")  
          
        # Extract the abstract (assuming the abstract starts with 'Abstract')  
          
        # find where abstract starts  
        start_idx = text.lower().find('abstract')   
          
        # end abstract at introduction if it exists on 1st page  
        if 'introduction' in text.lower():  
            end_idx = text.lower().find('introduction')    
        else:  
            end_idx = None  
          
        # extract abstract text  
        abstract = text[start_idx:end_idx].strip()  
      
        # if abstract appears on 1st page return it, if not resturn None  
        if start_idx != -1:  
            abstract = text[start_idx:end_idx].strip()  
            return abstract  
        else:  
            return None

#### Summarize with LLM

Now that we have our abstract text, we can use an LLM to summarize it and
generate keywords. Here, I define a function to pass an abstract to OpenAI’s
GPT-4o-mini model to do this.

    
    
    # Function to summarize the abstract and generate keywords using OpenAI API  
    def summarize_and_generate_keywords(abstract):  
      
        # Use OpenAI Chat Completions API to summarize and generate keywords  
        prompt = f"Summarize the following paper abstract and generate (no more than 5) keywords:\n\n{abstract}"  
          
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
        summary = response.choices[0].message.content  
        return summary

#### Bring it all together

Finally, we can use our user-defined functions to generate summaries and
keywords for any research paper passed to the program from the command line.

    
    
    # Get the PDF path from the command-line arguments  
    pdf_path = sys.argv[1]  
      
    # Extract abstract from the PDF  
    abstract = extract_abstract(pdf_path)  
      
    # if abstract exists on first page, print summary.  
    if abstract:  
        # Summarize and generate keywords  
        summary = summarize_and_generate_keywords(abstract)  
          
        print(summary)  
    else:  
        print("Abstract not found on the first page.")

We can then execute our program from the command line.

    
    
    python summarize-paper.py "files/attention-is-all-you-need.pdf"
    
    
    Output:  
    The paper introduces the Transformer, a novel network architecture for sequence  
    transduction tasks that relies solely on attention mechanisms, eliminating the   
    need for recurrent and convolutional structures. The Transformer demonstrates   
    superior performance in machine translation tasks, achieving a BLEU score of   
    28.4 on the WMT 2014 English-to-German translation and a state-of-the-art   
    score of 41.8 on the English-to-French translation task, while also being more   
    efficient in training time. Additionally, the Transformer shows versatility by   
    successfully applying to English constituency parsing with varying amounts of   
    training data.  
      
    **Keywords:** Transformer, attention mechanisms, machine translation,   
    BLEU score, neural networks.


### What’s Next?

Here, we covered some Python fundamentals and implemented our first AI
project! Although we covered a lot, there is still much more to learn.

The next step here is to implement your own AI project. This is the best way
to keep learning. However, before we go, here are some tips.

  * Use Google and ChatGPT _generously_ whenever you get stuck
  * “Figuring it out” is a key skill you must develop as a programmer
  * Check out the data scientist’s favorite tool: [Jupyter Notebooks](https://jupyter.org/)
  * Hack the example from this guide to get started!