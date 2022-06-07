---
title: 01 - Linear Models
created: '2022-06-02T07:46:32.019Z'
modified: '2022-06-07T07:48:58.397Z'
---

# 01 - Linear Models

The linear models are one of the most commonly used type of models.
Here it will be covered how they are used in classification tasks.

**Representing the classes**: 
The number of classes in a problem is defined as $K$. Where the set of classes can be expressed as $C_k$, where $k=1,\dots,K$.

For classification problems where $K=2$, the classes are represented by the labels $0$ and $0$.

For classification problem where $K>2$, something called a 1-of-K coding scheme is used. Here a vector of length $K$ is used. If we have a class $C_j$ then all elements of the vector is zero except for the element $j$.

## Discriminant functions
A discriminant is a function that takes an input vector $x$ and assign's it to on of the $K$ classes. 

Only linear discriminant functions are covered here.
A linear discriminant function is a function where the decision surfaces are hyperplanes.

The simplest representation of a linear discriminant function is the obtained by taking the linear function of the input vector so that:
$$y(x)=W^TX+w_0$$
$W$ is the weight vector

$w_0$ is the bias

The input vector $x$ is assigned to the class $C_1$ if $y(x)\geq 0$ and to the class $C_2$ otherwise.

This means that the decision boundary is defined by the relation:
$$y(x)=0$$

Consider two points $X_A$ and $X_B$ both are on the decision boundary.
This means that this relation is true:
$$y(X_A)=y(X_B)=0$$
$$W^T(X_A-X_B)=0$$
Meaning that the vector $W$ is orthogonal to the vectors within the decision surface.

This means that the vector $W$ determines the orientation of the decision surface.

Similarly, the bias $w_0$ determines the position of the decision surface.

This can be seen if $x$ is on the decision surface aka $y(x)=0$.
Then the normal distance from the origin to the decision surface is:
$$\frac{W^TX}{\left \| W \right \|} = - \frac{w_0}{\left \| W \right \|}$$

This can used to calculate perpendicular distance $r$
$$r =\frac{y(X)}{\left \| W \right \|}$$

## Multiple classes
When expanding the the discriminant function to multiple classes, the decision surface is a hyperplane. A The naive approach will work but comes with some difficulties. This can be on the following figure:
![](@attachment/stufflin.png)

The figure on the left hand is *One against all*
The figure on the right hand is *One against one*

Here some region will have an ambiguous classification.
An alternative is to introduce a K(K-1)/2 discriminant functions, one for every possible pairs of classes. This can be seen on the right-hand of the figure. The end result is the  a lot of of different functions.
But this still have the issues of ambiguity.

To avoid these a single K discriminant function comprising K linear functions:
$$y_k(X) = W_{k}^{T}X+w_{k0}$$
and then assigning a point $x$ to class $C_k$ if $y_k(X) > y_j(x)$ for all $j\neq k$. The desicion coundary between the two classes $C_k$ and $C_j$ is then defined:
$$y_k(X) = y_j(X)$$
Hence the corresponding hyperplane is:
$$(W_k-W_j)^TX+(w_{k0}-{w_{j0}})=0$$

![](@attachment/stuffmul.png)

## Least squares for classification
The sum of square error is the error function, that tries to minimize the classification error.
The least square error has some problems, if the data set contains some outliers.
This can be seen in the figure below:

![](@attachment/stufflsq.png)
The purple line is the least square error

## keywords

*decision regions*: These are the region where different classifications are determined.

*decision boundaries/decision surfaces*: These har the linear functions that create the decision regions.

*linearly separable*: If the dataset can be separated by a linear decision surfaces.

*1-of-K coding scheme* and *one-hot encoding*: These are the two ways to represent the classes in a classification problem.

*Instance space*: This is the space of all possible values of the input features.

