- Maximum margin hypeplanes
- Feature transformations and kernel functions
- The kernel trick
- String kernels

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