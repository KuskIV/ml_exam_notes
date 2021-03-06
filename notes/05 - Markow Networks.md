---
title: 05 - Markow Networks
created: '2022-06-02T07:47:46.574Z'
modified: '2022-06-07T11:16:09.953Z'
---

## Keywords
- Markov chain: Markov chains are a fairly common, and relatively simple, way to statistically model random processes. 
- Clique: Clique in an undirected graph is a subgraph that is complete.
- Complete graph: A complete graph is a graph in which all nodes are connected to all other nodes.
- Homophily: When link correlates with similarity of objects
- Transductive: Transductive learning is a method of learning from data that is not necessarily labeled.
- Inductive: Inductive learning is a method of learning from labeled data.
- Label propagation
- Gibbs sampling
- Markov Random Field/Markov Network: A Markov Random Field is a graph whose nodes model random variables, and whose edges model desired local influences among pairs of them.
# 05 - Markow Networks

In this lecture the focus will be on the topic of node classification in networks, with a focus on probabilistic classification using Markov Networks.

## Inductive vs Transductive

__Transductive__: The graph is fixed and the is the same when learning and predicting. All nodes needed to be classified are already known when learning the classifier.

__Inductive__: The graph used for training, can be different. Nodes that are classified can be new nodes added to the graph, or even be nodes in a different graph.

## Homophily

Homophily is when a link between individuals (such as friendship or other social connection) is correlated with those individuals being similar in nature. For example, friends often tend to be similar in characteristics like age, social background and education level.

## Independent classification:
__Generic approach__
- Define a set of **node features** $X_1 \dotsb X_K$
- For each node $v \in V_I$, constrict the training example
$$(X(v), Y(v))=(X_1(v), \cdots X_K(v), Y(v))$$
- Use standard machine learning approach to learn a classifier from the examples
- For nodes $u \in V_u$: calculate feature vector $X(u)$, and predict $Y(u)$

__Node features construction:__
- $X(v) = A(v)$, with $A$ a node attribute.
- $X(v) = d(v)$
- $X(v) = aggr{A(u) | u:(v,u) \in E}$: aggregate of attribute values of linked nodes.
- $X(v)$ Boolean function for a property of graph neighborhood.
- $X(v) = PageRank(v)$

## Label propagation
Label Propagation Algorithm (LPA) semi-supervised is an iterative algorithm where we assign labels to unlabelled points by propagating labels through the dataset.
__Characteristics__
- No node features
- Transduction classification exploiting homophily
- For unlabeled nodes compute probability distribution over class labels

Within community networks, the label propagation algorithm aims the change the label of each node based on the communities label. The biggest advantage for label propagation is it excellent runtime. 

__Principles of label propagation__
1. Each of the distinct nodes has it's corresponding label
2. The corresponding label of each node denotes the distinct community that this node belongs to
3. Through iteration within the network, each node will update its belongingness community based on belongingness community of neighbor nodes until all of the nodes with the same label are attributed to same communities.
4. The updated community of each node will be the corresponding belongingness community of the maximum number of nodes
5. Eventually, densely connected nodes reach a common label community

Label propagation works on the relatively simple assumption that closely connected nodes also have the same class aka label. The effect of this assumption is that it is possible to propagate the label to unlabeled nodes in the network.

The algorithm works by performing a radom walk foreach of the unlabeled nodes. This is done to determine the probability distribution of reaching a node with a label.
This is then done multiple times until the probabilities stop changing in the unlabled nodes. Unlabeled nodes are then assigned a label based on the probability distribution.


## Markov Networks
Markov Networks are a generalization of the Markov chain.
Directed models(Bayesian Networks): good for causal dependencies
Undirected models(Markov Networks): good for mutual non-causal dependencies.
__Notation__
For a variable X: Val(X) is the set of possible values for X.
- $Val(X) = \real$(Numeric variable)
- $Val(X) = {true, false}$ (Boolean)
- $Val(X) = {a, b, c, d}$ (Categorical)

__Markov Network__
Let $X_1 \cdots X_n$ be random variables. A markov network $N$ for $X_1 \cdots X_n$ consists of:
- an undirected graph $G$ whose nodes are the variables $X_1 \cdots X_n$
- a set of clique potentials
$$\phi_iVal(Y_i)\rightarrow \real^+    (i=1, \cdots ,K)$$
Where the variable $Y_i \subseteq X$ form a fully connected subgraph (clique) in $G$

## Gibbs Sampling
Problem: compute a marginal probability $P_N(X=x)$.

(approximate) solution: generate a sequence of samples: $X_1,X_2, \cdots X_N$
So that the frequencies in the sample (approximate) match the marginal probability.

The idea behind Gibbs sampling is to obtain new samples from previous sample by randomly changing the value of the only one selected variable.

Computing the conditional probabilities in the sampling is done like this:
$$P_N(X_K = x_K | X_{K} = x_{k}^{t-1}) = \frac{P_N(X_{t-1}^{k})}{P_N(x_{t-1}^{k})}$$

$$\frac{1/Z \prod_i \phi_i (x_{t-1}^{k}),x_k}{1/Z \sum_{x_{K}^{'}} \prod_i \phi_i (X_{k}^{t-1}, x_{k}^{'})}$$

where the sum $\sum_{x_{K}^{'}}$ is over all possible values $X_{k}^{'}$ of $X_k$

Gibbs from samples to estimates:
Estimate probability $P_N(X=x)$

1. Find initial $x$ with $P_N(X) > 0$
2. **Burn in**: Perform t steps of Gibbs sampling, this is done to eliminate the influence of the initialization.
3. Sample values $x^t+1, x^t+2, \cdots , x^{t+N}$
4. Estimate: $P_N(X=x) \approx \frac{1}{N} | \{ i|X^{t+1}| X=x \}|$

<!-- More wordy explanation:
To start off we are selecting an initial value for $x$ which is above 0. This is done by randomly selecting a value from the set of possible values for $X$.

The several steps of Gibbs sampling are performed to eliminate possible biases introduced by the random initializations.

In the next step we sample new values for the variables -->