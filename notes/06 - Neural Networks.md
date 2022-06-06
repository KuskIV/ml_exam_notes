---
attachments: [Clipboard_2022-06-04-14-48-11.png, Clipboard_2022-06-05-09-27-45.png]
title: 06 - Neural Networks
created: '2022-06-02T07:48:06.786Z'
modified: '2022-06-05T12:31:14.246Z'
---

# 06 - Neural Networks

This lecture took a look at neural networks, with particular focus on back propagation algorithms for learning neural networks from data.

## Activation Functions

Defines how the weighted sum of the input is transformed into an output from a node or nodes in a layer of the network.

## Error Functions

The loss function quantifies the difference between the expected outcomt and the outcome produced by the model. The loss is used to update the weights.

## Neural Networks

Feedforward neural networks approximates some function and maps an input to a category. They are called feedforward because information flows through the function, and are called recurrent when they are extended to include feedback connections.

## Gradient-Based Optimization

Gradient, is the rage of change. Most network algorithms utilize optimzation, which refer to the task of either minimizing (in most cases) or maximizing some function $f(x)$ by altering $x$. The function we want to minimize is the loss function.

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

The method of momentum is designed to accelerate learning, specially in the face of high curvature^[The amount by which a curve deviates from being a straight line], small but consistent gradients or noisy gradients. The algorithm accumalates an exponentially decaying moving average of past gradients and ocntinues to move in their direction.

This is achieved by introducing a variable $v$ representing the direction and speed at which the parameters move through parameter space and is set to an exponentionally decaying average of the negative gradient.

![](@attachment/Clipboard_2022-06-05-09-27-45.png)

Previoulsy the size of the stp was the norm of the gradient multiplied by the learning rage. Now it depends on how large and how aligned a sequence of gradients are. The step size is largest when many successive gradients points are in exactly the same direction.

The momentum hyperparameter can be through of as $\frac{1}{1-\alpha}$, where $\alpha=0.9$ corresponds to multiplying the maximum speed by $10$ relative to the gradience descent algorithm. Common values for $\alpha$ is $0.5$, $0.9$ and $0.99$ and it can be adapted over time, where it is increases over time.

## Nesterov Momentum

Similar to momentum, where the difference is where the gradient is evaluated. It is now evaluated after the current velocity is applied. This is done to attempto to add the _correct factor_ to the method.

## Vanishing Gradients

As more layers using certain actiation funcionts (like sigmoid) are added to neural networks, the gradients of the loss function approaches zero, making it hard to learn.

It is not an issue for smaller networks, but with $n$ hidden layers using sigmoid, $n$ small derivativese are multiplied together, making the gradient expotentially small.

In the case for sigmoid, the issue is that the output space is between 0 and 1. The issue is a large change in the input space for the sigmoid function will cause a small change in the output. Hence, the derivative becomes small.

A solution is to use ReLU, which does not have small derivatives. An issue with ReLU is a dying ReLU problem, where many neurons only output 0. This is solved by Leaky ReLU has a small slope for negative values instead of a flat slope.

## Dropout

Dropout refers to how a nerual network can choose to ignore neurons during training, choosen at random. Ignoring refers to the network not considering these neurons duing a particular forward and backward pass. 

At each training stage, indicidual neurons are either dropped out of the network with some probability, so a reduced network is left.

It is done to avoid overfitting.


## $L^*$ Parameter Reqularization

Regularization adds a penalty to the loss function of the model as it becomes more complex, to avoid overfitting. Regularization can lead to increasing training error.

### L1

L1 penalizes sum of absolute value of weights, and drives the weights towards zero. Is useful for feature selectoin, as we can drop variables associated with coefficient that go to zero.

### L2

L2 penalizes sum of square weights, and drives the weights towards the origin, evenly. Is usefull when you have codependent features.



## Chain Rule of Calculus

The chain rule is used to compute the derivatives of functions formed by composing other functions whose derivaties are known, and is used by back-propagation.

The chain rule says:

$$\frac{d}{dx} \left [ f(g(x)) \right ]=f'(g(x))g'(x)$$

It tells us how to differentiate composit functions, where a function is composit if you can write it as $f(g(x))$, meaning it is a function of a function.

## Back-Propagation

Forward propagation is when the network accepts an input $x$, which flows through the network to produce and output $\hat{y}$. During training forward propagation con cintinue onward until it produces a scalar loss, which flows back trough the network in order to compute the gradient, and this is back propagation.

To compute the gradient of some scalar $z$ with respect to one of its ancestors $x$ in the graph, we begin by observing that the gradient with respect to $z$ is givne by $\frac{dz}{dz}=1$. We can then compute the gradient with respect to each parent of $z$ in the graph by multiplying the current gradient by the Jacobian of the operation that produced $z$. WE continue multiplying by Jacobians, traveling backward through the graph in this way until we reach $x$. For any node that may be reached by going backward from $z$ through two or more paths, sum the gradients arriving from different paths at that node.

There is an example on slide 17 showing this.











