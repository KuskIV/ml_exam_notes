-  Probabilistic models (syntax and semantics)
-  Inference in probabilistic graphical models
-  Maximum likelihood learning
-  The EM algorithm

I will be presenting Probabilisti models. A **probabilistic model** is typically learned from data using **statistical learning techniques**. They typically apply **Probabilistic inference** algorithms to use models for prediction or structure analysis. **Probabilitis inference** is the task of deriving the probability of one or more random variables taking a specific cvalue or set of values.


 Now a **Probabilistic Graphical Model**:
- supports a structured specification of high-dimensional distributions in terms of low-dimensional factors
- its structured representation can be exploited for efficient learning and inference algorithms (sometimes ...)
- its graphical representation gives a human-friendly design and description possibilities

Some Advantages of probabilistic methods:
- Principled quantification of prediction uncertainties
- Robust and principled techniques to deal with incomplete information, missing data. 
- Provides a general model of the domain that can in principle be used to answer any inference query.
- Enables integration of domain knowledge. 
- Transparent and explainable.

Now i'm going to talk about **parameter estimation**. 
First of all **Maximum Likelihood Estimation** is a meethod that determines values for the parameters of a model. The parameter valuies are found such that they maximise the likelihood that the process described by the model produced the data that were actually observed.

If we for example use Gaussian dsitribtuion which has 2 parameters. The mean and the standard deviation. Different values of these parameters result in diffrent models. Then **Maximum Likelihood Estimation** can be used to find the values that best fit the data. 

If we for example have some data where some element only does not occour, but the data is limimted. To avoid overfitting, initialize all tables with pseudo-counts (corresponding to virtual data). E.g. use a pseudo count of 1, then add the actual counts from data. Now normalize. This eliminates the drawback of having a count being 0 and then giving 0 probability.

Now the **Expectation-Maximization (EM) algorithm:** is a general algorithm for finding maximum likelihood estimates for a set of parameters $\theta$ when the data are incomplete. Imagine if we want to find cluster in a dataset, but we do not know where each datapoint came from. 
We start with a random guess for what the distribution or clusters are and the proceed to improve iteratively by alternating two steps:
1. **(Expectation)** Assign each data point to a cluster probabilistically. This is a hypothetical completionm of the data set obtained from the current estimate of the paramters.
2. **(Maximazation)** Update the parameters for each cluster based on the points in the cluster. i.e. apply maximum lielihood inference to completed data to obtain new estimate for parameters.