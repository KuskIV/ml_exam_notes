-   Probabilistic models and plate notation
-   Variational inference basics (objective function, Evidence lower bound, mean field assumption)   
-   Black-box variational inference
-   Variational inference and probabilistic programming

Hi im going to be talking about variational inference specifically i will focus on variational inference basics. 

For the variational inference basics i will first be talking about what variational inference is.

Variational inference is a method for approximating  distributions. The main idea of variational inference is essentially to cast inference as a optimization problem as a minimization problem. Variational inference has some main differences from sampling based inference such as Gibbs sampling.

These have the following differences:
- Almost never find the globally optimal solution
- We know when they converge
- Usually they scale better than sampling
To summarize then variational inference is used to compute the posterior distribution of a model.

Now i will talk about what an objective function is.
A objective function is in machine learning a function the you would like to maximize or minimize. I machine learning this is the function that is used to optimize the model.

Now ill talk about the evidence lower bound. To do this i think is important to understand what evidence means in the this context. Essentially the evidence are the likelihood of the data given the model. Thus the evidence lower bound is simply the lower bound of the evidence. This is useful because it is a way to estimate the quality of the model, since a higher evidence may indicate that we have chosen the right model. Essentially we want to maximize the evidence lower bound, which indigently means minimizing the KL divergence. Because of this we can say than we try to maximize the log likelihood and minimize the distance to the prior.

Quickly i will explain why we want to minimize KL-divergence it is because KL-divergence is a measure of how much to distribution from each other.

Now that i have given an overview of variational inference i will talk the self study.
In the self study we used bayesian linear regression.
In doing this i will attempt to explain how it works and the process of doing it.

In bayesian linear regression we try to find the best posterior distribution of the parameters of the model.
In this cell we initialize the prior distributions in the next cell we specify the variational distribution.

Now we use these to actually learn the model.
Firstly we generate some data for the model.
then we initializes a instance of evidence lower bound.
These are then used to initialize the model.
now we simply take steps by using the generated data and prints some evaluation metrics out during learning.
When the training is done we plot the result. Where we have the original data and the learned distribution.

In the experiment we did the learning again but this time making subtle changes to the parameters used to observe the effect.
For the first set of experiments we changed the number of samples in the data and the precision of the sensor.

More samples seems to generally benefit the model. 
A low sensor quality resulted in a higher error in the model. But doubling the sensor quality did not double the the performance of the model.
Thus there is a non-linear relationship between the performance and the sensor quality.

For the next experiment we tried to change the learning rate and the confidence in the prior.
Learning rate seems to not really effect the result much in this case.

Moving the prior away from the true model also seemed to have little effect on the model.

finally increasing the confidence in the wrong guide seems to have a little effect on the model.

for the final experiment we tried to change confidence in the prior and change the prior distribution.

Increasing confidence in prior seems to be detrimental to the model,
but changing the prior distribution seems to have little actual effect.



https://towardsdatascience.com/introduction-to-bayesian-linear-regression-e66e60791ea7