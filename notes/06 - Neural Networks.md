---
attachments: [Clipboard_2022-06-04-14-48-11.png]
title: 06 - Neural Networks
created: '2022-06-02T07:48:06.786Z'
modified: '2022-06-04T12:58:35.665Z'
---

# 06 - Neural Networks

This lecture took a look at neural networks, with particular focus on back propagation algorithms for learning neural networks from data.

## Neural Networks

Feedforward neural networks approximates some function and maps an input to a category. They are called feedforward because information flows through the function, and are called recurrent when they are extended to include feedback connections.

## Gradient-Based Optimization

Most network algorithms utilize optimzation, which refer to the task of either minimizing (in most cases) or maximizing some function $f(x)$ by altering $x$. The function we want to minimize is the loss function.

The derivative of a function specifies how to scale a small change in the input to obtain the corresponding change in the output. The derivative is therefore useful for minimizing a function as it tells us how to change x in order to make a small improvement on y. We for example know that $f(x-\epsilon * sign(f'(x)))$ is less than $f(x)$ for a small enough $\epsilon$, and we can thus reduce $f(x)$ by moving $x$ in small steps with the opposit sign of the derivative. This is what gradient descent is. When $f'(x)=0$, the derivative provides no information about which direction to move, and these are called stationalry points. A local minimum is a point where $f(x)$ is lower than at all neigboring points, so it is no longer possible to decrease $f(x)$ by making infinitesimal steps. Local maximum is the opposit.

A global minimum is the absolute lowest value of $f(x)$. As it can be difficult to find this point, we usually settle with a point wihch is very low, but not neccesarily the lowest.

For functions with multiple inputs, we must make use of the concept of partial derivatives. This measures how $f$ changes as only the variable $x_i$ increases at point $x$.

The learning rate is a positive scalar determining the size of the step.

## Stochastic Gradient Descent

Stochastic gradient descent is an extension of the gradient descent algorithm. A recurring problem in ML is that large trainingsets are necessary for good generalization, but large training sets are also more computationally expensive.

The cost function used by a ML algorthm often decomposes as a sum over training exampels of some per-example loss function. The cost of this operation is high, as the training set size grows to billions of exampels, where the time to take a single gradient step becomes prohibitively long.

A solution to this is to sample a minibatch of examples drawn uniformly from the training set on each step. The size of this is a relatively small number, ranging from one to a few hundred.

A crucial parameter is the learning rate. This can be fixed, but it is better to gradually decrase the learning rate over time. It can be choosen at random, but a better approach to choose it by monitoring learning curves, which is more art than science.

A simple implementation can be seen below.

![](@attachment/Clipboard_2022-06-04-14-48-11.png)

An important attribute of the algorithm, when using minibatches, is that the computation time per update does not grow with the number of training exampels. This allows convergence even when the number of training exampels becomes very large.

Stochastic gradient descent is not only used in ML, but also to train large linear models on very large datasets.

## Batch and Minibatch Algorithms

For ML algorithms, the loss function is usually a sum over the training exampels. Optimization algorithms for ML typically compute each update to the parameters based on an expected value of the cost function estimated using only a subset of the terms of the full cost funtion, by randomly sampling a small number of exmpels from the dataset, then taking an average.

Optimization algorithms using the entire training set are called batch or deterministic gradient methods, as they process the training exampels simultaneouly in a large batch.

Optimization algorithms that use only a single example at a time are time are called stochastic or online methods.

Optimizations falling in between, by using more than one but fewer than all are called minibatch methods.

It is crucial the minibatches are selected randomly, as many datasets are naturally aranged. In small datasets you can shuffle each time, but for extremely large datasets this becomes impracital, and here it will be sufficient to shuffle just once. Failing to shuffle exampels in any way can seriouly reduce the effectiveness of the algorithm.

With some datasets growing in size, it is becoming more common to use each traininig examply only once. When using large training set, overfitting is not an issue, so underfitting and computational efficiency befome the predominant conerns.

## Momentum

The method of momentum is designed to accelerate learning, specially in the face of high curvature









