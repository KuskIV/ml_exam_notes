-   Probabilistic models and plate notation
-   Variational inference basics (objective function, Evidence lower bound, mean field assumption)   
-   Black-box variational inference
-   Variational inference and probabilistic programming

Hi im going to be talking about variational inference specifically i will focus on variational inference basics and black-box variational inference. 

For the variational inference basics i will first be talking about what variational inference is.

Variational inference is a method for approximating  distributions. The main idea of variational inference is essentially to cast inference as a optimization problem as a minimization problem. Variational inference has some main differences from sampling based inference such as Gibbs sampling.
- Almost never find the globally optimal solution
- We know when they converge
- Usually they scale better than sampling

Now i will talk about what an objective function is.
A objective function is in machine learning a function the you would like to maximize or minimize. I machine learning this is the function that is used to optimize the model. Essentially the objective function is the cost function.

Now ill talk about the evidence lower bound. To do this i think is important to understand what evidence means in the this context. Essentially the evidence are the likelihood of the data given the model. Thus the evidence lower bound is simply the lower bound of the evidence. This is useful because it is a way to estimate the quality of the model, since a higher evidence may indicate that we have chosen the right model. 