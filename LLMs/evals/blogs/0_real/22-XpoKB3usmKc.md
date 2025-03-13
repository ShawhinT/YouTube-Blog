# QLoRA — How to Fine-Tune an LLM on a Single GPU
#### An introduction with Python example code (ft. Mistral-7b)

This article is part of a [larger series](https://shawhin.medium.com/list/large-language-models-llms-8e009ae3054c) on using large language models (LLMs) in practice. In the
[previous post](https://towardsdatascience.com/how-to-build-an-ai-assistant-with-openai-python-8b3b5a636f69), we saw how to fine-tune an LLM using OpenAI.
The main limitation to this approach, however, is that OpenAI’s models are
concealed behind their API, which limits what and how we can build with them.
Here, I’ll discuss an alternative way to fine-tune an LLM using open-source
models and QLoRA.

![](https://cdn-images-1.medium.com/max/800/0*C783ZfFIphu8eFdm)Photo by
[Dell](https://unsplash.com/@dell?utm_source=medium&utm_medium=referral) on
[Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

* * *

**Fine-tuning** is when we **take an existing model and tweak it for a
particular use case**. This has been a critical part of the recent explosion
of AI innovations, giving rise to ChatGPT and the like.

Although fine-tuning is a simple (and powerful) idea, applying it to LLMs
isn’t always straightforward. The key challenge is that **LLMs are (very)
computationally expensive** (i.e. they aren’t something that can be trained on
a typical laptop).

For example, standard fine-tuning of a 70B parameter model requires over 1TB
of memory [1]. For context, an A100 GPU comes with up to 80GB of memory, so
you’d (at best) need over a dozen of these $20,000 cards!

While this may deflate your dreams of building a custom AI, don’t give up just
yet. The open-source community has been working hard to make building with
these models more accessible. One popular method that has sprouted from these
efforts is **QLoRA (Quantized Low-Rank Adaptation)** , **an efficient way to
fine-tune a model without sacrificing performance**.

### **What is Quantization?**

A key part of QLoRA is so-called **quantization**. While this might sound like
a scary and sophisticated word, it is a simple idea. When you hear “
_quantizing_ ,” think of **splitting a range of numbers into buckets**.

For example, there are infinite possible numbers between 0 and 100, e.g. 1,
12, 27, 55.3, 83.7823, and so on. We could _quantize_ this range by splitting
them into buckets based on whole numbers so that (1, 12, 27, 55.3, 83.7823)
becomes (1, 12, 27, 55, 83), or we could use factors of ten so that the
numbers become (0, 0, 20, 50, 80). A visualization of this process is shown
below.

![](https://cdn-images-1.medium.com/max/800/1*wO1Qiz1NGDOfTTbFsmHloA.png)Visualization of
quantizing numbers via whole numbers or 10s. Image by author.

#### **Why we need it**

Quantization allows us to **represent a given set of numbers with less
_information_**. To see why this is important, let’s (briefly) talk about how
computers work.

Computers encode _information_ using binary digits (i.e. bits). For instance,
if I want a computer to remember the number 83.7823, this number needs to be
translated into a string of 1s and 0s (aka a bit string).

One way of doing this is via the **single-precision floating-point format**
(i.e. **FP32**), which represents numbers as a sequence of 32 bits [2]. For
example, 83.7823 can be represented as 01000010101001111001000010001010 [3].

Since a string of 32 bits has 2³² (= 4,294,967,296) unique combinations that
means we can represent 4,294,967,296 unique values with FP32. Thus, if we have
numbers from 0 to 100, the **bit count sets the precision for representing
numbers in that range**.

But there is **another side of the story**. If we use 32 bits to represent
each model parameter, each parameter will take up 4 bytes of memory (1 byte =
8 bits). Therefore, a 10B parameter model will consume 40 GB of memory. And if
we want to do full parameter fine-tuning, **that will require closer to 200GB
of memory!**[1]

This presents a dilemma for fine-tuning LLMs. Namely, **we want high
precision** for successful model training, **but we need to use as little
memory as possible** to ensure we don’t run out of it. Balancing this tradeoff
is a key contribution of QLoRA.

### **QLoRA**

**QLoRA (or Quantized Low-Rank Adaptation)** combines 4 ingredients to get the
most out of a machine’s limited memory **without sacrificing model
performance**. I will briefly summarize key points from each. More details are
available in the QLoRA paper [4].

#### **Ingredient 1: 4-bit NormalFloat**

This first ingredient takes the idea of quantization near its practical
limits. In contrast to the typical 16-bit data type (i.e., half-precision
floating point) used for language model parameters, QLoRA uses a special data
type called **4-bit NormalFloat**.

As the name suggests, this data type encodes numbers with just 4 bits. While
this means we only have 2⁴ (= 16) buckets to represent model parameters, 4-bit
NormalFloat uses a **special trick to get more out of the limited information
capacity**.

The naive way to quantize a set of numbers is what we saw earlier, where we
split the numbers into **equally-spaced** **buckets**. However, a more
efficient way would be to use **equally-sized buckets**. The difference
between these two approaches is illustrated in the figure below.

![](https://cdn-images-1.medium.com/max/800/1*dgd3vP3r8v6WczxDZRaX_Q.png)Difference between
equally-spaced and equally-sized buckets

More specifically, 4-bit NormalFloat employs an information-theoretically
optimal quantization strategy for normally distributed data [4]. Since model
parameters tend to clump around 0, this is an effective strategy for
representing LLM parameters.

#### **Ingredient 2: Double Quantization**

Despite the unfortunate name, **double quantization** generates memory savings
by **quantizing the quantization constants** (see what I mean).

To break this down, consider the following quantization process. Given an FP32
tensor, a simple way to quantize it is using the mathematical formula below
[4].

![](https://cdn-images-1.medium.com/max/800/1*v_Zz1JtE8A-lAn-ADfkVCA.png)Simple quantization formula from FP32 to Int8. Example from [4].
Image by author.

Here we are converting the FP32 representation into an Int8 (8-bit integer)
representation within the range of [-127, 127]. Notice this boils down to
**rescaling the values** in the tensor _X^(FP32)_ and **then rounding them**
to the nearest integer. We can then simplify the equation by defining a
scaling term (or quantization constant) _c^FP32 = 127/absmax(X^FP32))_.

While this naive quantization approach isn’t how it’s done in practice
(remember the trick we saw with 4-bit NormalFloat), it does illustrate that
the **quantization comes with some computational overhead** to store the
resulting constants in memory.

We could minimize this overhead by doing this process just once. In other
words, compute one quantization constant for all the model parameters.
However, this is not ideal since **it is (very) sensitive to extreme values**.
In other words, one relatively large parameter value will skew all the others
because of the _absmax()_ function in _c^FP32_.

Alternatively, we could partition the model parameters into smaller blocks for
quantization. This reduces the chances that a large value will skew other
values but comes with a larger memory footprint.

To mitigate this memory cost, we can (again) **employ quantization** , but now
**on the constants generated from this block-wise approach**. For a block size
of 64, an FP32 quantization constant adds 0.5 bits/parameter. By quantizing
these constants further, to say 8-bit, we can reduce this footprint to 0.127
bits/parameter [4].

![](https://cdn-images-1.medium.com/max/800/1*zZL5x0AibbSC23sg_fci8g.png)Visual comparison of
standard vs block-wise quantization. Image by author.

#### **Ingredient 3: Paged optimizers**

This ingredient uses Nvidia’s unified memory feature to help avoid out-of-
memory errors during training. It transfers “pages” of memory from the GPU to
the CPU when the GPU hits its limits. This is **similar to how memory is
handled between CPU RAM and machine storage** [4].

More specifically, this memory paging feature moves pages of optimizer states
to the CPU and back to the GPU as needed. This is important because there can
be intermittent memory spikes during training, which can kill the process.

#### **Ingredient 4: LoRA**

**LoRA (Low-rank Adaptation)** is a Parameter Efficient Fine-tuning (PEFT)
method. The key idea is instead of retraining all the model parameters, LoRA
**adds a relatively small number of trainable parameters while keeping the
original parameters fixed** [5].

Since I covered the details of LoRA in a [previous article](https://towardsdatascience.com/fine-tuning-large-language-models-llms-23473d763b91#8e86) of this series, I will just say we can use it to
reduce the number of trainable parameters by 100–1000X without sacrificing
model performance.

#### **Bringing it all together**

Now that we know all the ingredients of QLoRA, let’s see how we can bring them
together.

To start, consider a **standard fine-tuning process** , which consists of
retraining every model parameter. What this might look like is using FP16 for
the model parameters and gradients (4 total bytes/parameters) and FP32 for the
optimizer states, e.g. momentum and variance, and parameters (12
bytes/parameter) [1]. So, a **10B parameter model would require about 160GB of
memory to fine-tune**.

**Using LoRA** , we can immediately reduce this computational cost by
decreasing the number of trainable parameters. This works by freezing the
original parameters and adding a set of (small) adapters housing the trainable
parameters [5]. The computational cost for the model parameters and gradients
would be the same as before (4 total bytes/parameters) [1].

The **savings** , however, **comes from the optimizer states**. If we have
100X fewer trainable parameters and use FP16 for the adapter, we’d have an
additional 0.04 bytes per parameter in the original model (as opposed to 4
bytes/parameter). Similarly, using FP32 for the optimizer states, we have an
additional 0.12 bytes/parameter [4]. Therefore, **a 10B parameter model would
require about 41.6GB of memory to fine-tune**. A significant savings, but
still a lot to ask for from consumer hardware.

**QLoRA** takes things further by quantizing the original model parameters
using Ingredients 1 and 2. This reduces the cost from 4 bytes/parameter to
about 1 byte/parameter. Then, by using LoRA in the same way as before, that
would add another 0.16 bytes/parameter. Thus, **a 10B model can be fine-tuned
with just 11.6GB of memory!** This can easily run on consumer hardware like
the free T4 GPU on Google Colab.

A visual comparison of the 3 approaches is shown below [4].

![](https://cdn-images-1.medium.com/max/800/1*9_4c9SHEF0tL9n61ugAIzA.png)Visual comparison of
3 fine-tuning techniques. Based on the figure in [4]. Re-illustrated by
author.

### **Example Code: Fine-tuning Mistral-7b-Instruct to respond to YouTube
comments**

Now that we have a basic understanding of how QLoRA works let’s see what using
it looks like in code. Here, we will use a 4-bit version of the
Mistral-7B-Instruct model provided by
[TheBloke](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GPTQ) and
the Hugging Face ecosystem for fine-tuning.

This example code is available in a [Google Colab notebook](https://colab.research.google.com/drive/1AErkPgDderPW0dgE230OOjEysd0QV1sR?usp=sharing),
which can run on the (free) GPU provided by Colab. The
[dataset](https://huggingface.co/datasets/shawhin/shawgpt-youtube-comments) is
also available on Hugging Face.

🔗 [Google Colab](https://colab.research.google.com/drive/1AErkPgDderPW0dgE230OOjEysd0QV1sR?usp=sharing) | [Training Dataset](https://huggingface.co/datasets/shawhin/shawgpt-youtube-comments) | [GitHub Repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/qlora)

* * *

#### **Imports**

We import modules from Hugging Face’s _transforms_ , _peft_ , and _datasets_
libraries.

    
    
    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline  
    from peft import prepare_model_for_kbit_training  
    from peft import LoraConfig, get_peft_model  
    from datasets import load_dataset  
    import transformers

Additionally, we need the following dependencies installed for some of the
previous modules to work.

    
    
    !pip install auto-gptq  
    !pip install optimum  
    !pip install bitsandbytes

#### **Load Base Model & Tokenizer**

Next, we load the quantized model from Hugging Face. Here, we use a version of
[Mistral-7B-Instruct-v0.2 prepared by TheBloke](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GPTQ), who
has freely quantized and shared thousands of
[LLMs](https://huggingface.co/TheBloke).

Notice we are using the “Instruct” version of Mistral-7b. This indicates that
the model has undergone**instruction tuning** , **a fine-tuning process** that
**aims to** **improve model performance in answering questions and responding
to user prompts**.

Other than specifying the model repo we want to download, we also set the
following arguments: _device_map_ , _trust_remote_code_ , and _revision_.
_device_map_ lets the method automatically figure out how to best allocate
computational resources for loading the model on the machine. Next,
_trust_remote_code=False_ prevents custom model files from running on your
machine. Then, finally, _revision_ specifies which version of the model we
want to use from the repo.

    
    
    model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"  
    model = AutoModelForCausalLM.from_pretrained(  
        model_name,  
        device_map="auto",   
        trust_remote_code=False,  
        revision="main") 

Once loaded, we see the 7B parameter model only takes us **4.16GB of memory**
, which can easily fit in either the CPU or GPU memory available for free on
Colab.

Next, we load the tokenizer for the model. This is necessary because the model
expects the text to be encoded in a specific way. I discussed
[tokenization](https://towardsdatascience.com/fine-tuning-large-language-models-llms-23473d763b91#4457) in [previous articles](https://towardsdatascience.com/cracking-open-the-openai-python-api-230e4cae7971#c72b) of this series.

    
    
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

#### **Using the Base Model**

Next, we can use the model for text generation. As a first pass, let’s try to
input a test comment to the model. We can do this in 3 steps.

**First** , we craft the prompt in the proper format. Namely,
Mistral-7b-Instruct expects input text to start and end with the special
tokens [INST] and [/INST], respectively. **Second** , we tokenize the prompt.
**Third** , we pass the prompt into the model to generate text.

The code to do this is shown below with the test comment, “ _Great content,
thank you!_ ”

    
    
    model.eval() # model in evaluation mode (dropout modules are deactivated)  
      
    # craft prompt  
    comment = "Great content, thank you!"  
    prompt=f'''[INST] {comment} [/INST]'''  
      
    # tokenize input  
    inputs = tokenizer(prompt, return_tensors="pt")  
      
    # generate output  
    outputs = model.generate(input_ids=inputs["input_ids"].to("cuda"),   
                                max_new_tokens=140)  
      
    print(tokenizer.batch_decode(outputs)[0])

The response from the model is shown below. While it gets off to a good start,
the response seems to continue for no good reason and doesn’t sound like
something I would say.

    
    
    I'm glad you found the content helpful! If you have any specific questions or   
    topics you'd like me to cover in the future, feel free to ask. I'm here to   
    help.  
      
    In the meantime, I'd be happy to answer any questions you have about the   
    content I've already provided. Just let me know which article or blog post   
    you're referring to, and I'll do my best to provide you with accurate and   
    up-to-date information.  
      
    Thanks for reading, and I look forward to helping you with any questions you   
    may have!

#### Prompt Engineering

This is where **prompt engineering** is helpful. Since a [previous article](https://medium.com/towards-data-science/prompt-engineering-how-to-trick-ai-into-solving-your-problems-7ce1ed3b553f) in this series covered this
topic in-depth, I’ll just say that prompt engineering involves **crafting
instructions that lead to better model responses**.

Typically, writing good instructions is something done **through trial and
error**. To do this, I tried several prompt iterations using
[together.ai](https://www.together.ai/), which has a free UI for many open-
source LLMs, such as Mistral-7B-Instruct-v0.2.

Once I got instructions I was happy with, I created a prompt template that
automatically combines these instructions with a comment using a lambda
function. The code for this is shown below.

    
    
    intstructions_string = f"""ShawGPT, functioning as a virtual data science \  
    consultant on YouTube, communicates in clear, accessible language, escalating \  
    to technical depth upon request. \  
    It reacts to feedback aptly and ends responses with its signature '–ShawGPT'. \  
    ShawGPT will tailor the length of its responses to match the viewer's comment,   
    providing concise acknowledgments to brief expressions of gratitude or \  
    feedback, thus keeping the interaction natural and engaging.  
      
    Please respond to the following comment.  
    """  
      
    prompt_template =   
        lambda comment: f'''[INST] {intstructions_string} \n{comment} \n[/INST]'''  
      
    prompt = prompt_template(comment)
    
    
    The Prompt  
    -----------  
      
    [INST] ShawGPT, functioning as a virtual data science consultant on YouTube,   
    communicates in clear, accessible language, escalating to technical depth upon   
    request. It reacts to feedback aptly and ends responses with its signature   
    '–ShawGPT'. ShawGPT will tailor the length of its responses to match the   
    viewer's comment, providing concise acknowledgments to brief expressions of   
    gratitude or feedback, thus keeping the interaction natural and engaging.  
      
    Please respond to the following comment.  
       
    Great content, thank you!   
    [/INST]

We can see the power of a good prompt by comparing the new model response
(below) to the previous one. Here, the model responds concisely and
appropriately and identifies itself as _ShawGPT_.

    
    
    Thank you for your kind words! I'm glad you found the content helpful. –ShawGPT

#### **Prepare Model for Training**

Let’s see how we can improve the model’s performance through fine-tuning. We
can start by enabling gradient checkpointing and quantized training.
**Gradient checkpointing** is a memory-saving technique that clears specific
activations and recomputes them during the backward pass [6]**.** **Quantized
training** is enabled using the method imported from _peft_.

    
    
    model.train() # model in training mode (dropout modules are activated)  
      
    # enable gradient check pointing  
    model.gradient_checkpointing_enable()  
      
    # enable quantized training  
    model = prepare_model_for_kbit_training(model)

Next, we can set up training with LoRA via a configuration object. Here, we
target the **query layers** in the model and use an **intrinsic rank of 8**.
Using this config, we can create a version of the model that can undergo fine-
tuning with LoRA. Printing the number of trainable parameters, we observe a
more than 100X reduction.

    
    
    # LoRA config  
    config = LoraConfig(  
        r=8,  
        lora_alpha=32,  
        target_modules=["q_proj"],  
        lora_dropout=0.05,  
        bias="none",  
        task_type="CAUSAL_LM"  
    )  
      
    # LoRA trainable version of model  
    model = get_peft_model(model, config)  
      
    # trainable parameter count  
    model.print_trainable_parameters()  
      
    ### trainable params: 2,097,152 || all params: 264,507,392 || trainable%: 0.7928519441906561  
    # Note: I'm not sure why its showing 264M parameters here.

#### **Prepare Training Dataset**

Now, we can import our training data. The dataset used here is available on
the HuggingFace Dataset Hub. I generated this dataset using comments and
responses from my [YouTube channel](https://www.youtube.com/@ShawhinTalebi).
The code to prepare and upload the dataset to the Hub is available at the
[GitHub repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/qlora).

    
    
    # load dataset  
    data = load_dataset("shawhin/shawgpt-youtube-comments")

Next, we must prepare the dataset for training. This involves ensuring
examples are an appropriate length and are tokenized. The code for this is
shown below.

    
    
    # create tokenize function  
    def tokenize_function(examples):  
        # extract text  
        text = examples["example"]  
      
        #tokenize and truncate text  
        tokenizer.truncation_side = "left"  
        tokenized_inputs = tokenizer(  
            text,  
            return_tensors="np",  
            truncation=True,  
            max_length=512  
        )  
      
        return tokenized_inputs  
      
    # tokenize training and validation datasets  
    tokenized_data = data.map(tokenize_function, batched=True)

Two other things we need for training are a **pad token** and a **data
collator**. Since not all examples are the same length, a pad token can be
added to examples as needed to make it a particular size. A data collator will
dynamically pad examples during training to ensure all examples in a given
batch have the same length.

    
    
    # setting pad token  
    tokenizer.pad_token = tokenizer.eos_token  
      
    # data collator  
    data_collator = transformers.DataCollatorForLanguageModeling(tokenizer,   
                                                                  mlm=False)

#### **Fine-tuning the Model**

In the code block below, I define hyperparameters for model training.

    
    
    # hyperparameters  
    lr = 2e-4  
    batch_size = 4  
    num_epochs = 10  
      
    # define training arguments  
    training_args = transformers.TrainingArguments(  
        output_dir= "shawgpt-ft",  
        learning_rate=lr,  
        per_device_train_batch_size=batch_size,  
        per_device_eval_batch_size=batch_size,  
        num_train_epochs=num_epochs,  
        weight_decay=0.01,  
        logging_strategy="epoch",  
        evaluation_strategy="epoch",  
        save_strategy="epoch",  
        load_best_model_at_end=True,  
        gradient_accumulation_steps=4,  
        warmup_steps=2,  
        fp16=True,  
        optim="paged_adamw_8bit",  
    )

While several are listed here, the two I want to highlight in the context of
QLoRA are _fp16_ and _optim_. **_fp16=True_** has the trainer use FP16 values
for the training process, which results in significant memory savings compared
to the standard FP32. **_optim=”paged_adamw_8bit”_** enables Ingredient 3
(i.e. paged optimizers) discussed previously.

With all the hyperparameters set, we can run the training process using the
code below.

    
    
    # configure trainer  
    trainer = transformers.Trainer(  
        model=model,  
        train_dataset=tokenized_data["train"],  
        eval_dataset=tokenized_data["test"],  
        args=training_args,  
        data_collator=data_collator  
    )  
      
    # train model  
    model.config.use_cache = False  # silence the warnings.  
    trainer.train()  
      
    # renable warnings  
    model.config.use_cache = True

Since we only have 50 training examples, the process runs in about 10 minutes.
The training and validation loss are shown in the table below. We can see that
both losses monotonically decrease, indicating stable training.

![](https://cdn-images-1.medium.com/max/800/1*M6pvjdz3fc1e-rNUOLyPyQ.png)Training and
Validation loss table. Image by author.

#### **Loading Fine-tuned model**

The final model is freely available on the [HF hub](https://huggingface.co/shawhin/shawgpt-ft). If you want to skip the
training process and load it directly, you can use the following code.

    
    
    # load model from hub  
    from peft import PeftModel, PeftConfig  
    from transformers import AutoModelForCausalLM  
      
    model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"  
    model = AutoModelForCausalLM.from_pretrained(model_name,  
                                                 device_map="auto",  
                                                 trust_remote_code=False,  
                                                 revision="main")  
      
    config = PeftConfig.from_pretrained("shawhin/shawgpt-ft")  
    model = PeftModel.from_pretrained(model, "shawhin/shawgpt-ft")  
      
    # load tokenizer  
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

#### **Using the Fine-tuned Model**

We can use the fine-tuned model for inference in the same way as before. Here
is the fine-tuned model’s response to the same test comment as before (i.e. “
_Great content, thank you!_ ”).

    
    
    Glad you enjoyed it! –ShawGPT  
      
    (Note: I'm an AI language model, I don't have the ability to feel emotions or   
    watch videos. I'm here to help answer questions and provide explanations.)

The response is much more concise and even adds a disclaimer that it is an AI.
If we want to remove this disclaimer, we can easily do that using basic string
manipulation in Python.

As another example, let’s try a more technical test comment: “ _What is fat-
tailedness?_ ” The model’s response is given below.

    
    
    Fat-tailedness is a statistical property of a distribution. In simple terms,   
    it refers to the presence of extreme outliers or heavy tails in the   
    distribution.  
      
    For instance, consider the distribution of heights in a population. A normal   
    distribution would have most people clustered around an average height with a   
    few people deviating slightly from the mean. However, in a fat-tailed   
    distribution, you would observe a larger number of people being significantly   
    taller or shorter than the average.  
      
    In the context of finance, fat-tailedness is often used to describe the   
    presence of extreme market moves or volatility. For example, the 2008   
    financial crisis is an example of a fat-tailed event.  
      
    I hope this explanation helps! Let me know if you have any questions.  
    –ShawGPT

The response is similar to what we saw in the [previous article](https://medium.com/towards-data-science/how-to-build-an-ai-assistant-with-openai-python-8b3b5a636f69) of this series with the fine-tuned OpenAI
model. It gives a concise and appropriate explanation of fat-tailedness, but
this isn’t [how I explain fat-tailedness](https://medium.com/towards-data-science/pareto-power-laws-and-fat-tails-0355a187ee6a).

While we could attempt to capture this specialized knowledge via further fine-
tuning, a simpler approach would be to **augment the fine-tuned model using
external knowledge** from my [article series](https://medium.com/towards-data-science/pareto-power-laws-and-fat-tails-0355a187ee6a) on fat tails (and other
data science topics).

This brings up the idea of **Retrieval Augmented Generation** (i.e. **RAG**),
which will be discussed in the next article of this series.

### **What’s Next?**

QLoRA is a fine-tuning technique that has made building custom large language
models more accessible. Here, I gave an overview of how the approach works and
shared a concrete example of using QLoRA to create a YouTube comment
responder.

While the fine-tuned model did a qualitatively good job mimicking my response
style, it had some limitations in understanding specialized data science
knowledge. In the [next article of this series](https://medium.com/towards-data-science/how-to-improve-llms-with-rag-abdc132f76ac), we will see how we
can overcome this limitation by improving the model with RAG.