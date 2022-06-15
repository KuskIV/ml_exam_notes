- The basis for learning neural networks (loss functions and gradient decent)
- Learning and back propagation (computational graphs, the chain rule)
- Learning in practice (stochastic gradient descent, momentum, regularisation)

Hi im going to talk about the learning of neural networks.

When training the network it is important to understand the what lose functions are used for. The lose function calculates the difference between the output of the network and the desired output. This produces the loss which is used to update the weights of the network during back propagation.

When the network is actually learning it is important to understand the proceed of learning there are gradient descent and stochastic gradient descent methods. 

gradient means the slope of the loss function as the weights are updated. Since the lose should ideally be as low as possible we want to minimize this.

Different approaches exists to determine how much change there should be in the weights. This is what gradient descent is. Gradient descent work by calculating the gradient/derivative and then going in the opposite direction. This is essentially repeated until the model converges. 

A problem with gradient descent is that it can become very computationally expensive, with larger data sets.

Stochastic gradient descent is an extension of the gradient decent algorithm. Stochastic gradient descent work by having something called a mini batch. This is essentially a sample of the data that is draw uniformly from the data.

Instead of depending only on the current gradient to update the weight, gradient descent with momentum replaces the current gradient with m (“momentum”), which is an aggregate of gradients. This aggregate is the exponential moving average of current and past gradients.

There is also the concept of regularisation. Regularisation is a technique that is used to prevent overfitting. Essentially it is a technique that penalizes the model for becoming more complex than needed. The two most common regularisation techniques are L1 and L2.

L1 penalizes sum of absolute value of weights, and drives the weights towards zero. Is useful for feature selection, as we can drop variables associated with coefficient that go to zero.

L2 penalizes sum of square weights, and drives the weights towards the origin, evenly. Is useful when you have codependent features.

Now i will talk a bit about how the weights are actually updated in the network.

To do this back propagation is used. The chain rule is used to calculate the gradient of the loss function with respect to the weights. Going backwards trough the network we use the gradient to update the weights.


