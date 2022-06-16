- Probabilistic models (syntax and semantics)
- Inference in probabilistic graphical models
- Maximum likelihood learning
- The EM algorithm 

Hi im going to be talking about probabilistic graphical models. 

Firstly ill talk a bit about the uses for probabilistic graphical models. They are often used in the context of machine learning and statistical analysis.

There are certain advantages of using probabilistic graphical models these are:
- Principled quantification of prediction uncertainties.
- Robust and principled techniques to deal with incomplete.information, missing
data.
- Provides a general model of the domain that can in principle be used to answer
any inference query.
- Enables integration of domain knowledge.
- Transparent and explainable.

If the data is missing certain points it is possible to use the maximum likelihood estimator to fill in the missing data. Essentially MLL gives us the probability of a certain event happening. To do this we attempt to find the value that maximizes the likelihood. Maximum likelihood estimation is commonly used in statistical analysis, where it helps to find the best fit to the data.

However if we are missing a general parameter of the distribution we can not use the maximum likelihood estimator. Instead we have to utilize a iterative algorithm called the EM algorithm.

Now ill be talking a bit about the EM algorithm, it is closely related to Bayesian inference.
The EM algorithm is the expectation maximization algorithm. It is a method for learning the parameters of a probabilistic model. 
The EM algorithm generally works consists of the following steps:
I. Initialization of the parameters of the model.
II. Expectation step, where the model is estimated based on the data.
III. Maximization step, where the model is updated based on the estimated parameters.

The expectation step and the maximization step are then repeated until the model converges. The parameters of distribution are often the variance and mean of the distribution.

Correctness of the em-algorithm is important. The em-algorithm is not guaranteed to converge to the correct solution. It can only guarantee that it finds the local maximum. To account for this it is common to run the algorithm multiple times with different starting points and select the best solution.  
