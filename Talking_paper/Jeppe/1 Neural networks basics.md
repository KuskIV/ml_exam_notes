- Neural network basics
- Loss functions
- Learning neural networks (gradient decent and stochastic gradient descent)
- Neural network structures

## NEW
Hi im going to be talking about neural networks basics.
A neural net work consists of a set of neurons, and the connections between the neurons.
Each neuron is connected to other neurons, and the connections are made by the weights.
The basic computation of a neural networks forward pass is to take the input, apply the weights, activation function, and then pass the output to the next layer.
This is the done throughout the network, until the output is reached, where the error is calculated and the weights are updated with back propagation.
There are three types of basic layers in a neural network each consisting of multiple neuron and connections.
These are the input layer, the hidden layer, and the output layer.

Now i will just be talking about some of the term in skipped over in the very high level explanation.

Activation functions are applied to the output of each neurons. 
These function essentially dictate how the output of the neurons is calculated, and based on what function is used, the output have different constraints.
Many activation function are non-linear and are used to constrain the output of the neurons to a known range.
Some common activation functions are:
- Sigmoid function: Sigmoid essentially maps the output of the neurons to a range between 0 and 1.
- ReLU function: ReLU is a function that is used to constrain the output of the neurons to a known range.
- Tanh function: Tanh maps the output of the neurons to a range between -1 and 1.

When we reach the output layer, we come to the loss function or error function.
Essentially, the loss function is used to calculate the error of the network, aka how wrong we are.
There are many different loss functions, each suited to a different problem. Some of the most common ones are:
- mean squared error: It takes the difference between the output and the expected output and squares it.
- Logistic loss: Works similarly to the mean squared error, but instead of squaring it, it takes the log of the output.
- Cross entropy: Works by taking the log of the output, and then taking the sum of the outputs of the different classes. Here, the output is a probability, and the classes are the different possible outputs.

The loss function is essentially what we want to minimize to achieve a good model.
Using the error we can update the weights of the neurons with the gradient of the loss function.
We want to make the loss function converge this is done by using the gradient descent algorithm and involves a learning rate.
<!-- 
The idea of the gradient descent algorithm is to keep updating the weights of the neurons until the loss function converges, but each update is done by taking the gradient of the loss function with respect to the weights. Idealy this becomes smaller and smaller the closer we get to the minimum. -->

Now i will talk a bit about how back propagation works.
Back propagation is the process of updating the weights of the neurons based on the error of the network.
To perform back propagation, we need to introduce a new concept of chain rule.
The chain rule essentially calculates the gradient of the loss function with respect to the weights of the neurons. 
Using this we can update the weights of the neurons, propagating backward trough the network. When all the weights are updated, the network is now trained on a single point.

We then continue to update the weights of the neurons until the loss function converges.

I mentioned minimum earlier but there are different kinds of minimums.
There are global minimums, and local minimums.
We cannot guarantee that we will find the global minimum, but we can guarantee that we will find the local minimum.
This is true even when the model has converged.

This leads us to the idea of momentum.
Momentum is a technique that is used to prevent the network from converging to a local minimum.
Momentum uses the previous gradient to calculate the next gradient. This makes it harder for the network to converge to a local minimum.
Though it can still happen, it is less likely.



## OLD
Hi im going to talk about the basics of a neural network.
The basic structure of a neural network contains the input layer and the output layer. In between these layers are the hidden layers and the activation functions.

The activation functions defines how the weighted sum of the input is transformed into an output from a node or nodes in a layer of the network.

When training the network it is important to understand the what error functions are used. The lose function calculates the difference between the output of the network and the desired output. This produces the loss which is used to update the weights of the network during back propagation.

When the network is actually learning it is important to understand the proceed of learning there are gradient descent and stochastic gradient descent methods. 

gradient means the slope of the loss function as the weights are updated. Since the lose should ideally be as low as possible we want to minimize this.

Different approaches exists to determine how much change there should be in the weights. This is what gradient descent is. Gradient descent work by calculating the gradient/derivative and then going in the opposite direction. This is essentially repeated until the model converges. 

A problem with gradient descent is that it can become very computationally expensive, with larger data sets.

Stochastic gradient descent is an extension of the gradient decent algorithm. Stochastic gradient descent work by having something called a mini batch. This is essentially a sample of the data that is draw uniformly from the data.

For the self study we experiment with different variations of gradient descent.

We found that the batch size seems to have little effect, but that larger generally leads to better results.
for the learning rate we found the best to be 0.02 a good balance between speed and accuracy.

The next exercise we then implement momentum.
Instead of depending only on the current gradient to update the weight, gradient descent with momentum replaces the current gradient with m (“momentum”), which is an aggregate of gradients. This aggregate is the exponential moving average of current and past gradients.

Here we find that the momentum seems to not have much effect on the results.
