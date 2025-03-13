# Independent Component Analysis (ICA)
#### Finding hidden factors in data

This is the final post in a two-part series on [**Principal Component Analysis
(PCA)**](https://towardsdatascience.com/principal-component-analysis-pca-79d228eb9d24) and **Independent Component Analysis (ICA)**. Although the
techniques are similar, they are, in fact, different approaches and perform
different tasks. In this post, I will provide a high-level introduction to
ICA, compare it to PCA, and give an example of using ICA to remove blink
artifacts from EEG data.

* * *

![](https://cdn-images-1.medium.com/max/800/1*uawuRZGzXJhO9jwJGKOseg.png)The
simplest version of the “Cocktail Party Problem”. Image by author.

### ICA

The standard problem used to describe ICA is the “Cocktail Party Problem”. In
its simplest form, imagine two people having a conversation at a cocktail
party (like the red and blue speakers above). For whatever reason, you have
two microphones placed near both party-goers (like the purple and pink
microphones above). Both voices are heard by _both_ microphones at different
volumes based on the distance between the person and the microphone. In other
words, we record two files that include audio from the two party-goers mixed
together. The problem then is, _how can we separate the two voices in each
file to obtain isolated recordings of each speaker?_

This problem is solved easily with I**ndependent Component Analysis (ICA),**
which **transforms a set of vectors into a maximally independent set**.
Returning to our “Cocktail Party Problem,” ICA will convert the two mixed
audio recordings (represented by purple and pink waveforms below) into two
unmixed recordings of each individual speaker (represented by blue and red
waveforms below). Notice that the **number of inputs and outputs are the
same** , and since the outputs are mutually independent, there is no obvious
way to drop components like in **Principal Component Analysis (PCA)**.

![](https://cdn-images-1.medium.com/max/800/1*Ug4bTpek2z-ZXJjZZ5RO0w.png)Converting mixed
signals to independent components using ICA. Image by author.

#### How it works

There are **two key assumptions** made in ICA. The hidden independent
components we are trying to uncover must be one, **statistically independent**
and two, **non-Gaussian**. By independent, I mean information about **x** does
not give you information about **y** and vice versa. Mathematically, this
translates to,

![](https://cdn-images-1.medium.com/max/800/1*zkcyzP8bvLPEZZVRwo1fQA.png)Mathematical
definition of statistical independence. Image by author.

Where _p(x)_ represents the probability distribution of x. _p(x,y)_ represents
the joint distribution of x and y. The non-Gaussian assumption simply means
the independent components have distributions that are not Gaussian, meaning
it doesn’t look like a bell curve.

![](https://cdn-images-1.medium.com/max/800/1*xD2LlTB55CY5LpHsSSjquw.png)Non-
Gaussianity is a key assumption for ICA. Image by author.

The first assumption is the starting point of ICA. We want to disentangle
information to derive a set of independent factors. If there are not multiple
independent generators of information to uncover, there really isn’t a need
for ICA. For example, imagine using ICA for the “Cocktail Party Problem”, but
with only one partygoer, what one could call the COVID birthday party problem.
It wouldn’t make much sense.

The need for the second assumption lies in the mathematics. ICA uses the idea
of **non-Gaussianity** to uncover independent components. Non-Gaussianity
**quantifies how _far_ the distribution of a random variable is from being
Gaussian**. Example measures of non-Gaussianity are kurtosis and negentropy.
Why such a measure is helpful follows from the **Central Limit Theorem**.
Specifically, a result that states the sum of two independent random variables
has a distribution that is _closer_ to Gaussian than either of the original
variables. ICA combines this idea, non-Gaussianity measures, and the non-
Gaussian assumption to uncover independent components hidden in data.

To illustrate this, consider a dataset with two variables **x_1** and **x_2**.
These variables serve as a basis that defines a space i.e. we can use them to
plot points in 2 dimensions. Suppose we know the two independent components
underlying the data, **s_1,** and **s_2**. These two components serve as an
alternative basis to describe the same space. Therefore, any point **y** in
this space could be written as both a linear combination of variables **x_1**
and **x_2** or components **s_1** and **s_2**.

![](https://cdn-images-1.medium.com/max/800/1*2Jv_AZ6ftqh2bS4vt_IaUQ.png)Linear combination of
measured signals i.e. input variables. Image by author.![](https://cdn-images-1.medium.com/max/800/1*zRIPs6cF3WDm7lLw5C-n4Q.png)Linear combination of
independent components. Image by author.

Going back to the Central Limit Theorem, the distribution of the sum of two
random variables will be _more Gaussian_ than either individual variable.
Thus, when a_1 and a_2 are both non-zero, the distribution of **y** will be
_more Gaussian_ than either **s_1** or **s_2**. The reverse is that if either
a_1 or a_2 is zero, then the distribution of **y** will be _less Gaussian_
than in the former case. And, if the non-Gaussian assumption of **s_1** and
**s_2** holds, it will not be Gaussian at all since **y** will be exactly
equal to one of the independent components!

In other words, the non-Gaussianity of **y** is maximized when it is directly
proportional to one of the independent components. This allows us to frame ICA
as an optimization problem. For example,

![](https://cdn-images-1.medium.com/max/800/1*kMpEifOAHgdR2Swm4Hm8pQ.png)Framing ICA as an
optimization problem for a single independent component. Image by author.

Where we want to find the values of w_1 and w_2 that maximize the kurtosis of
a linear combination of our known input variables. These optimal values of w_1
and w_2 will define an independent component.

![](https://cdn-images-1.medium.com/max/800/1*Ot2KxDnr51TE67jhYfR6ow.png)Solutions to ICA
optimization problem define independent components.

More generally, we can solve for the matrix of weights, **W** , which
maximizes the non-Gaussianity of the matrix multiplication of **W** and a data
matrix, **X**.

![](https://cdn-images-1.medium.com/max/800/1*7uViihS8d4kx7c-9ffb-VQ.png)Framing ICA as an optimization problem for multiple independent
components. Image by author.

#### Key Points

I may have (once again) gone too far into the mathematical weeds. As a
takeaway, I will highlight three key points of ICA:

  * The number of inputs equals the number of outputs
  * Assumes independent components are statistically independent
  * Assumes independent components are non-Gaussian

### PCA vs ICA

Before moving on to an example, I will briefly compare PCA and ICA. Although
the two approaches seem related, they perform different tasks. Specifically,
**PCA** is often used to **compress information** i.e. dimensionality
reduction. In contrast, **ICA** aims to **separate information** by
transforming the input space into a maximally independent basis. A commonality
is both approaches require input data to be **autoscaled** i.e. **subtract
each column by its mean and divide by its standard deviation**. This is one
reason why PCA is usually a good thing to do before performing ICA.

![](https://cdn-images-1.medium.com/max/800/1*a9QDAXe9YBu3huWY5iiLJQ.png)Comparison of PCA and
ICA. Image by author.

### Example: Blink Removal from EEG

As always, I will close with a concrete, practical example. I will use ICA to
remove blink artifacts from EEG data in this example. Code is available in the
[**GitHub repository**](https://github.com/ShawhinT/YouTube/tree/main/ica).

Electroencephalography (EEG) is a technique that measures electrical activity
resulting from the brain. A major disadvantage of EEG is its sensitivity to
motion and other non-brain artifacts. One such artifact occurs whenever
participants blink. In the below figure, blink artifacts can plainly be seen
via spikes in the voltage vs time plot of the Fp1 electrode (near the front of
the head).

![](https://cdn-images-1.medium.com/max/800/1*2lJs8_9ff9CWUaHF7sVKyA.png)Importing data and
plotting Fp1 voltage vs time. Image by author.

A good first step when using ICA is first performing PCA on the dataset and
doing this in Matlab is easily done with the function _pca()_. I will note
here it is critical to **autoscale** the data. This is done automatically in
the _pca()_ function. Also, here, we start with 64 columns corresponding to 64
EEG electrode voltages measured over time. After PCA, we are left with 21
columns corresponding to 21 score vectors i.e. principal components.

![](https://cdn-images-1.medium.com/max/800/1*0TM16kIZfk2AD1lXjmFpZQ.png)Code
to apply PCA to dataset. Image by author.

Next, we can train an ICA model and apply it to the PCA score matrix.

![](https://cdn-images-1.medium.com/max/800/1*6Sa4-yJJeU445WhA-uIsiQ.png)Code
to apply ICA to principal components. Image by author.

We can plot the independent components to inspect which ones correspond to
blinking artifacts.

![](https://cdn-images-1.medium.com/max/800/1*p-3nx8Dnao8Kfy4FjFZPEg.png)Plots
of 21 independent components squared. Image by author.

I use a lazy heuristic to pick out independent components representing blink
information. Namely, picking components whose square has 4 prominent peaks.
The remaining components can be used to reconstruct the original dataset
without information from these blink components.

![](https://cdn-images-1.medium.com/max/800/1*EAbPnn0THBdlst1kmyLOOA.png)Code
to pick out blink independent components and reconstruct EEG data. Image by
author.

Finally, we plot the original and resulting voltage over time plot for the Fp1
electrode.

![](https://cdn-images-1.medium.com/max/800/1*7hUIdPPEE5sFMzPK9I6zAQ.png)Fp1
signal before and after blink removal.

### Conclusion

**Independent Component Analysis (ICA)** extracts hidden factors within data
by transforming a set of variables into a new set that is maximally
independent. ICA relies on a measure of non-Gaussianity to accomplish this
task. [**Principal Component Analysis (PCA)**](https://towardsdatascience.com/principal-component-analysis-pca-79d228eb9d24) and **ICA** aim at different goals. Namely, the former
compresses information, and the latter separates information. Despite their
differences, using PCA as a preprocessing step for ICA is often helpful. This
combination of techniques has applications in financial analysis and
neuroscience.