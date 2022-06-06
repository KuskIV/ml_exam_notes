---
title: 07 - Stochastic Gradient Descent and Regularization
created: '2022-06-04T10:04:14.821Z'
modified: '2022-06-06T08:08:48.173Z'
---

# 07 - Stochastic Gradient Descent and Regularization

This lecture continued on nerual networks. The focus will be on stochastic gradient descent and regularization (covered in #06), and consider convolutional networks and recurrent networks.

## Types of Optimization Algorithms

- First-order methos (like standard gradient descent): Relies on the gradient when optimizing the parameter

- Second-order methods (like Newtons method, too slow to be used): Takes the curvature into account

## Convolutional Neural Networks

Convlolutional neural networks (CNN) are used to process data in the form of multiple arrays, for example a color imange composed of three 2D arrays containing pixed intsensities in the three color channels. The architecture of a typical CNN is structued as a series of stages.

CNNs are composed of three types of layser:
- Convolution: Perform feature extraction
- Pooling: Perform feature extraction
- Fully connected: Maps extracted features into the final output

A typical architecture consists of repititions of a stack of several convolution layers and a pooling layer, followed by one or more fully connected layer.

### Convolution Layer

Is a fundamental component of the CNN, and performs feature extraction, consisting of a combination of linear and nonlinear operations.

A convolution is a specialized type of linear operation used for features extraction, where a small array of numers, called a kernel, is applied across the input. An element wise product bewteen each element of the kernel and the input is calculated at each location the kernel to obtain the output value in the corresponding position, called a feature map. As a kernel cannot have the center overlap the outermost elements, this will result in a recided height and width of the output feature map, which is why padding zeroes is usually done on the sides.

A kernel is usually $3 \times 3$, $5 \times 5$ or $7 \times 7$ and the distance between two successibe kernel is usually 1, and this is called the stride. A larger can be used in order to achieved downsampling of the feature maps. Another way to achieve downsampling is the pooling operation.

A key feature is weight sharing. Kernels are shared across all the imagese positiosn. This creates the following characteristics:
1. Letting the local feature patters extracted by kernels translations be invariant as kernels travel across all the image positions and detect local patterns
1. Learning spatial hierarchies of feature patters by downsampling in conjunction with a pooling operation, resulting in capturing an increasingly large field of view
1. Increasing model efficiency by reducing the number of parameters to learn in comparison with fully connected nerual network.

### Pooling Layer

A pooling layer provides a downsampling operation which reduces the dimensionality  of the feature maps. The parameters are similar to those in the convolution operations.

## Fully Connected Layer

The output feature maps of the final convolution or pooling layer is usually transformed into a one-dimensional array of numbers, and connected to one or more fully connected layers, also known as dense layers. Once the features extracted by the convolution layers are downsampled by the pooling layers, they are mapped by a suset of fully connected layers to the final outputs of the network. The final fully connected layer typically has the same number of nodes as the number of classes. Each fully connected layer is followe by a nonliear functino, such as ReLU, or softmax in the last layer.

## Recurrent Neural Networks

Recurrent neural networks (RNN) are best when it is used on sequential inputs, such as speech and language. They are a variant of the conventional feedforward artificial neural networks that can deal with sequential data and can be trained to hold the knowledge about the past.

They are adapted to work for time series data or data that involves sequenes, where ordinary networks are only meant for data points which are independent of each other. When we have data points in a sequence where each point depends on the previous point a modification to incorporate these dependenies are required. RNN have the concept of menory, that helps them store states of information of previous inputs to generate the next output. 

RNNs has a feedback loop, which can be unrolled $k$ times. At every step we can unfold the network for $k$ time steps to get the output at time step $k+1$. The unfolded network is very similar to the feedforward network.

### Training a Recurrent Neural Network

The backpropagation algorithm of an artificial network is modified to include the unfolding in time to train the weights of the network. In the pseudo code below, $h$ is the hidden sstatel, $k$ is a value set by the user and $p_t$ is the target value at time $t$:

```python
while stopping_condition_not_met():
  set_all_h_to_zero()
  for i in range(n-k):
    forward_propagate() # forward propagate the network over the unfolded network for k times to compute all h and y 
    e = y_t - p_t # compute the error
    back_propagate(e) # backpropagate the error across the unfolded network and update the weights
```

### Types of RNNs

There are different types of RNNs with varying architectures, some of these include:
- **One-to-one**: Here there is a single $(x_t, y_t)$ pair. Traditional NN employ a similar architecture
- **One-to-many**: A single input at $x_t$ can produce multiple outputs, e.g. $(y_{t0}, y_{t1}, y_{t2})$. This is used in music generation.
- **Many-to-one**: When many inputs from different timesteps produce a single output, $(x_t, x_{t+1}, x_{t+2})$ produce $y_t$. Such networks are employed in sentiment analysis, where the cclass label depends upon a sequence of words.
- **Many-to-many**: There are many exampels of this, for example when two inputs produce three outputs. These networks are used in translation, like english to french.

### Pros and cons

Pros:
- Ability to handle sequence data
- Ability to handle inputs of varying leghts
- Ability to sore historical information

Cons:
- Computation can be very slow
- The network does not take into account future inputs to make decisions
- Vanishing gradient problem, where the gradients used to compute the weight update may get very close to zero, preventing the network from learning new weights. The deeper the network, the more pronouced is this problem.

### Different RNN Architectures

There are different kinds of RNN:
- **Bidirectional Recurrent Neural Network (BRNN)**: Inputs from future time steps are used to improve the accuracy of the network. It is like having knowledge of the first and last wods of a sentence to predict the middle word.
- **Gated Recurrent Units (GRU)**: Designed to handle vanishing gradient problem. They have a reset and update gate to determine which information to be retained for future predictions
- **Long Short Term Memory (LSTM)**: Designed to handle vanishing gradient proble. They have input, output and forget gate to determine which information to retain






