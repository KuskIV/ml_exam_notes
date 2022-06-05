---
title: 05 - Markow Networks
created: '2022-06-02T07:47:46.574Z'
modified: '2022-06-04T10:02:01.927Z'
---

# 05 - Markow Networks

In this lecture the focus will be on the topic of node classification in networks, with a focus on progabilistic classification using Markov Networks.

## Inductive vs Transductive

__Transductive__: The graph is fixed and the is the same when learning and predicting. All nodes needed to be lassified are already known when learning the classifier.

__Inductive__: The graph used for training, can be differen. Nodes that are classified can be new nodes added to the graph, or even be nodes in a different graph.

## Homophily

Homophily is when a link between individuals (such as friendship or other social connection) is correlated with those individuals being similar in nature. For example, friends often tend to be similar in characteristics like age, social background and education level.

## Independent classification:
__Generic approach__
- Define a set of **node features** $X_1 \dotsb X_K$
- For each node $v \in V_I$, constrict the training example
$$ (X(v), Y(v))=(X_1(v), \cdots X_K(v), Y(v))$$
- Use standard machine learning approach to learn a classifier from the examples
- For nodes $u \in V_u$: calculate feature vector $X(u)$, and predict $Y(u)$

__Node features construction:__
- $X(v) = A(v)$, with $A$ a node attribute.
- $X(v) = d(v)$
- $X(v) = aggr{A(u) | u:(v,u) \in E}$: aggregate of attribute values of linked nodes.
- $X(v)$ Boolean function for a property of graph neighborhood.
- $X(v) = PageRank(v)$

## Label propagation
Label Propagation Algorithm (LPA) is an iterative algorithm where we assign labels to unlabelled points by propagating labels through the dataset.
__Characteristics__
- No node features
- Transductive classification exploiting homophily
- For unlabeled nodes compute probability distribution over class labels




