# The Fast Fourier Transform (FFT)
#### With a teaspoon of intuition

This is the second part of a 3-part series on Fourier and Wavelet Transforms.
In this article, I will describe the Fast-Fourier Transform (FFT) and attempt
to give some intuition as to what makes it so _fast_. The key impact of FFT is
it provides an efficient way to compute the Fourier Transform of real-world
data. An example of applying FFT to the audio signal of a guitar is presented.

![](https://cdn-images-1.medium.com/max/800/1*QuV0VxtPWkFxuqKqPZdt3g.png)The
Fast Fourier Transform fosters key techniques in audio production. Here, audio
is edited based on its frequency spectrum.

* * *

### Discrete Fourier Transform (DFT)

In my previous post the [Fourier Transform (FT)](https://medium.com/@shawhin/time-series-signals-the-fourier-
transform-f68e8a97c1c2) and some applications were introduced. In signal
processing, this formal FT definition is not always helpful since it is rare
to have functional forms of signals. To apply this method to real world data
we need a FT definition for a discrete set of values. This is given by the
**Discrete Fourier Transform (DFT)** which is the **FT of a discrete sequence
of values**. This is _derived_ (informally) by rewriting the function in the
FT as a discrete sequence (vector if you like) and replacing the infinite sum,
with a sum over a finite number of values.

![](https://cdn-images-1.medium.com/max/800/1*BSsOXyrKR6UhtIiz1dmmeg.png)Conversion of Fourier
Transform to Discrete Fourier Transform.

Taking a closer look at the DFT expression.

![](https://cdn-images-1.medium.com/max/800/1*WtMS3H-vH3FSCXOVij128A.png)A
definition for the Discrete Fourier Transform.

Where, **x_n** is an element of our discrete signal, which is a column vector.
**f_k** is an element of our transformed discrete signal, also a column
vector. **N** is the number of elements in the vector consisting of x_n’s.
**n** and **k** are indexes corresponding to the original and transformed
signal vectors, respectively.

Let’s introduce a new term.

![](https://cdn-images-1.medium.com/max/800/1*A4Fv9AUuky7gT3MYhmGBSQ.png)Element of Fourier
Matrix.

Notice that **R_kn** has 2 indexes, **n** and **k.** Therefore, we can think
of it as an element of a 2 dimensional matrix. Substituting back into our
expression for DFT.

![](https://cdn-images-1.medium.com/max/800/1*k1Y4e2t0hZnbYFyrhUDrGg.png)

For clarity, we can write the matrices corresponding to these terms.

![](https://cdn-images-1.medium.com/max/800/1*d_Lko0nOJbn2jiLwjuLVqQ.png)Corresponding
matrices for elements in DFT.

Finally, from the properties of matrix multiplication we can represent the DFT
as a simple matrix operation. (If this is not immediately obvious, think about
a simple case where N=K=2).

![](https://cdn-images-1.medium.com/max/800/1*Ay0YC5XpDNOy9TsFkX6Kog.png)DFT
represented as a matrix multiplication.

My natural reaction to this sequence of steps is: _“Wow, that so cool! The DFT
can be written as matrix multiplication.. but so what?”_ If we want to code
this up we still (naively) will need 2 for loops, and in the case where N=K
this gives us O(N²) time complexity. Meaning, we will have to perform on the
order of N² computations to complete this operation. To put that into
perspective, the DFT of your favorite 3 minute song would have on the order
(3min*60sec/min*44100Hz)² ≈ 6E10¹³ computations!

Although things may seem hopeless, let’s take look at a concrete example of
this matrix **R**. Consider the case, where N=K=4. Again, N corresponds to the
number of elements in input signal **x** and K is the number of elements in
the DFT output **f**.

![](https://cdn-images-1.medium.com/max/800/1*80GrnZqbGnExp8mNfTleXQ.png)4 by
4 Fourier Matrix.

**R** is called the **Fourier Matrix**. Here we have the 4 by 4 Fourier matrix
whose elements were defined earlier (that “new term”). Notice, **R** is
symmetric meaning if we swapped the rows and columns we would have the same
matrix. Note, we have 4 unique terms out of 16 elements i.e. 1, -1, i, and -i.

We can also define any Fourier Matrix, R, in terms of its n=k=1 element, where
we start counting from 0. In general, this is given by,

![](https://cdn-images-1.medium.com/max/800/1*5E-Ni-egevqP9rydihtvkw.png)Fundamental term in Fourier Matrix.

We can rewrite the 4 by 4 Fourier Matrix using only this term.

![](https://cdn-images-1.medium.com/max/800/1*PMn-6hmffs7CsiXmVwWpDg.png)4 by
4 Fourier Matrix expressed in terms of fundamental.

Let’s take a look at a few more examples.

![](https://cdn-images-1.medium.com/max/800/1*2kl2eUSIEm2mttsZmsxFig.png)8 by
8 Fourier Matrix.![](https://cdn-images-1.medium.com/max/800/1*lNazs_p80FPrrVbor8XSrQ.png)4 by 4 Fourier Matrix
(again).![](https://cdn-images-1.medium.com/max/800/1*hSqtAzOoPQVf8sFlnP6PkQ.png)2 by 2 Fourier
Matrix.

We can notice, that the above Fourier matrices are comprised of a _few_ unique
terms compared to the size of each matrix. Additionally, all three matrices
seem to have elements in common. It would be nice if we could exploit this
redundancy to reduce the number of operations needed to compute the DFT… This
is exactly what the Fast-Fourier Transform does.

### Fast-Fourier Transform (FFT)

Often cited as one of the most important algorithms of the 20th century, the
**Fast-Fourier Transform (FFT)** is truly what brings the idea of the Fourier
Transform into practice. The FFT is **an efficient algorithm for computing the
DFT**. The core idea behind FFT is re-expressing Fourier Matrices as the
product of 3 (sparse) matrices, given below.

![](https://cdn-images-1.medium.com/max/800/1*f2ELOrhdr5U42CH4pxRjxQ.png)Re-
expressing the N by N Fourier Matrix as the product of 3 sparse
matrices.![](https://cdn-images-1.medium.com/max/800/1*yKSM-1LlyoFWAaiQClVRoQ.png)Definition of the
Permutation matrix, used above.

To see a concrete example, let’s return to our 4 by 4 Fourier Matrix.

![](https://cdn-images-1.medium.com/max/800/1*hejdRw_iN1rLqLH3tq30dg.png)Re-
expression of 4 by 4 Fourier Matrix![](https://cdn-images-1.medium.com/max/800/1*z5d5EcNV6mjUAtctgvKb4w.png)**From left to
right** : 2 by 2 identity matrix, D matrix, and Fourier Matrix.

We can take a moment to visually compare this example to the general
expression. Defining some objects, **I_2** is the 2 by 2 identity matrix,
**D_2** is a 2 by 2 diagonal matrix consisting of the first 2 diagonal
elements of the 4 by 4 Fourier Matrix, and finally **R_2** is the 2 by 2
Fourier Matrix.

It may not be immediately obvious why this re-expression is helpful. Let’s
walk through this operation at a high level. First we note, that multiplying
the permutation matrix by the input signal is practically free, as far as
computation. This is equivalent to reshuffling elements in the input signal
which can be done in constant time, O(1). Next, half the terms in the middle
matrix are zeroes, thus we are left with 8 non-trivial terms this gives O(2N)
time complexity. Finally, half the terms in the left-most matrix are again
zero. Additionally, half of the non-zero terms will always be 1, so there is
no need to perform a multiplication. Ultimately this leaves us with O(N) time
complexity for the left matrix.

Adding everything up, O(1) + O(2N) + O(N) = O(3N + 1) = O(13). Which is an
improvement from the original O(N²) = O(16). More generally, it turns out as N
goes to infinity we get O(N log(N)) time complexity for the FFT.

To see this, let’s take a look at one last example.

![](https://cdn-images-1.medium.com/max/800/1*K27Ku5v1fB5Z3LZ1YzlXlw.png)Re-
expression of 16 by 16 Fourier Matrix in terms of 8 by 8 Fourier Matrix

Here we have the R_16 expressed in terms of R_8. Notice, that we can play the
same game with R_8 and express it in terms of R_4.

![](https://cdn-images-1.medium.com/max/800/1*S65vYvJFWIfKkTobrk4poA.png)Re-
expression of 16 by 16 Fourier Matrix in terms of 4 by 4 Fourier Matrix

Repeating the same idea for R_4.

![](https://cdn-images-1.medium.com/max/800/1*EyRSic9gRbevgzvo6GKOIA.png)Re-
expression of 16 by 16 Fourier Matrix in terms of 2 by 2Fourier Matrix

Notice, every time we re-express a Fourier Matrix, we pick up some zeroes and
lose computations. This is what makes the FFT so powerful and leads to O(N
log(N)) time complexity. Using technical jargon, this is an example of a
recursive program.

As a brief note, N in the above expression must be a power of 2. In practice,
this can be achieved for an arbitrary signal by padding it with zeroes before
and after.

#### An Application: Harmonics of Guitar String (E2)

As both a musician and physicist, it brings me great joy to find an excuse to
merge the two fields. In this application, I apply an FFT to an audio
recording of a low E string from an electric guitar. The code and data for
this example can be accessed at this [GitHub repo](https://github.com/ShawhinT/YouTube/tree/main/FFT).

The resulting power spectrum, that is, distribution of constituent frequency
values present in audio signal, gives (approximately) the harmonic series. The
**harmonic series** is a **sequence of frequencies which are integer multiples
of some fundamental** , here E2 (~82 Hz) is our fundamental frequency. It was
only after doing this example that I realized the harmonic series approximates
the musical major scale we all know and love.

![](https://cdn-images-1.medium.com/max/800/1*BvFDaFjQRWhqcmf5mpw59g.png)**Top** : recording
of low E string (E2) from an electric guitar. **Bottom** : One-sided power
spectrum of audio signal.

### Conclusion

The Fast-Fourier Transform (FFT) is a powerful tool. It makes the Fourier
Transform applicable to real-world data. Applications include audio/video
production, spectral analysis, and computational physics.

Although FFT has made a great impact on science and technology, it is limited
in what information it can extract from a signal. Specifically, the Fourier
Transform uncovers global frequency information. In many situations, critical
information does not persist over the entirety of a signal, but rather over a
short window. An alternative analytical tool that is better suited for such
tasks is the [**Wavelet Transform**](https://towardsdatascience.com/the-wavelet-transform-e9cfa85d7b34). This is the topic of my next blog post.