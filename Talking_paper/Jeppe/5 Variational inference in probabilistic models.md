-   Probabilistic models and plate notation
-   Variational inference basics (objective function, Evidence lower bound, mean field assumption)   
-   Black-box variational inference
-   Variational inference and probabilistic programming

Hi im going to be talking about variational inference specifically i will focus on variational inference basics. 

For the variational inference basics i will first be talking about what variational inference is.

Variational inference is a method for approximating  distributions. The main idea of variational inference is essentially to cast inference as a optimization problem as a minimization problem. Variational inference has some main differences from sampling based inference such as Gibbs sampling.
- Almost never find the globally optimal solution
- We know when they converge
- Usually they scale better than sampling
To summarize then variational inference is used to compute the posterior distribution of a model.

Now i will talk about what an objective function is.
A objective function is in machine learning a function the you would like to maximize or minimize. I machine learning this is the function that is used to optimize the model. Essentially the objective function is the cost function.

Now ill talk about the evidence lower bound. To do this i think is important to understand what evidence means in the this context. Essentially the evidence are the likelihood of the data given the model. Thus the evidence lower bound is simply the lower bound of the evidence. This is useful because it is a way to estimate the quality of the model, since a higher evidence may indicate that we have chosen the right model. Essentially we want to maximize the evidence lower bound, which indigently means minimizing the KL divergence. Because of this we can say than we try to maximize the log likelihood and minimize the distance to the prior.

Quickly i will explain why we want to minimize KL-divergence it is because KL-divergence is a measure of how much to distribution from each other.

The mean field assumption is a assumption that we do about the variational distribution.

Now that i have given an overview of variational inference i will talk the self study.
In the self study we used bayesian linear regression.
In doing this i will attempt to explain how it works and the process of doing it.

In bayesian linear regression we try to find the best posterior distribution of the parameters of the model.
In this cell we initialize the prior distributions.


