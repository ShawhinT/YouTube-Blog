# Causality: An Introduction
#### The new science of an old question

This is the first post in a series on causality. The series is based on the
work of Judea Pearl and other researchers working in this space. In this post,
I will introduce what Pearl calls “the new science of cause and effect” [1] by
connecting causality to how we think, highlighting issues with traditional
statistics, and showing how to represent causality mathematically. In future
posts, we will look more closely at two fields of causality: [**causal inference**](https://towardsdatascience.com/causal-inference-962ae97cefda) and [**causal discovery**](https://shawhin.medium.com/causal-discovery-6858f9af6dcb)**.**

* * *

![](https://cdn-images-1.medium.com/max/800/1*AHVT8OE1p87kCC5As5c-2g.png) I
know what you’re thinking.. why is there a picture of a banana here? Image by
author.

### The Banana

Consider the figure above. Yes, the banana. I’ll give you a moment.

A natural question is, “what does a banana have to do with causality?” Well,
it's funny because there is no relationship between bananas and causality.
However, your mind, either intentionally or unintentionally, probably tried to
make a connection.

It boils down to the basic question of _why?_ Why a banana? Why did I click on
this blog post? Why am I still reading this? The fact is this is we are
constantly asking ourselves why. Our minds automatically try to weave together
_causal_ stories to help us make sense of a perhaps senseless world.
Derivatives of this question go as follows. What is the cause? What is the
reason for this? or What’s next? Where is this going?

Although this causal way of thinking is natural to us, our traditional tools
of statistics cannot easily handle causality. Three main points will
illustrate the inadequacies of traditional statistics in this context. I will
call these points the _3 traps of statistics_.

### 3 Traps of Statistics

#### Trap 1: Spurious Correlation

We’ve all heard the old adage that _correlation is not causation_. This
statement summarizes the concept of **spurious correlation, a** **statistical
correlation with no causal implications**. Consider the figure below (I
promise no banana this time). There exists a strong correlation (66%) between
the yearly number of people who drowned in a pool and the number of Nick Cage
movies. Clearly, and hilariously, these two variables are not causally linked
in any way, despite their correlation. More ridiculous examples can be found
at the image source [[2](https://tylervigen.com/spurious-correlations)].

![](https://cdn-images-1.medium.com/max/800/1*9HqEXfiYYwAZ3_tw2eJpiA.png)Correlation between
yearly number of people who drowned by pool and number of Nick Cage movies.
Source: <https://tylervigen.com/spurious-correlations>

Although this is a silly example, it serves as a reminder that we must be
careful when working with correlations. One may point toward establishing
statistical significance, however, there are two obstacles to that. First,
this is much easier said than done in the real world (what’s a good p-value?
how much data do we need?), and second, even statistical significance is not
sufficient to conclude causality. As we can see from another satirical, yet
“statistically valid”, story about storks and babies
[[3]](https://web.stanford.edu/class/hrp259/2007/regression/storke.pdf).

#### Trap 2: Simpson’s Paradox

A spurious correlation is a well-known trap of statistics, so it’s _easy_ to
be on the lookout for it. A less well-known trap is **Simpson’s Paradox**
which is **when** **the same data give contradictory conclusions depending on
how you look at them**.

Suppose there is an experimental treatment for heart disease. We collect data
from participants and plot the relationship between treatment and outcome. We
then plot the data in the figure below.

![](https://cdn-images-1.medium.com/max/800/1*cEOB_h6HlAWpJ-2Di72miA.png)Imaginary example of
the relationship between experimental treatment and risk of heart disease.
Image by author.

At first glance, we might conclude this is a terrible treatment. The more
someone takes the pill or engages in the prescribed behavior the worse their
risk of heart disease gets. But now suppose we look at two subpopulations of
study participants as shown in the figure below.

![](https://cdn-images-1.medium.com/max/800/1*sAisFTqy4QSNEpWQ5Eg0Fw.png)Imaginary example of
relationship between experimental treatment and risk of heart disease, now
conditioned on participant sex. Image by author.

Considering each subpopulation separately, we get the opposite result as
before. In each group, i.e. males and females, an increase in treatment is
associated with a decrease in heart disease risk. This paradox is summarized
nicely by a quote from Judea Pearl, **“we have a treatment that is good for
man, good for a woman, but bad for a person”**

Let’s look at another example, but with numbers and from reality. In the
figure below, we have batting averages for Derek Jeter and David Justice over
the years 1995 and 1996. If you take either year in isolation, David Justice
had a better performance. However, if you combine the 2 years together, Derek
Jeter performed better. Confusing right?

![](https://cdn-images-1.medium.com/max/800/1*9EG8XjJsIRzE3VTyyynXYg.png)Comparison of batting
averages for Derek Jeter and David Justice for 1995 to 1996. Source:
<https://en.wikipedia.org/wiki/Simpson%27s_paradox>

**Simpson’s paradox highlights that how you look at your data matters.** So
the question becomes, how do we partition data? Although there is no standard
method in statistics for this, causal inference provides a formalism to handle
this problem. It all boils down to causal effects, which quantify a variable's
impact on another variable after adjusting for the appropriate confounders.
The next post on causal inference will dive into this a bit more.

#### Trap 3: Symmetry

The problems with traditional statistics when thinking about causality stem
from a fundamental property of algebra, symmetry
[[4](https://doi.org/10.2202/1557-4679.1203)]. The left-hand side of an
equation equals the right-hand side (that’s the point of algebra). The equal
sign implies symmetry. However, causality is fundamentally asymmetric i.e.
causes lead to effects and not the other way around.

Let’s look at a simple example. Suppose we model the relationship between a
disease and the symptoms it produces with the expression below. _Y_ represents
the severity of the symptoms, _X_ is the severity of the disease, _m_ is the
connection between the two, and _b_ represents all other factors.

![](https://cdn-images-1.medium.com/max/800/1*O82xnwxMBRK0pcOU1FcMgg.png)Simple relationship
between symptoms and diseases. Based on work of Judea Pearl
[[4](https://doi.org/10.2202/1557-4679.1203)]. Image by author.

Using the rules of algebra, we can invert the equation above to get the
following expression.

![](https://cdn-images-1.medium.com/max/800/1*i4e0HL3_qcZlP3tCw3OV6A.png)Inverted relationship
between symptoms and diseases. Based on work of Judea Pearl
[[4](https://doi.org/10.2202/1557-4679.1203)]. Image by author.

Here’s the problem: if we interpret the first equation as diseases cause
symptoms, we have to interpret the second equation as symptoms cause diseases!
Which is, of course, not true.

When handling data, a correlation between X and Y, implies an identical
correlation between Y and X. This goes even further to the more general notion
of statistical dependence, i.e. a dependence between X and Y, implies a
dependence between Y and X. This fact eliminates the possibility of
interpreting models based solely on data (e.g. machine learning) as causal
models. With proper assumptions, however, there may be hope to learn the
causal structure from data alone, as will be discussed in a future article on
causal discovery.

So, if symmetry is a core property of algebra and statistics, we need a
different formalism that can handle asymmetric relationships to represent
causality. One way of doing this is described in the next section.

### Causality

Before diving into mathematically representing causality, we should answer a
deeper question: what is causality? **Causality** goes beyond correlation or
statistical dependency to describe the causal connections of a system.

A variable, X, can be said to cause another variable, Y, if when all
confounders are adjusted, **an intervention in X results in a change in Y, but
an intervention in Y does not necessarily result in a change in X**[1]. This
is in contrast to correlations, which are inherently symmetric i.e. if X
correlates with Y, Y correlates with X, while if X causes Y, Y may not cause
X.

![](https://cdn-images-1.medium.com/max/800/1*Wy1wYgfedxyz8TYyK-yOdg.gif)Visualization of causality. Here, an intervention in X changes Y,
however an intervention in Y leaves X unchanged. Image by author.

Causality is represented mathematically via **Structural Causal Models
(SCMs)**[[5](https://arxiv.org/abs/2102.11107)]. The two key elements of SCMs
are a graph and a set of equations. More specifically, the graph is a
**Directed Acyclic Graphs (DAG),** and**** the set of equations is a
**Structural Equation Model (SEM)**.

**DAGs** represent causal structure by showing who _listens_ to whom or, more
importantly, who _doesn’t listen_ to whom. A DAG is **a special kind of
graph** for which all edges are directed (information flow is in one
direction) and no cycles exist (information that leaves a vertex cannot return
to it). The vertices (circles) in a causal DAG represent variables and edges
(arrows) represent causation, where a variable is directly _caused_ by its
parents.

**SEMs** represent relationships between variables. These equations have two
peculiarities. First, equations are asymmetric, meaning equality only works in
one direction. This has the implication that SEMs cannot be inverted to derive
alternative SEM equations. Second, equations can be non-parametric, meaning
the functional form is not known.

Notice, at face value, an SEM can contain more information than a DAG. DAGs
outline causal connections, while SEMs can show the relationship's causal
connections and details. Although DAGs may seem unnecessary from this
perspective, there is tremendous value in _seeing_ the causal relationships in
a clear-cut way through DAGs that aren’t so obvious via SEMs. Additionally,
the choice of the DAG representation ultimately unlocked the method of
[d-separation](http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html) for evaluating
causal effects.

![](https://cdn-images-1.medium.com/max/800/1*PaQcwXAJS4IXg1D5u_7gHA.png)Example structural
causal model (SCM). Image by author.

#### Causal Inference

Now, with a formalism in hand, we can move toward analyzing causality
mathematically. A natural starting place is **causal inference**. The goal of
causal inference is to **answer questions based on the causal structure** of
the problem.

The starting point of causal inference is a causal model. In other words, you
need to know, at least, which variables _listen_ to each other. For example,
you could know that X causes Y but not the details of the interaction.

There are many facets to causal inference, such as estimating [**causal effects**](https://towardsdatascience.com/causal-effects-f30f962ffff3), using
**do-calculus** , and breaking down **confounding**. I will introduce and
explore these topics in the [next post](https://towardsdatascience.com/causal-inference-962ae97cefda) of this series on causal inference.


#### Causal Discovery

In causal inference, the causal structure of the problem is often assumed. In
other words, a DAG representing the situation is assumed. In practice,
however, the causal connections of a system are often unknown. **Causal
discovery** aims to uncover causal structures from observational data.

At its core, causal discovery is an **inverse problem**. It’s like predicting
the shape of an ice cube based on the puddle it left on the kitchen floor.
Although this sounds impossible, the basic strategy is to narrow down possible
solutions with assumptions. I will save more details for the [final post](https://shawhin.medium.com/causal-discovery-6858f9af6dcb) of this series
on causal discovery.

### Conclusion

As many data scientists (or anyone working with data) will tell you, answering
questions from data is as much art as it is science. This “new science of
cause and effect” provides a theoretical framework to help give direction to
this art. Although much of the groundwork has been laid, causality is still a
young field with several open problems.

Just like with machine learning, the cutting edge of causality is constantly
advancing. Naturally, there is no way I could comprehensively capture this
rapidly growing field in a single blog post or even in a series of blog posts.
My goal, however, in this series is to share some key ideas and resources I’ve
found helpful. In the next couple of posts, I will discuss two big ideas from
causality: [**causal inference**](https://towardsdatascience.com/causal-inference-962ae97cefda) and [**causal discovery**](https://shawhin.medium.com/causal-discovery-6858f9af6dcb).
