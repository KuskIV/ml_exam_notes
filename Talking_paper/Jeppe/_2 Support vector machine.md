- Maximum margin hypeplanes
- Feature transformations and kernel functions
- The kernel trick
- String kernels

For this self study we used the MNIST dataset, which consists 70000 28x28 images of handwritten digits from 0 to 9.

Sometimes it is not possible to separate data in linear space, but this data can be transformed into a linearly separable feature space. The main tool to do this is the kernel function.

In the exercise we utilized SVM (Support Vector Machine) to classify the digits. The object of a SVM is to find a separating hyperplane that separates the data into two classes. When separating data with a svm we want to find the line with the widest margin between the two classes.

In the first exercise we split the dataset into a training set and a test set. We then tested the SVM with different kernel function and observed the differences.

From the experiment each of the kernel function perform similarly, but the best performing one is the RBF polynomial kernel and rbf. The only differences between these two is the time where rbf was marginally slower.