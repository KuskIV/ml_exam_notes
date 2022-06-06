---
title: 08 - Probabilistic Graphical Models
created: '2022-06-02T07:48:49.189Z'
modified: '2022-06-04T10:04:10.764Z'
---

# 08 - Probabilistic Graphical Models
This lecture looks at probabilistic graphical models and the underlying learning principles. First a recap of bayesian network models. Thereafter methods for learning the parameters of probabilistic models from data.

## Bayesian Networks
Definition: A bayesian network consists of the following:
- A set of variables and a set of directed edged between variables.
- Each variable has a finite set of mutually exclusive states.
- The variables together with the direct edges form an acyclic directed graph

Bayesian networks use Bayesian inference for probability computations. They model conditional dependence and therefore causation by representing conditional dependence by edges in a directed graph.

## Parameter Estimation

