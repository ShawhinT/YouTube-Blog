# The 4 Hats of a Full-Stack Data Scientist
#### How to become a data science “unicorn”

![](https://cdn-images-1.medium.com/max/800/0*W1_-BIj_JsQ1Vusg)Photo by
[Amanda Jones](https://unsplash.com/@amandagraphc?utm_source=medium&utm_medium=referral)
on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

This is the first article in a [larger series](https://shawhin.medium.com/list/full-stack-data-science-f0910c75d006)
on “Full Stack Data Science” (FSDS). Although there are distinct roles for
different aspects of a machine learning (ML) project, there is often a need
for someone who can **manage and implement projects end-to-end**. This is what
we can call a full-stack data scientist. In this article, I will introduce
FSDS and discuss its 4 _Hats_.

* * *

### **What is a Full Stack Data Scientist?**

When I first learned data science (5+ years ago), data engineering and ML
engineering were not as widespread as they are today. Consequently, the role
of a data scientist was often **more broadly defined** than what we may see
these days.

![](https://cdn-images-1.medium.com/max/800/1*OFfpBgCTh9mYfnnslWLM7g.png)Google trends over
time for data science, data engineering, and ML engineering—screenshot from
[Google trends](https://trends.google.com/trends).

For example, data scientists may have written ETL scripts, set up databases,
performed feature engineering, trained ML models, and deployed models into
production.

Although it is becoming more common to split these tasks across multiple roles
(e.g., data engineers, data scientists, and ML engineers), many situations
still call for contributors who are **well-versed in all aspects of ML** model
development. I call these contributors _full-stack data scientists_.

More specifically, I see a **full-stack data scientist** as **someone who can
manage and implement an ML solution end-to-end**. This involves formulating
business problems, designing ML solutions, sourcing and preparing data for
development, training ML models, and deploying models so their value can be
realized.

### **Why do we need them?**

Given the rise of specialized roles for implementing ML projects, this notion
of **FSDS may seem outdated**. At least, that was what I thought in my first
corporate data science role.

These days, however, the value of learning the full tech stack is becoming
increasingly obvious to me. This all started last year when I [interviewed top data science freelancers](https://towardsdatascience.com/i-spent-675-92-talking-to-top-data-scientists-on-upwork-heres-what-i-learned-4ae3d9300993) from Upwork.

Almost everyone I spoke to fit the full stack data scientist definition given
above. This wasn’t just out of fun and curiosity but **from necessity**.

A **key takeaway** from these interviews was **data science skills (alone) are
limited in their potential business impact**. To generate real-world value
(that a client will pay for), building solutions end-to-end is a must.

But this isn’t restricted to freelancing. Here are a few other contexts where
FSDS can be beneficial

  * An SMB (small-medium business) with only 1 dedicated resource for AI/ML projects
  * A lone AI/ML contributor is embedded in a business team
  * Founder who wants to build an ML product
  * Individual contributor at a large enterprise who can explore projects outside established teams

In other words, full-stack data scientists are generalists who can see the big
picture and dive into specific aspects of a project as needed. This makes them
a valuable resource for any business looking to generate value via AI and
machine learning.

### **4 Hats of FSDS**

While FSDS requires several skills, the role can be broken down into four key
hats: **Project Manager** , **Data Engineer** , **Data Scientist** , and **ML
Engineer**.

Of course, no one can be world-class in all hats (probably). But one can
certainly be above average across the board (it just takes time).

Here, I’ll break down each of these hats based on my experience as a data
science consultant and interviews with 27 data/ML professionals.

### **Hat 1: Project Manager**

The key role of a project manager (IMO) is to answer 3 questions: _what_ ,
_why_ , and _how_. In other words, _what are we building?_ _Why are we
building it?_ _How will we do it?_

While it might be easy to skip over this work (and start coding), failing to
put on the PM hat properly risks spending a lot of time (and money) **solving
the wrong problem**. Or solving the right problem in an unnecessarily complex
and expensive way.

The starting point for this is **defining the business problem**. In most
contexts, the full-stack data scientist isn’t solving their problem, so this
requires the ability to work with stakeholders to uncover the problem's root
causes. I discussed some tips on this in a [previous article](https://towardsdatascience.com/5-questions-every-data-scientist-should-hardcode-into-their-brain-3948e215750f).

Once the problem is clearly defined, one can identify how AI can solve it.
This sets the target from which to work backward to estimate project costs,
timelines, and requirements.

#### **Key skills**

  * Communication and managing relationships
  * Diagnose problems and design solutions
  * Estimating project timelines, costs, and requirements

### **Hat 2: Data Engineer**

In the context of FSDS, data engineering is concerned with **making data
readily available for model development or inference** (or both).

Since this is inherently product-focused, the DE hat may be more limited than
a typical data engineering role. More specifically, this likely won’t require
optimizing data architectures for several business use cases.

Instead, the focus will be on [**building data pipelines**](https://medium.com/towards-data-science/data-science-project-management-e8787d818ad0). This involves designing and implementing ETL (or
ELT) processes for specific use cases.

ETL stands for extract, transform, and load. It involves **extracting** data
from their raw sources, **transforming** it into a meaningful form (e.g., data
cleaning, deduplication, exception handling, feature engineering), and
**loading** it into a database (e.g., data modeling and database design).

Another important area here is **data monitoring**. While the details of this
will depend on the specific use case, the ultimate goal is to give ongoing
visibility to data pipelines via alerting systems, dashboards, or the like.

#### **Key skills**

  * Python, SQL, CLI (e.g. bash)
  * Data pipelines, ETL/ELT (Airflow, Docker)
  * A cloud platform (AWS, GCP, or Azure)

### **Hat 3: Data Scientist**

I define a data scientist as someone who **uses data to uncover regularities
in the world that can be used to drive impact**. In practice, this often boils
down to training a machine learning model (because computers are much better
than humans at finding regularities in data).

For most projects, one must **switch between this Hat and Hats 1 and 2**.
During model development, it is common to encounter insights that require
revisiting the data preparation or project scoping.

For example, one might discover that an exception was not properly handled for
a particular field or that the extracted fields do not have the predictive
power that was assumed at the project's outset.

An essential part of model training is **model validation**. This consists of
defining performance metrics that can be used to evaluate models. Bonus points
if this metric can be directly translated into a business performance metric.

With a performance metric, one can programmatically **experiment with and
evaluate several model configurations** by adjusting, for example, train-test
splits, hyperparameters, predictor choice, and ML approach. If no model
training is required, one may still want to compare the performance of
multiple pre-trained models.

#### **Key Skills**

  * Python (pandas/polars, sklearn, TensorFlow/PyTorch)
  * Exploratory Data Analysis (EDA)
  * Model Development (feature engineering, experiment tracking, hyperparameter tuning)

### **Hat 4: ML Engineer**

The final hat involves taking the ML model and turning it into an ML
solution—that is, **integrating the model into business workflows** so its
value can be realized.

A simple way to do this is to **containerize the model and set up an API** so
external systems can make inference calls. For example, the API could be
connected to an internal website that allows business users to run a
calculation.

Some use cases, however, may not be so simple and require more sophisticated
solutions. This is where an **orchestration tool** can help define complex
workflows. For example, if the model requires monthly updates as new data
become available, the whole model development process, from ETL to training to
deployment, may need to be automated.

Another important area of consideration is **model monitoring**. Like data
monitoring, this involves tracking model predictions and performance over time
and making them visible through automated alerts or other means.

While many of these processes can run on local machines, deploying these
solutions using a cloud platform is common practice. Every ML engineer (MLE) I
have interviewed uses at least 1 cloud platform and recommended cloud
deployments as a core skill of MLEs.

#### **Key Skills**

  * Containerize scripts (Docker), build APIs (FastAPI)
  * Orchestration — connecting data and ML pipelines (AirFlow)
  * A cloud platform (AWS, GCP, or Azure)

### **Becoming the Unicorn**

While a full-stack data scientist may seem like a technical unicorn, the point
(IMO) isn’t to become a guru of all aspects of the tech stack. Rather, it is
to _learn enough to be dangerous_.

In other words, it’s not about mastering everything but being able to **learn
anything you need to get the job done**. From this perspective, I surmise that
most data scientists will become “full stack” given enough time.

Toward this end, here are **3 principles** I am using to accelerate my
personal FSDS development.

  1. Have a reason to learn new skills — _e.g. build end-to-end projects_
  2. Just learn enough to be _dangerous_
  3. Keep things as simple as possible —  _i.e. don’t overengineer solutions_

### **What’s next?**

A full-stack data scientist can manage and implement an ML solution end-to-
end. While this may seem like overkill for contexts where specialized roles
exist for key stages of model development, this generalist skillset is still
valuable in many situations.

As part of my journey toward becoming a full-stack data scientist, [future articles of this series](https://shawhin.medium.com/list/full-stack-data-science-f0910c75d006) will walk through each of the 4 FSDS Hats via the end-
to-end implementation of a real-world ML project.

In the spirit of learning, if you feel anything is missing here, I invite you
to drop a comment (they are appreciated) 😁