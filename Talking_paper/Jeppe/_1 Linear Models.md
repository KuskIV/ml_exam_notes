- Decision Regions
- Overfitting
- Least squares regression (corresponding to sklearn LinearRegression in self study 1)
- Linear discriminant analysis
- Logistic Regression

## ORD
- logistic regression
- binary classification
- multiclass classification, decision boundary, decision regions
- 4 different models for classification
- One hot encoding
- results
## NEW

Hi im going to present a brief overview of linear models for classification and then talk a bit about the self study.

The most commonly used linear classification model is Logistic Regression. Normally logistic regression is used in binary classification problems.
An example of a non-linear classification model is k-nearest neighbors.

Though Linear models are mostly suited for binary classification problem they can be used in multiple class classification problems. This does however involves some extra concepts. For a linear function to be able to classify multiple different there are generally two different approaches to this these are one against all classification and one against one classification.

To do this involves something called a discriminant function which essentially is a function that defines the decision regions of the model. A decision region is a region in the space of the input space where the model is able to make a decision, these region each correspond to some class.

I will now present the self study.
For the self study the popular iris dataset is used. Initially we will only be using the 2 of the 4 features available in the dataset.
This is because there is no easy way to visualize 4d data in 2d.

We define 4 different models 3 linear and 1 non-linear. These are linear regression, logistic regression and linear support vector machine. as for the non linear we k-nearest neighbors.

We onehot encode the different classes.

Next we run some experiment to see how different values of K effect the accuracy of the k-nearest neighbors. From the experiment i can be observed that a higher K value results in a better accuracy. A K of 4 already results in a 100% accuracy and can thus not improve from larger values of K.

Here we can see some of the different decision boundaries of the different models. 

For KNN we see a somewhat horizontal line that splits the data into the different classes.

The linear regression model has a very different decision boundary. It seems that the model has split the data into the different classes, from the average position points and simply draw a line from there that best splits the data.

The logistic regression model and the linear support vector machine model have a very similar decision boundaries. Both are straight horizontal lines that separate the classes.

For the next exercise we tested the accuracies when making 70/30 split of the data. I will mostly focus on the confusion matrix and the accuracy. For the KNN model we can see that the accuracy is very high. From the confusion matrix we can see that model has slight troubles with class blue and green classes.

For linear regression we can see that the accuracy is very low. From the confusion matrix we can see that the model has trouble with class blue and green classes, but alos with the red class.


## OLD
4 min presentation

The popular iris dataset is a classic dataset for machine learning, were used.
For the self study we were presented with three different linear models these were:
- Linear regression
- Logistic regression
- SVC (Support Vector Classification)

The non-linear classifier KNN (K-Nearest Neighbors) was also used.
For each of these the decision boundary was plotted as to asses the differences between the models.

Now i would like to talk a bit about the decision boundary's or the decision regions and discriminant functions.
Essentials a discriminant function takes some input vector and outputs what class it belongs to.

A linear decision boundary is a function that divides the class with a hyperplane also called decision surface in this context.

Since linear discriminant functions are always for binary classification some problem is needed to be solved when during multiple classifications.

The naive approach to this will work by just having multiple linear discriminant functions. But these can results in some classifications becoming ambiguous and essentially meaning nothing.

But is do able if the different scenarios are accounted for.
there is the:
One against all*
One against one*

For the first exercise 

- KNN we see that the decision boundaries are somewhat horizontal lines through the space, which splits the classes into different decision regions. The above scatter plot also shows the same horizontal tendencies for the 2 considered features, so it is a good representation. Somethings else that can be seen is that KNN seems to become better with the value K.

- Lin. Reg. shows the three linear decision boundaries, which have no overlap in the decision regions, this will result in as we can see these intersecting hyperplanes, as each hyperplane only is fitted on the single class.
it seems not as good as KNN. It misclassifies a bunch of the blue points.

- Log. Reg. shows the three linear decision boundaries, each nicely dividing the data. Log reg is usually used for binary classification problem.

- SVC: generally looks a lot like the log reg. 

For the next exercise we do 70% 30% split, for the train and test set.
This is to compare the accuracy of the KNN and linear regression models.

From this we can see tha the KNN has an accuracy:
KNN Train accuracy 0.9428571428571428
KNN Test accuracy: 0.9333333333333333

and the linear regression has an accuracy:
Linear Regression Train accuracy 0.7904761904761904
Linear Regression Test accuracy: 0.6444444444444445

Here it is clear that the KNN is better than the linear regression.

We can see very clearly from the confusion matrix for linReg. on the test set it has some clear difficulties on class:1 (blue), where it classifies a significant portion as class:2 (green), we can scroll up and we can also see very clearly from the decision boundaries on the train set, why this is happening.

table of confusion matrix for logReg:
 [[ 9  0  0]
 [ 2  5 13]
 [ 0  1 15]]

 For the next exercise we ran the same experiment on all four features in the dataset the results were that both were generally better than with only two.
