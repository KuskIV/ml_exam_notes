-    Neural network basics
-    Loss functions
-    Learning neural networks (gradient decent and stochadtic gradient descent)
-    Neural network structures


Notebook 6

I will talk about Nerual Networks. So there is a two step computation. First the inputs are combined as a weighted sum, then the output is computed with an **activation function** of the combined inputs. **Activation functions** define how the weighted sum of the input is transformed into an output from a node or nodes in a layer of the network. Two common ones are **Sigmoid** and **Hyberbolic tangent**. With **Sigmoid** the output is between 0 and 1. With **Hyberbolic tangent** the output is between -1 and 1.

The structure of a neural network is a number of input layers, all connected to some number of hidden layers, which are finally connected to the output layers. The connection between the layers have weights, which are learned during the training.

When the network is learning an imporant factor is the **loss function** or **error function** which quantifies the difference between the expected outcomt and the outcome produced by the model. The loss is used to update the weights. One example is **Mean sqaured error**, where 0 means the model is perfect. Another exmaple is log-loss which we use in the notebook.

Usually when learning a **gradient-based algorithm** is used to minimize the cost function. To do this two steps are performed iteratively.
1. Compute the gradient, that is the first-order derivative of the function at the current point.
2. Move in the oppoiste direction of the slope increase from the current point by the computed amount.

This is what gradient descent is. The idea is to pass the training set through the hidden layers of the neural netowrk and then update the parameters of the layers by computing the gradients using the training samples from the data.

Now we introduce minibathces. A mini batch means that we only take a subset of the data in one iteration. If the batch size is 1 so we only look at one traing example in each iteration it is called **Stochastic Gradient Descent**. If we instead have a match
 size of e.g. 32 the it is reffered to as **mini-batch gradient descent.**

Ultimately we usually end up in a local minimum which is a point where the value is lower than at all neigboring points, so it is no longer possible to decrease the value by making infinitesimal steps. Local maximum is the opposit.

A global minimum is the absolute lowest value. As it can be difficult to find this point, we usually settle with a point wihch is very low, but not neccesarily the lowest.

The learning rate is a positive scalar determining the size of the step. Which usually decreases over time to ensure convergence

In the exercise we experimented with diffrent learning rates and batch sizes. Here we saw that a batchsize of 32 and 64 made little difference, but larger seems slightly better. For the learning rate 0.02 seemed good, as a larger one had a negativ impact and a smaller one made the converges slower.

We also tried adding momentum. The method of momentum is designed to accelerate learning, specially in the face of high curvature, small but consistent gradients or noisy gradients. The algorithm accumalates an exponentially decaying moving average of past gradients and continues to move in their direction.

But I did not make muc of a difference.

