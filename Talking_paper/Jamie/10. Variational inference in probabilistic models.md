- Probabilistic models and plate notation
- Variational inference basics (objective function, Evidence lower bound, mean field assumption)   
- Black-box variational inference
- Variational inference and probabilistic programming


I will be presenting Probabilisti models. A **probabilistic model** is typically learned from data using **statistical learning techniques**. They typically apply **Probabilistic inference** algorithms to use models for prediction or structure analysis. **Probabilitis inference** is the task of deriving the probability of one or more random variables taking a specific cvalue or set of values.

In **Bayesian inference** **plate notation** is a method of representing variables that reapeat in a graphical model. Instead of drawing each repreated variable individually, a plate or rectangle is used to group variables into a subngraph that repeat togheter and number is drawn on the plate to represent the number of repititions of the subgraph in the plate.

Now I will talk about **Variational inference**. The main idea of variational methods is to cast inference as an optimization problem.

**The KL-divergence (Kullback-Leibler divergence)** is a way of measuring the matching between two distributions. By minizimizing the KL-divergence over a set of parameters we can find a distribtuion that is similar to the data distribution.

Maximizing the **Evidence lower bound (ELBO)** is equivalent to minimizing the KL divergence.  ELBO consist of two terms the reconstruction term and the penalty term. The **reconstruction term** is the expected log-likelihood measuring how well some samples exaplins the data. The **Penalty term** penalizes large deviations between the sample and prior. 

Antoher term is the **Mean field assumption** That is, we assume that each weight in the neural network is independent of all the others.

**Variational inference** transforms the problem of approximating a conditional distribution into an optimization problem.

Maximizing the **ELBO** is equivalent to minimizing the** KL divergence**.

In **black box variation** they instead use **stochastic optimization** to maximize the **ELBO**. In **stochastic optimization**, we maximize a function using noisy estimates of its gradient

- The goal is to obtain efficient inference in unconstrained Bayesian network models any structure, any combination of distributional families
- Black-Box Variational Inference promises VB inference in any model, but at the cost that inference relies on sampling – and it sometimes shows poor converge properties in practice.