# Automating Data Pipelines with Python & GitHub Actions
### A simple (and free) way to run data workflows

This is the 4th article in a [larger
series](https://shawhin.medium.com/list/full-stack-data-science-f0910c75d006)
on Full Stack Data Science (FSDS). In the [last
post](https://towardsdatascience.com/how-to-build-data-pipelines-for-machine-
learning-b97bbef050a5), I shared a concrete example of how to build data
pipelines for machine learning projects. One limitation of the example,
however, was that the data pipeline had to be run manually. While this might
be fine for some applications, more often than not, it’s better to automate
than delegate this process to a person. In this article, I will walk through a
simple way to do this using Python and GitHub Actions.

![](https://cdn-images-1.medium.com/max/800/0*rrbrX7Jv6VlDdkNE)Photo by [Chen
Mizrach](https://unsplash.com/@chenhanozel?utm_source=medium&utm_medium=referral)
on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

* * *

A few years ago, Andrej Karpathy gave a talk describing “Operation Vacation”
[1]. This was what Tesla’s full self-driving engineering team called their
goal of completely automating the improvement of the self-driving model.

Although this goal was somewhat facetious, it illustrates an aspiration I’ve
seen in most data scientists and engineers: **the desire to build a system
that can operate autonomously** (so they can go on vacation).

Here, I will discuss how to automate a key element of any machine learning
system—the data pipeline.

### **2 Ways to Automate Data Pipelines**

While there are countless ways to build and automate data pipelines, here I’ll
categorize the approaches into two buckets: using an orchestration tool and
not using an orchestration tool.

### **Way 1: Orchestration Tool**

Orchestration tools allow developers to manage workflows with hundreds (and
even thousands) steps.

#### **Airflow**

One of the most popular orchestration tools is Airflow, which can manage
complex workflows using Python. This has made it a standard among data
engineers managing enterprise data pipelines.

A downside of Airflow, however, is that its setup and maintenance can be
complicated. Consequently, it requires a strong technical understanding of how
it works, which can take time to develop.

#### **Airflow Wrappers**

The complexity of Airflow has led to the rise of Airflow wrappers, which make
its core functionality easier to use. Popular examples of these tools include
[Dagster](https://docs.dagster.io/getting-started),
[Mage](https://docs.mage.ai/introduction/overview),
[Astronomer](https://www.astronomer.io/docs/), and
[Prefect](https://www.prefect.io/opensource) (_not a wrapper, but
comparable_).

While all these tools provide scalable and reliable ways to manage
sophisticated data workflows, **they might be overkill for many ML
applications**. So, let’s take a step back and ask how we can build pipelines
without orchestration tools.

### **Way 2: Python + Triggers**

As discussed in the [previous article](https://towardsdatascience.com/how-to-
build-data-pipelines-for-machine-learning-b97bbef050a5), data pipelines
consist of **three basic tasks: extraction, transformation, and loading**. All
of these can be implemented using Python.

For example, if we wanted to pull data from a single data source and store it
in a single database, the workflow would look like this.

![](https://cdn-images-1.medium.com/max/800/1*s-qAvBPOBXaYFZLPIUHfCQ.png)A
simple data pipeline. Image by author.

While we could surely use an orchestration tool for this, nothing stops us
from consolidating the ETL scripts into a single Python file and running that.

![](https://cdn-images-1.medium.com/max/800/1*HyhIF4jUCamsU4Yikv2CUw.png)Consolidated data
pipeline. Image by author.

#### **Automating with Triggers**

The above abstraction simplifies the execution of this pipeline, but it’s
still not automated since we manually have to run the _etl.py_ script. To take
the next step, we need to introduce a trigger.

A **trigger** runs a command when a specific criterion is satisfied. For
example, the time is 12:00 AM, or a new file appears in a directory.

This final piece allows us to fully automate the data pipeline so we can spend
our time doing more productive things e.g. read Medium articles 😉.

Here’s what our example pipeline would look like if running every day at
midnight.

![](https://cdn-images-1.medium.com/max/800/1*NFNUDbl9frRFzSfufJqWAA.png)Consolidated data
pipeline running every day at midnight via cron. Image by author.

### **GitHub Actions**

We can implement the simple workflow described above via **GitHub Actions
(GA)**. GA is a **CI/CD (continuous integration, continuous delivery)
platform** , which is a fancy way of saying it helps you automate software
testing and updating.

While data may traditionally be seen to sit outside of software, these are
inseparable when it comes to machine learning. This is because **ML uses data
to “write” software** (i.e. train models).

The biggest upside of using GA is GitHub provides free computing to run
actions for public repositories, which is great for poor developers (like me)
and simple proof-of-concept projects.

### **Example Code: Automating ETL Pipeline for YouTube Video Transcripts**

Let’s walk through a concrete example of automating a simple ETL people using
GitHub Actions. I’ll do this for the example code from the [previous
article](https://towardsdatascience.com/how-to-build-data-pipelines-for-machine-learning-b97bbef050a5) in this series, where I extracted transcripts
from all the videos from my YouTube channel.

Example code is freely available at the [GitHub
repository](https://github.com/ShawhinT/data-pipeline-example).

* * *

#### **Create ETL Python Script**

The first step is consolidating the entire ETL (Extract, Transform, Load)
pipeline into a single Python script.

I do that here by defining three files: _functions.py, data_pipeline.py_ , and
_requirements.txt_. In **_functions.py_** , each step of the pipeline is
defined as a function. These are then called in sequential order in
**_data_pipeline.py_**. **_requirements.txt_** lists all the Python
dependencies for the pipeline.

![](https://cdn-images-1.medium.com/max/800/1*wgBRc7fKxf2dB6_fpsDd-Q.png)Directory tree. Image
by author.

    
    
    # data_pipeline.py  
      
    from functions import *  
    import time  
    import datetime  
      
    print("Starting data pipeline at ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  
    print("----------------------------------------------")  
      
    # Step 1: extract video IDs  
    t0 = time.time()  
    getVideoIDs()  
    t1 = time.time()  
    print("Step 1: Done")  
    print("---> Video IDs downloaded in", str(t1-t0), "seconds", "\n")  
      
    # Step 2: extract transcripts for videos  
    t0 = time.time()  
    getVideoTranscripts()  
    t1 = time.time()  
    print("Step 2: Done")  
    print("---> Transcripts downloaded in", str(t1-t0), "seconds", "\n")  
      
    # Step 3: Transform data  
    t0 = time.time()  
    transformData()  
    t1 = time.time()  
    print("Step 3: Done")  
    print("---> Data transformed in", str(t1-t0), "seconds", "\n")  
      
    # Step 4: Generate text emebeddings  
    t0 = time.time()  
    createTextEmbeddings()  
    t1 = time.time()  
    print("Step 4: Done")  
    print("---> Embeddings generated in", str(t1-t0), "seconds", "\n")

I added time printouts for each step in the pipeline to help with code
observability and debugging. I won’t get into the guts of each step here since
those were described in the [previous
article](https://towardsdatascience.com/how-to-build-data-pipelines-for-
machine-learning-b97bbef050a5) and [this
video](https://youtu.be/6qCrvlHRhcM?si=MYHlNOuO-Q19zsuf&t=2054), but those
interested can review the code on [GitHub](https://github.com/ShawhinT/data-
pipeline-example).

#### **Create GitHub Repo**

Next, we create a GitHub repo. You can do this from the command line or the
web interface. I’ll use the latter.

To do this, I go to my GitHub repositories, hit “New”, and fill out the
following fields.

![](https://cdn-
images-1.medium.com/max/800/1*W3CXtIutP_SJCXOOnHKfwQ.png)Creating GitHub
repository. Image by author.

Then, we can clone the repo locally via the following command.

    
    
    >> git clone https://github.com/ShawhinT/data-pipeline-example.git

#### **Create Workflow .yml File**

We can now create our workflow via a .yml file. To do that, we will create a
new folder called .github/workflows and a new file called _data-pipeline.yml_.

![](https://cdn-images-1.medium.com/max/800/1*EEvKm2Z7GGedCPU8NneLTw.png)New
directory tree. Image by author.

The .yml file looks like this.

    
    
    name: data-pipeline-workflow  
      
    on:  
      push: # run on push  
      schedule:  
        - cron: "35 0 * * *" # run every day at 12:35AM  
      workflow_dispatch:  # manual triggers  
      
    jobs:  
      run-data-pipeline:  
        runs-on: ubuntu-latest  
        steps:  
          - name: Checkout repo content  
            uses: actions/checkout@v4  
            with:  
              token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}  # Use the PAT instead of the default GITHUB_TOKEN  
          - name: Setup python  
            uses: actions/setup-python@v5  
            with:  
              python-version: '3.9'  
              cache: 'pip'  
          - name: Install dependencies  
            run: pip install -r requirements.txt  
          - name: Run data pipeline  
            env:  
              YT_API_KEY: ${{ secrets.YT_API_KEY }} # import API key  
            run: python data_pipeline.py # run data pipeline  
          - name: Check for changes # create env variable indicating if any changes were made  
            id: git-check  
            run: |  
              git config user.name 'github-actions'  
              git config user.email 'github-actions@github.com'  
              git add .  
              git diff --staged --quiet || echo "changes=true" >> $GITHUB_ENV   
          - name: Commit and push if changes  
            if: env.changes == 'true' # if changes made push new data to repo  
            run: |  
              git commit -m "updated video index"  
              git push

While this may seem overwhelming to those new to GitHub Actions, it consists
of **4 key elements: name, triggers, jobs, and steps**.

Starting with the **name** , this is the name of our workflow. Here, I call it
_“data-pipeline-workflow”_.

Next, we define **triggers** for the workflow using the “ _on:_ ” syntax.
Here, I define three separate triggers. **1) on push** , meaning the workflow
will execute when new code is pushed to the repo. **2) on schedule** , meaning
it will execute via a cron job. **3) on workflow_dispatch** , this will create
a button in our repo we can manually click to run the workflow.

Workflows are made up of **jobs**. In this example, we have a single job
called “ _run-data-pipeline_ ”. We can set the operating system for the job (I
use Ubuntu here).

Jobs are then made up of **steps**. Here, our job consists of 6 steps, which
are listed below.

  1. **Checkout repo content** : uses the [pre-built checkout action](https://github.com/actions/checkout) to pull code from the repo. I also provide a Personal Access Token (PAT) to allow the action to push code to the repo, which we will create momentarily.
  2. **Setup Python** : install the desired Python version with the [pre-built action](https://github.com/actions/setup-python).
  3. **Install dependencies** : install Python libraries listed in _requirements.txt_.
  4. **Run data pipeline** : executes the _data_pipeline.py_ script. I add a secret environment variable to allow the action to use my YouTube API token without exposing it on a public repo. I will show you how to do this next.
  5. **Check for changes** : checks if any changes were made to the repo. This is necessary because if we try to push code to the repo when there are no differences, it will throw an error, and the job will fail to run.
  6. **Commit and push if changes** : if there are changes to the repo, they will be committed and pushed.

One last thing I’ll do is create a folder called “data” where we can save the
final data files.

![](https://cdn-images-1.medium.com/max/800/1*rHO7HhcvIIT7MlNgGvg1zA.png)Updated directory
tree with data folder. Image by author.

#### Add Repo Secrets

Notice in the data-pipeline.yml file I referenced two strange-looking
variables, e.g., _${{ secrets.PERSONAL_ACCESS_TOKEN }}_ and _${{
secrets.YT_API_KEY }}._

These are **repository secrets** that are accessible to GitHub Actions as
environment variables. To create them, we go to our repository settings, click
Secrets and Variables, select Actions, and click “New repository secrets”.

![](https://cdn-images-1.medium.com/max/800/1*mGBdM2iuPSWyuLR8H73Qkw.png)Creating a new
repository secret. Image by author.

To create the _PERSONAL_ACCESS_TOKEN_ variable, click on your profile icon in
the top right-hand corner > open Settings in a new tab > scroll to the bottom,
and select “Developer settings” > click “Personal access tokens” > click
“Generate new token” (classic). This will allow you to create a token that
gives the Actions write access to your repo.

Here are the details I used.

  * **Name** : data-pipeline-example-PAT
  * **Expiration** : No expiration (feel free to set this to end at some point)
  * **Select scopes** : repo

Then click “Generate token” at the bottom of the page. This will display a
long string of text, which you can copy and paste into your GitHub repository
secret.

![](https://cdn-images-1.medium.com/max/800/1*OeYhQSEDkgRX0bmjL-eexA.png)Creating _PERSONAL_ACCESS_TOKEN. Image by author._

I then create another secret variable called _YT_API_KEY_ similarly _._

#### Push and commit

With our secrets in place, we can commit and push our code.

    
    
    >> git add .  
    >> git commit -m "adding data pipeline code"  
    >> git push

Once pushed, we can go to the repo's “Actions” tab and watch the workflow run!

[**GitHub - ShawhinT/data-pipeline-example: Example data pipeline automation
with GitHub Actions**  
 _Example data pipeline automation with GitHub Actions - ShawhinT/data-
pipeline-example_ github.com](https://github.com/ShawhinT/data-pipeline-
example "https://github.com/ShawhinT/data-pipeline-
example")[](https://github.com/ShawhinT/data-pipeline-example)

### What’s next?

While orchestration tools are commonplace in data engineering, these might be
overkill for some ML use cases. Here, we saw a free and simple way to automate
a data pipeline using Python and GitHub Actions.

In the [next article](https://towardsdatascience.com/how-to-deploy-ml-solutions-with-fastapi-docker-and-gcp-de1bb8bfc59a) of this series, we will
continue going down the data science tech stack and discuss how we can
integrate this data pipeline into a semantic search system for my YouTube
videos.