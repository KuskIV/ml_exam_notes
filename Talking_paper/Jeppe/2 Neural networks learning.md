- The basis for learning neural networks (loss functions and gradient decent)
- Learning and back propagation (computational graphs, the chain rule)
- Learning in practice (stochastic gradient descent, momentum, regularisation)

## NEW

Hi im going to be talking about how neural networks learning works.
First ill talk a bit about the forward pass.
Each Layer in the network is a set of neurons, these neurons are connected to each other by the weights.
During the forward pass, the input is passed through the network, and the output is calculated, a activation function is applied to the output, and then the output is passed to the next layer.

These function essentially dictate how the output of the neurons is calculated, and based on what function is used, the output have different constraints.
Some common activation functions are:
- Sigmoid function: Sigmoid essentially maps the output of the neurons to a range between 0 and 1.
- ReLU function: ReLU is a function that is used to constrain the output of the neurons to a known range.
- Tanh function: Tanh maps the output of the neurons to a range between -1 and 1.

When we reach the output layer, we come to the loss function.
Essentially, the loss function is used to calculate the error of the network, aka how wrong we are.
There are many different loss functions, each suited to a different problem. Some of the most common ones are:
- mean squared error: It takes the difference between the output and the expected output and squares it.
- Logistic loss: Works similarly to the mean squared error, but instead of squaring it, it takes the log of the output.
- Cross entropy: Works by taking the log of the output, and then taking the sum of the outputs of the different classes. Here, the output is a probability, and the classes are the different possible outputs.

The loss function is essentially what we want to minimize to achieve a good model.
Using the error we can update the weights of the neurons with the gradient of the loss function.
We want to make the loss function converge this is done by using the gradient descent algorithm and involves a learning rate.

Now i will talk a bit about how back propagation works.
Back propagation is the process of updating the weights of the neurons based on the error of the network.
To perform back propagation, we need to introduce a new concept of chain rule.
The chain rule essentially calculates the gradient of the loss function with respect to the weights of the neurons. 
Using this we can update the weights of the neurons, propagating backward trough the network. When all the weights are updated, the network is now trained on a single point.

For a finale i would like to introduce Momentum, Stochastic Gradient Descent and Regularisation.
Momentum is a technique that is used to prevent the network from converging to a local minimum.
Momentum uses the previous gradient to calculate the next gradient. This makes it harder for the network to converge to a local minimum.
Though it can still happen, it is less likely.

Stochastic Gradient Descent is a technique that is used to update the weights of the neurons based on the error of the network.
Essentially we use it to minimize the error of the network, these work by gradually minimizing the error.

Now im going to talk about regularization.
Regularization is a technique that is used to prevent the network from overfitting.
This works by adding a penalty to the loss function, and thus preventing the network from overfitting.
More conceptually the this discourages the model from becoming too complex, thus preventing the network from overfitting.
## OLD
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


