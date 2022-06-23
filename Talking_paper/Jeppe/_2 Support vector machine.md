- Maximum margin hypeplanes
- Feature transformations and kernel functions
- The kernel trick
- String kernels

## ORD
- Support vector machine.
- Maximum margin hyperplanes.
- Non-linearly separable data, feature transformations.
- Kernel functions, kernel trick, Computationally expensive functions.
- MNIST dataset, 3 and 7.
- Varying kernel functions.
- Customized kernel functions.
## NEW

Hi i will be talking about support vector machines. Support vector machines are a class of machine learning algorithms that are used to classify data. They are mostly used in binary classification problems, like most other linear classifiers. Essential what a support vector does is try to find what is called the Maximum margin hyperplane. 

The Maximum margin hyperplane is a hyperplane that separates the data into two classes.
The intuition behind this is that the larger margin the hyperplane can have between to two different classes the more accurate the model is. So essetialy when deciding the best line to make we simply need to maximize the distance to each class.

But what if the data is not linearly separable?
This is were feature transformations and kernel functions come in.
Feature transformation essential adds another dimension to the dataset, making it a higher dimensional dataset. 
This is done using a function that is convenient for the use case to make the data linearly separable.
When we make this transformation we call it mapping the data into the features space.

When the data has been mapped and becomes linearly separable we can simply set the maximum margin hyperplane to the best line that separates the data.

But actually calculating the convenient function to make the data linearly separable is a bit tricky and can be very computationally expensive, because the more features are involved the larger degree of polynomial function are required to separate the data the more expensive it becomes. Essentially the kernel measures the similarity between the data and the data. This is where the kernel trick comes in, which makes it possible to do this without transforming the data. This is done using the dot product of the data.

Now i will talk a bit about the self studies.
For this self study we used the MNIST dataset, which consists 70000 28x28 images of handwritten digits from 0 to 9.
To make the exercises simpler and faster we only use two classes, 7 and 3.
For the first exercise we split the data up into training and test data.

The we learn different support vector machines, where we vary the kernel function used.
The kernel function are linear, polynomial, Gaussian function and sigmoid.
From the experiment each of the kernel function perform similarly, but the best performing one is the polynomial kernel and rbf. The only differences between these two is the time, where rbf was marginally slower.

For the second exercise we manually made several different convocational kernels. I will now try to explain the idea behind the functions we made.
The first one is simply a 3 by 3 matrix of ones.
The second one is a 3 by 3 matrix of diagonal ones and zeros else where.
The third one is a 3 by 3 matrix of diagonal ones and zeros else where except in the other direction.
The fourth one is a 3 by 3 matrix of vertical line in the middle of the matrix.
The fifth one is a 3 by 3 matrix of horizontal line in the middle of the matrix.
The last two are simply random matrices.

The idea for most these is that we want to extract some features about the matrix that represent number.

The next part is just functions that use them to create the feature map.
The results are a bit worse than before, but only sightly worse.

## OLD

For this self study we used the MNIST dataset, which consists 70000 28x28 images of handwritten digits from 0 to 9.

In the exercise we utilized SVM (Support Vector Machine) to classify the digits. The object of a SVM is to find a separating hyperplane that separates the data into two classes. When separating data with a svm we want to find the line with the widest margin between the two classes. 

In the first exercise we split the dataset into a training set and a test set. We then tested the SVM with different kernel function and observed the differences.

Sometimes it is not possible to separate data in linear space, but this data can be transformed into a linearly separable feature space. The main tool to do this is the kernel function.

for the first exercise we experimented with the kernel functions:
- linear kernel 
- polynomial kernel
- Gaussian kernel
- Tanh/Sigmoid kernel

From the experiment each of the kernel function perform similarly, but the best performing one is the polynomial kernel and rbf. The only differences between these two is the time, where rbf was marginally slower.

When it is not possible to separate data in a low dimensionality, additional dimensions are added. This enables us to separate the data linearly, but when operations are performed with higher dimensions, this can lead to extremely high and impractical computation costs, especially if many dimensions are added.

This is what the kernel trick solves. The trick is that kernel methods represents the data only through a set of pairwise similarity comparisons between the original data in the low dimensionality, instead of applying the transformation, and representing the data in a higher dimensional feature space.

The benefit is that the objective function we are optimizing to fit the higher dimensional decision boundary only includes the dot product of the transformed vectors. Therefore we can just substitute these dot product terms with the kernel function without using $\phi(x)$, meaning we find the optimal hyperplane using the hither dimensional space, without having to calculate or in reality eve know anything about $\phi(x)$.