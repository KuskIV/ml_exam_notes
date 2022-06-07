---
title: 08 - Probabilistic Graphical Models
created: '2022-06-02T07:48:49.189Z'
modified: '2022-06-04T10:04:10.764Z'
---

# 08 - Probabilistic Graphical Models
This lecture looks at probabilistic graphical models and the underlying learning principles. First a recap of bayesian network models. Thereafter methods for learning the parameters of probabilistic models from data.

Probabilistic Graphical Models:
- support a structured specification of high-dimensional distributions in terms of low-dimensional factors
- structured representation can be exploited for efficient learning and inference algorithms (sometimes ...)
- graphical representation gives human-friendly design and description possibilities

Advantages of probabilistic/statistical methods:
- Principled quantification of prediction uncertainties
- Robust and principled techniques to deal with incomplete information, missing data. 
- Provides a general model of the domain that can in principle be used to answer any inference query.
- Enables integration of domain knowledge. 
- Transparent and explainable.

## Bayesian Networks

### Bayes Theorem
 $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
 where: 
 - $P(A | B) is the probability of A given B (posterior).
 - $P(B | A) is the probability of B given A (likelihood).
 - $P(A) is the probability of A (prior).
 - P(B) is the probability of B (evidence).

Definition: A bayesian network consists of the following:
- A set of variables and a set of directed edged between variables.
- Each variable has a finite set of mutually exclusive states.
- The variables together with the direct edges form an acyclic directed graph

Bayesian networks use Bayesian inference for probability computations. They model conditional dependence and therefore causation by representing conditional dependence by edges in a directed graph.

![alt text]( \../attachments/bayesianex.png "Title")

With given probabilities for each variable i.e. P(A) = (.92, .08)

## Parameter Estimation
Now we have a Bayesian network model, but no conditional probabilities. We can instead use a database with vales for the variables to estimate the conditional probabilities.

### Maximum Likelihood Estimation
Thumbtack example. Thumbtack thrown 100 times, landed pin up 80 times.
Probability $\theta$ of pin up:

$p(data| \theta )$ 
$= p(pin up, pin down,..., pin up| \theta )$
                 
 $= p(pin up| \theta )*p(pin down| \theta )*...*p(pin up| \theta )$

The parameter $\hat{\theta}$ that maximizes the likelihood is chosen if we have to select from different models.

$\hat{\theta} = 0.8$

To find the maximum likelihood estimate for parameters in a Bayesian network model. We find the maximum likelihood estimates for each conditional probability distribution in the model.

In general with complete data you get a maximum likelihood estimate as the fraction of counts over the total number of counts.

### Parameter overfitting
To avoid overfitting, initialize all tables with pseudo-counts (corresponding to virtual data). E.g. use a pseudo count of 1, then add the actual counts from data. Now normalize. This eliminates the drawback of having a count being 0 and then giving 0 probability.

## Incomplete data
Marginal likelihood: identify probability of incomplete sample $Y_i$ with marginal probability of observed variables.

Can be used if data are missing at random instead of standard likelihood.

### Expectation-Maximization (EM) algorithm:
General algorithm for finding maximum likeihood estimates for a set of parameters $\theta$ when the data are incomplete.
- Use hypothetical completions of data sets obtained from current estimate for $\theta$.
- Apply maximum likelihood inference to completed data to obtain new estimate for $\theta$.

Example:

![alt text]( \../attachments/EMexam.png "Title")

In the case of a complete dataset, to find the distribution of P(Pr = yes) we would use the following:
$P(Pr = yes) = \frac{N(Pr = yes)}{N}$

Instead with incomplete data:
We assign a probability distribution usually with random distribution, but in this case (0.5, 0.5)
Now we calculate the expected value for $N(Pr = yes)$

$\mathbb{E}[N(Pr = y)]= P_0(Pr = y | Bt = uT = pos) + 1 + 1 + 1 + P_0(Pr = y | Bt = neg) \\ = 0.5 + 1 + 1 + 1 + 0.5 = 4$

$\mathbb{E}[N(Pr = n)]= P_0(Pr = n | Bt = uT = pos) + 0 + 0 + 0 + P_0(Pr = n | Bt = neg)\\= 0.5 + 0 + 0 + 0 + 0.5 = 1$

or

$\mathbb{E}[N(Pr = n)]= \sum^{N}_{i=1} P_0 (Pr = yes | d_i)$

We get

$\hat{P_1}(Pr = yes) = \frac{\mathbb{E}[N(Pr = yes)]}{N} = \frac{4}{5} = 0.8$

Now we calculate:

$\mathbb{E}[N[Ut = pos, Pr = yes]] = P(Ut = pos, Pr = yes | Bt = pos, Ut = pos) + 1 + P(Ut = pos, Pr = yes | Bt = pos, Pr = yes) + 0 + P(Ut = pos, Pr = yes | Bt = neg) \\ = 0.5 + 1 + 0.5. + 0 + 0.25 = 2.25$

This can be used to calculate:

$P_1(Ut = pos | Pr = yes) = \frac{\mathbb{E}[N(Ut = pos, Pr = yes)]}{\mathbb{E}[N(Pr = yes)]} = \frac{2.25}{4} = 0.5625$

Now the procedure starts over, but with the new probability estimates. This continues until the probabilities no longer change.

EM converges to a local maximum. To avoid sub-optimal maxima: run EM several times with different starting points.


### Bayesian Estimation
Maximum likelihood estimation has drawback when considering spare data. With limited data some cases can show up 0 times and as such be given zero probability. Which cannot always be assumed.

Bayesian estimation is an alternative to maximum likelihood.
In Bayesian estimation you start with a prior distribution and then update the distribution as examples are observed.

Basis:
- Parameters are modeled as random variables and information about them can be included prior to observing data
- By Bayes’ rule, the prior information is combined with the likelihood, yielding a posterior distribution that is used for making inferences about the parameter

The equation for Bayesian estimation looks similar to that of Bayes theorem.

$p(\theta | D) = \frac{p(\theta, D)} {p(D)} = \frac{p(\theta) p(D|\theta)}{p(D)}$

where
- D = all observed data
- $p(\theta)$ is the prior distribution