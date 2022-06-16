- The basis for learning neural networks (loss functions and gradient decent)
- Learning and back propagation (computational graphs, the chain rule)
- Learning in practice (stochastic gradient descent, momentum, regularisation)


The structure of a neural network is a number of input layers, all connected to some number of hidden layers, which are finally connected to the output layers. The connection between the layers have weights, which are learned during the training.

When the network is learning an imporant factor is the **loss function** or **error function** which quantifies the difference between the expected outcomt and the outcome produced by the model. The loss is used to update the weights. One example is **Mean sqaured error**, where 0 means the model is perfect. Other examples are log-loss or cross entropy loss.

Usually when learning a **gradient-based algorithm** is used to minimize the cost function. To do this two steps are performed iteratively.
1. Compute the gradient, that is the first-order derivative of the function at the current point.
2. Move in the oppoiste direction of the slope increase from the current point by the computed amount.

This is what gradient descent is. The idea is to pass the training set through the hidden layers of the neural netowrk and then update the parameters of the layers by computing the gradients using the training samples from the data.

Now we introduce minibathces. A mini batch means that we only take a subset of the data in one iteration. If the batch size is 1 so we only look at one traing example in each iteration it is called **Stochastic Gradient Descent**. If we instead have a match
 size of e.g. 32 the it is reffered to as **mini-batch gradient descent.**

The learning rate is a positive scalar determining the size of the step.  Which usually decreases over time to ensure convergence.

The method of momentum is designed to accelerate learning, specially in the face of high curvature, small but consistent gradients or noisy gradients. The algorithm accumalates an exponentially decaying moving average of past gradients and continues to move in their direction.


As more layers using certain **actiation functions** (e.g. sigmoid) are added to neural networks, the gradients of the **loss function** approaches zero, making it hard to learn. This is called **Vanishing Gradients**. In the case for sigmoid, the issue is that the output space is between 0 and 1. The issue is a large change in the input space for the sigmoid function will cause a small change in the output. Hence, the derivative becomes small.
A solution is to use ReLU, which does not have small derivatives. An issue with ReLU is a dying ReLU problem, where many neurons only output 0. This is solved by Leaky ReLU has a small slope for negative values instead of a flat slope.

**The chain rule** is used to compute the derivatives of functions formed by composing other functions whose derivaties are known, and is used by back-propagation. It tells us how to differentiate composit functions.

Finally **Forward propagation** is when the network accepts an input $x$, which flows through the network to produce and output $\hat{y}$. During training forward propagation con cintinue onward until it produces a scalar loss, which flows back trough the network in order to compute the gradient, and this is back propagation.