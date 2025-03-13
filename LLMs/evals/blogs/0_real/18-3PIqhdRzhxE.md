# Local LLM Fine-Tuning on Mac (M1 16GB)
#### Beginner-friendly Python code walkthrough (ft. MLX)

This article is part of a [larger series](https://shawhin.medium.com/list/large-language-models-llms-8e009ae3054c) on using large language models (LLMs) in practice. In a
[previous post](https://towardsdatascience.com/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32), I showed how to fine-tune an LLM using a single
(free) GPU on Google Colab. While that example (and many others) readily runs
on Nvidia hardware, they are not easily adapted to M-series Macs. In this
article, I walk through an easy way to fine-tune an LLM locally on a Mac.

![](https://cdn-images-1.medium.com/max/800/0*7-r3F1guQD-CUR3v)Photo by [Myron Mott](https://unsplash.com/@s2killa?utm_source=medium&utm_medium=referral) on
[Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

* * *

With the rise of open-source large language models (LLMs) and efficient fine-
tuning methods, building custom ML solutions has never been easier. Now,
anyone with **a single GPU can fine-tune an LLM on their local machine**.

However, Mac users have been largely left out of this trend due to Apple’s
M-series chips. These chips employ a unified memory framework, which precludes
the need for a GPU. Thus, many (GPU-centric) open-source tools for running and
training LLMs are not compatible with (or don’t fully utilize) modern Mac
computing power.

I had **almost** given up on my dreams of training LLMs locally until I
discovered the MLX Python library.

### **MLX**

[**MLX**](https://ml-explore.github.io/mlx/build/html/index.html) is a Python
library developed by Apple’s Machine Learning research team to **run matrix
operations efficiently on Apple silicon**. This is important because matrix
operations are the core computations underlying neural networks.

The key benefit of MLX is it fully utilizes the M series chips' **unified
memory paradigm** , which enables modest systems (like mine — M1 16GB) to run
fine-tuning jobs on large models (e.g., Mistral 7b Instruct).

While the library doesn’t have high-level abstractions for training models
like Hugging Face, there is an [example implementation of LoRA](https://github.com/ml-explore/mlx-examples/tree/main/lora) that can be
readily hacked and adapted for another use case.

This is exactly what I do in the example below.

### **Example Code: Fine-tuning Mistral 7b Instruct**

This example is similar to one from a [previous article](https://towardsdatascience.com/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32). However, instead of using Hugging Face’s
Transformers library and Google Colab, I will use the MLX library and my local
machine (2020 Mac Mini M1 16GB).

Similar to the [previous example](https://towardsdatascience.com/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32), I will be **fine-tuning a
quantized version of Mistral-7b-Instruct to respond to YouTube comments in my
likeness**. I use the QLoRA parameter efficient fine-tuning method. If you are
unfamiliar with QLoRA, I have an overview of the method
[here](https://towardsdatascience.com/qlora-how-to-fine-tune-an-llm-on-a-single-gpu-4e44d6b5be32).

🔗 [GitHub Repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/qlora-mlx) | [Training Data](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/qlora-mlx/data) | [Pre-trained Model](https://huggingface.co/mlx-community/Mistral-7B-Instruct-v0.2-4bit)

* * *

#### **1) Setting Up Environment**

Before we run the example code, we will need to set up our Python environment.
The first step is downloading the code from the [GitHub repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/qlora-mlx).

    
    
    git clone https://github.com/ShawhinT/YouTube-Blog.git

The code for this example is in the _LLMs/qlora-mlx_ subdirectory. We can
navigate to this folder and create a new Python env (here, I call it _mlx-
env_).

    
    
    # change dir  
    cd LLMs/qlora-mlx  
      
    # create py venv  
    python -m venv mlx-env

Next, we activate the environment and install the requirements from the
requirements.txt file. _Note: mlx requires your system to have an M series
chip, Python >= 3.8, and macOS >= 13.5_.

    
    
    # activate venv  
    source mlx-env/bin/activate  
      
    # install requirements  
    pip install -r requirements.txt

#### **2) Inference with Un-finetuned Model**

Now that we have _mlx_ and other dependencies installed, let’s run some Python
code! We start by importing helpful libraries.

    
    
    # import modules (this is Python code now)  
    import subprocess  
    from mlx_lm import load, generate

We will use the _subprocess_ module to run terminal commands via Python and
the _mlx-lm_ library to run inference on our pre-trained model.

_mlx-lm_ is built on top of _mlx_ and is **specifically made for running
models from the Hugging Face hub**. Here’s how we can use it to generate text
from an existing model.

    
    
    # define inputs  
    model_path = "mlx-community/Mistral-7B-Instruct-v0.2-4bit"  
    prompt = prompt_builder("Great content, thank you!")  
    max_tokens = 140  
      
    # load model  
    model, tokenizer = load(model_path)  
      
    # generate response  
    response = generate(model, tokenizer, prompt=prompt,   
                                          max_tokens = max_tokens,   
                                          verbose=True)

_Note: Any of the hundreds of models on the Hugging Face_[ _mlx-community page_](https://huggingface.co/mlx-community) _can be readily used for
inference. If you want to use a model that isn’t available (unlikely), you can
use the_[ _scripts/convert.py_](https://github.com/ShawhinT/YouTube-Blog/blob/main/LLMs/qlora-mlx/scripts/convert.py) _script to convert it into a
compatible format._

The _prompt_builder()_ function takes in a YouTube comment and integrates it
into a prompt template, as shown below.

    
    
    # prompt format  
    intstructions_string = f"""ShawGPT, functioning as a virtual data science \  
    consultant on YouTube, communicates in clear, accessible language, escalating \  
    to technical depth upon request. \  
    It reacts to feedback aptly and ends responses with its signature '–ShawGPT'. \  
    ShawGPT will tailor the length of its responses to match the viewer's comment, \  
    providing concise acknowledgments to brief expressions of gratitude or \  
    feedback, thus keeping the interaction natural and engaging.  
      
    Please respond to the following comment.  
    """  
      
    # define lambda function  
    prompt_builder = lambda comment: f'''<s>[INST] {intstructions_string} \n{comment} \n[/INST]\n'''

Here’s how the model responds to the comment “ _Great content, thank you!_ ”
**without fine-tuning**.

    
    
    –ShawGPT: Thank you for your kind words! I'm glad you found the content helpful  
    and enjoyable. If you have any specific questions or topics you'd like me to   
    cover in more detail, feel free to ask!

While the response is coherent, there are **2 main problems** with it. 1) the
signature “-ShawGPT” is placed at the front of the response instead of the end
(as instructed), and 2) the response is much longer than how I would
_actually_ respond to a comment like this.

#### **3) Preparing Training Data**

Before we can run the fine-tuning job, we must **prepare training, testing,
and validation datasets**. Here, I use 50 real comments and responses from my
YouTube channel for training and 10 comments/responses for validation and
testing (70 total examples).

A training example is given below. It is in the JSON format, i.e., a key-value
pair where the key = “text” and the value = the merged prompt, comment, and
response.

    
    
    {"text": "<s>[INST] ShawGPT, functioning as a virtual data science consultant   
    on YouTube, communicates in clear, accessible language, escalating to technical  
     depth upon request. It reacts to feedback aptly and ends responses with its   
    signature '\u2013ShawGPT'. ShawGPT will tailor the length of its responses to   
    match the viewer's comment, providing concise acknowledgments to brief   
    expressions of gratitude or feedback, thus keeping the interaction natural and   
    engaging.\n\nPlease respond to the following comment.\n \nThis was a very   
    thorough introduction to LLMs and answered many questions I had. Thank you.   
    \n[/INST]\nGreat to hear, glad it was helpful :) -ShawGPT</s>"}

The code to generate the train, test, and val datasets from a .csv file is
available on [GitHub](https://github.com/ShawhinT/YouTube-Blog/blob/main/LLMs/qlora-mlx/data/prep-data.ipynb).

#### **4) Fine-tuning Model**

With our training data prepared, we can fine-tune our model. Here, I use the
[_lora.py_](https://github.com/ml-explore/mlx-examples/blob/main/lora/lora.py)
example script created by the _mlx_ team.

This script is saved in the [_scripts_](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/qlora-mlx/scripts) folder of the repo we cloned, and the
train/test/val data are saved in the
[_data_](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/qlora-mlx/data) folder. To run the fine-tuning job, we can run the following
terminal command.

    
    
    python scripts/lora.py --model mlx-community/Mistral-7B-Instruct-v0.2-4bit \  
                           --train \  
                           --iters 100 \  
                           --steps-per-eval 10 \  
                           --val-batches -1 \  
                           --learning-rate 1e-5 \  
                           --lora-layers 16 \  
                           --test  
      
    # --train = runs LoRA training  
    # --iters = number of training steps  
    # --steps-per-eval = number steps to do before computing val loss  
    # --val-batches = number val dataset examples to use in val loss (-1 = all)  
    # --learning-rate (same as default)  
    # --lora-layers (same as default)  
    # --test = computes test loss at the end of training

To have training run as quickly as possible, I closed out all other processes
on my machine to allocate as much memory as possible to the fine-tuning
process. On my M1 with 16GB of memory, this took about **15–20 minutes** to
run and peaked at around **13–14 GB of memory**.

_Note: I had to make one change in lines 340–341 of the_[ _lora.py script_](https://github.com/ml-explore/mlx-examples/blob/main/lora/lora.py)
_to avoid overfitting, which was changing the rank of the LoRA adapters from
r=8 to r=4._

#### **5) Inference with Fine-tuned Model**

Once training is complete, a file called _adapters.npz_ will appear in the
working directory. This contains the LoRA adapter weights.

To run inference with these, we can again use the _lora.py._ This time,
however, instead of running the script directly from the terminal, I used the
_subprocess_ module to run the script in Python. This allows me to use the
_prompt_builder()_ function defined earlier.

    
    
    # define inputs  
    adapter_path = "adapters.npz" # same as default  
    max_tokens_str = "140" # must be string  
      
    # define command  
    command = ['python', 'scripts/lora.py', '--model', model_path,   
                                            '--adapter-file', adapter_path,   
                                            '--max-tokens', max_tokens_str,   
                                            '--prompt', prompt]  
      
    # run command and print results continuously  
    run_command_with_live_output(command)

The _run_command_with_live_output()_ is a helper function (courtesy of
ChatGPT) that **continuously prints process outputs from the terminal
command**. This avoids having to wait until inference is done to see any
outputs.

    
    
    def run_command_with_live_output(command: list[str]) -> None:  
        """  
        Courtesy of ChatGPT:  
        Runs a command and prints its output line by line as it executes.  
      
        Args:  
            command (List[str]): The command and its arguments to be executed.  
      
        Returns:  
            None  
        """  
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  
      
        # Print the output line by line  
        while True:  
            output = process.stdout.readline()  
            if output == '' and process.poll() is not None:  
                break  
            if output:  
                print(output.strip())  
              
        # Print the error output, if any  
        err_output = process.stderr.read()  
        if err_output:  
            print(err_output)

Here’s how the model responds to the same comment (_Great content, thank
you!_), but now **after fine-tuning**.

    
    
    Glad you enjoyed it! -ShawGPT

This response is much better than before fine-tuning. The “-ShawGPT” signature
is in the right place, and it sounds like something I would _actually_ say.

But that’s an easy comment to respond to. Let’s look at something more
challenging, like the one below.

    
    
    Comment:   
    I discovered your channel yesterday and I am hucked, great job.   
    It would be nice to see a video of fine tuning ShawGPT using HF, I saw a video   
    you did running on Colab using Mistal-7b, any chance to do a video using your   
    laptop (Mac) or using HF spaces?
    
    
    Response:  
    Thanks, glad you enjoyed it! I'm looking forward to doing a fine tuning video   
    on my laptop. I've got an M1 Mac Mini that runs the latest versions of the HF   
    API. -ShawGPT

At first glance, this is a great response. The model responds appropriately
and does a proper sign-off. It also gets lucky in saying I have a M1 Mac Mini
😉

However, there are two issues with this. First, Mac Minis are desktops, not
laptops. Second, the example doesn’t directly use the HF API.

### What’s Next?

Here, I shared a simple local fine-tuning example for M-series Macs. The data
and code for this example are freely available on the [GitHub repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/LLMs/qlora-mlx).

I hope that this can be a helpful jumping-off point for your use cases. If you
have **any suggestions for future content** in this series, please let me know
in the comments :)