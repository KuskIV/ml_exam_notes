---
title: 03 - SVM
created: '2022-06-02T07:47:01.507Z'
modified: '2022-06-02T09:38:20.699Z'
---

# 03 - SVM

## Keywords

__Hyperplane__: 
__Support Vector__:

## Data Transformations

Any mapping 

$$\phi:\mathbb{R}^D\rightarrow\mathbb{R}^{D'}$$

defines how some original data x is turned into a transformend data instance $\phi(x)=(\phi_1(x), \dots, \phi_D(x))$, where the components $\phi_i(x)$ are called features or basis functions and the $\mathbb{R}^{D'}$ is hte feature space of $\phi$. $D'$ is often greater than $D$ and $\phi$ is typically non-linear. The idea is that we want to make to non-linear data into some data we can apply linear models to.

## Support Vector Machine (SVM)

The objective of the SVM is to find a hyperplane in an N-dimensional space (N is the number of features) that distinctly classifies the datapoints.

![](@attachment/Clipboard_2022-02-14-10-34-57.png)

To seperate two classes of data points, there are many possible hyperplanes. The objective is the find a plane that has the maximum margin, i.e the maximum distance between datapoints of both classes.

Hyperplanes are dicision boundaries that help classify the datapoints. Datpoints falling on either side of the hyperplane can be attributed to different classes.

The dimensionality of the hyperplane depends on the number ofeatures, if the input feature is 2, then the hyperplane is just a line. If the number of features is 3, then the hyperpalne becomes a two-dimensional plane.

Support vectors are datapoints closer to the hyperplane and influence the position and orientation of the hyperplane. Using these support vectors, we maximize the margin of the classifier. Deleting the support vectors will change the position of the hyperplane.

The margin is the distance between the decision oundary and the closest of the datapoints. Maximizing the margin leads to a particular choice of decision boundry. The location of the boundry is determined by a subset of the datapoints known as support vectors, indicated by the cickles on the right.

![](@attachment/Clipboard_2022-02-14-10-57-20.png)

In SVM, we take the output of the linear function and if the output is greater than 1 we identify with one class and if the output is -1 we identify as another class.

### Overlapping Class Distribution

The idea of a training dataset without overlap is unrealistic. We therefore need to modify the SVM to allow some training poitns to be misclassified. The penalty is a linear function of the distance and in order to do this, a slack variable greater or equal to 0 is introduced. Each datapoint has a slackvariable, where:

- $S=0$ means it is insdie the correct margin boundry
- $0<S\leq1$ means it is inside the margin, but on the correct side of the decision boundry.
- $S>1$ means it is on the wrong side of the decision boundry and is misclassified.

In the slides, this was mentioned as a simplification, but it was: The idea was that we want to calibrate $w,b$ so that for support vectors $x_n$:
$$y_n(w*x_n+b)=1$$
meaning, we want to multiply the margin with some value so it equals one (normalize the values). This is how we can always compare with 0, 1 and greater than 1.

The goal is to maximize the margin while softly penalizing points that lie on the wrong side of the maring boundry. We maximize:

$$C\sum_{n=1}^{N}S_n+\frac{1}{2}\left \| w \right \|^2$$

where the parameter $C>0$ controls the trade-off between the slack variable penalty and the margin.

### Loss function and gradient updates

In the SVM algorithm we aim to maximize the margin between the datapoints and the hyperplane.

The cost is 0 if the predicted and actual value is the same. Else the cost will be calculated.

## Nonlinear SVM

When features are not linearly seperable, one way to solve this is by adding/removing dimensinos (usually adding), and mapping datapoints to this new space using a kernel fuction. This new high-dimensioal features space makes in possible to make it a linear classification problem again.




### Mercers Theorem

A kernel function $k(x,y)$ is an inner product between the samles where $k(x,y)=\left \langle \phi(x),\phi(y)  \right \rangle$. Valid kernel functions must satisfy the Mercers condition, namely $k(x,y)$ must equal $k(y,x)$.

### Matric Version of Mercers Theorem

### Kernels

Basic kernels include:
- Polynomial Kernel: $(x*z+1)^p$
- Gaussian Kernel: $e^{-\left \| x - z \right \| / 2\sigma^2}$
- Hyperboloc Tangent: $tanh(k*x*z-\delta)$

Kernel building rules

## Kernels for Non Standard Data

### Term Frequency Vector

### Cosine SImilarity

## Kernel

The SVM kernel is a function that takes a low dimensional input space and transforms it into a higher order dimensional space. This means it converts not seperable problems into seperable problems.

## Information Retrieval

## Dynamic Programming Approach

## Summary

SVM + Kernel Functions:

Advantages:
- Powerfull method for classifiaction
- Successfull applications, e.g. in bio-informatics
- Wide variety of data tyypes and classification problems reduced to a single tyype of optimization problem

Disadvantages
- Binary classifier only: generalization to multiclass only via multipe binary classifiers
- Complexity quadratic in number of instances
- To find the “right” kernel function may require a lot of engineering


