---
title: 10 - Probabilistic Models
created: '2022-06-02T07:50:14.551Z'
modified: '2022-06-10T12:51:13.284Z'
---

# 10 - Probabilistic Models

## Probabilistic Programming

It is a tool for statistical modeling using the tools of computer science.

## Latent Variable Models

A latent variable is a hidden variable you cannot observe in the training or test data. They can be used for capturing complex or conceptual properties of a system that are difficult to quantify or measure directly.

Latent variable models assumes that complex observed data contains simpler, but unobserved patterns. The simplest version is a mixture model, which assumes that the data are clustered and that each datapoint is drawn from a distribution associated with its assigne cluster. The hidden variables of the model are the cluster assignments and the parameters to the per-cluster distributions. Given observed data, the mixture model posterior is a conditional distribution over cluserings and parameters. This conditional identifies a likely grouping of the data and the characteristics of each group.

A model consists of three types of variables:
- Observatinos: Datapoints
- Hidden variables: Encode hidden quantities
- Hyperparameter: Non-random quanitities

Latent variable models aim to model the probabilityy distribution with latent variables, where the latent variable will describe the data in a simpler way. Datapoints $x$ following a probability distriubtion $p(x)$, are mapped into latent variables $z$ that follow a distribution $p(z)$. 5 terms are relevant for this:
- **Prior distribution**, $p(z)$: Models the behaviour of the latent variables
- **Likelihood**, $p(x|y)$: Defines how to map latent variabese to the data points
- **Joint distribution**, $p(x,z)=p(x|z)p(z)$: Describe the model
- **Marginal distribution**, $p(x)$: The distribution of the original data
- **Posterior distribution**, $p(z|x)$: Describes the latent variagles that can be produced by a specific data point.

And two terms:
- **Generation**: The process of computing the data point $x$ from the latent variable $z$. We move from latent space into the acctual data distribution.
- **Inference**: The process of finding the latent variable $z$ from the data point $x$.

## Box's Loop

Building and using latent variable models is part of an iterative process for solving data analysis problems. First, formulate a simple model based on the kinds of hidden structure that you believe in the data. Then, given a data set, use an inference algorithm to approximate the posterior which points to the particular hidden patterns. Finally, use the posterior to test the model against the data, identifying the important ways that it succeeds and files. If satisfied, use the model to solve the program if not, revise the model according to the results of the critisism and repeat the cycle.

This is the Box's Loop. It is a method of understanding nature by iterative experimental design, data collection, model formulation and model critisism.

## Baysiean Regression

In bayesian regression, linear regression is formulated using probability distributions, where the response, $y$, is not estimated as a single value, but is assumed to be drawn from a probability distribution. The aim is not to find the single best value of the model parameter, but rather to determine the posterior distribution for the model parameters.

Not only is the response generated from a probability distribution, but the model parameters are assumed to come fomr a distribution as well. The posterior probability of the model parameter is conditional upon the training inputs and outputs:

$$P(\beta|y,x)=\frac{P(y|\beta,x)*P(\beta | x)}{P(y|x)}$$

where $P(\beta|y,x)$, is the posterior probability distribution of the model parameter given the inputs and outputs. This is based on Bayes Theorem:

$$\text{Posterior}=\frac{\text{Likelihood}*\text{Prior}}{\text{Normalization}}$$

From this, two benefits can be observed:

- **Priors**: If we have domain knowledge, or a guess for what the model parameters should be, we can include them in our model and if not, we can use non-informative priors.
- **Posterior**: The results of performing Bayesian linear regression is a distribution of possible model parameters based on the data and the prior. This allows us to quantify our uncertainty about the model, if we have few data points, the posterior distribution will be spead out.

The formulation of model parameters as distributions encapsulates the Bayesian wordview: we start out with an initial esstimate, our prior, and as we gather more evidence, our model becomes less wrong.

The advantage is that we can model the uncertainty.


