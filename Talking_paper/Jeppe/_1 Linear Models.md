- Decision Regions
- Overfitting
- Least squares regression (corresponding to sklearn LinearRegression in self study 1)
- Linear discriminant analysis
- Logistic Regression

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
