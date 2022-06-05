---
title: 07 - Stochastic Gradient Descent and Regularization
created: '2022-06-04T10:04:14.821Z'
modified: '2022-06-05T12:29:16.178Z'
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








