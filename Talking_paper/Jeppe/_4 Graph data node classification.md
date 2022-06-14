- Inductive and transductive classification
- Homophily
- Independent classification
- Label propagation
- Node classification with Markov networks

Hi im going to be talking about graph node classification.

Firstly im going to cover what is meant by:
- transductive classification
- inductive classification
- homophily

transductiv when is when the graph is fixed meaning the graph structure does not change from the training to the testing. All node needed to be accounted for are already known during the training.

Inductive when is when the graph is not fixed meaning the graph structure can change from the training to the testing.

Homophily is when a link between individuals (such as friendship or other social connection) is correlated with those individuals being similar in nature. For example, friends often tend to be similar in characteristics like age, social background and education level. This is very often seen in real data, when closely linked individuals are similar in nature. This also the case when looking at communities in graphs the more densely connected a community the more similar they are.

Label Propagation Algorithm (LPA) semi-supervised is an iterative algorithm where we assign labels to unlabelled points by propagating labels through the dataset.
__Characteristics__
- No node features
- Transduction classification exploiting homophily
- For unlabeled nodes compute probability distribution over class labels

Within community networks, the label propagation algorithm aims the change the label of each node based on the communities label. The biggest advantage for label propagation is it excellent runtime. 

Label propagation works on the relatively simple assumption that closely connected nodes also have the same class aka label. The effect of this assumption is that it is possible to propagate the label to unlabeled nodes in the network.

The algorithm works by performing a random walk foreach of the unlabeled nodes. This is done to determine the probability distribution of reaching a node with a label.
This is then done multiple times until the probabilities stop changing in the unlabeled nodes. Unlabeled nodes are then assigned a label based on the probability distribution.

For the task we were asked to write the gibbs sampling function.

## Gibbs Sampling
But first ill quickly explain what gibbs sampling is
Problem: compute a marginal probability $P_N(X=x)$.

(approximate) solution: generate a sequence of samples: $X_1,X_2, \cdots X_N$
So that the frequencies in the sample (approximate) match the marginal probability.

The idea behind Gibbs sampling is to obtain new samples from previous sample by randomly changing the value of the only one selected variable.

From the results in the self study 
- We can see that the standard divination. is low over 5 runs of gibbs sampling so seems decently stable,
- we see that the accuracy as a function of the number of steps swings quite a bit in [.65,.80], and that more steps doesn't really add much