- Inductive and transductive classification
- Homophily
- Independent classification
- Label propagation
- Node classification with Markov networks

## NEW
Hi im going to be talking about node classification.

Firstly i will be talking about the differences between transduction and inductive classification.
The ideas and goal between the two are very different.
In transductive classification we have all of the data both the training and the test data. We use this data to train the model and then we use the model to predict labels for the test data.

In inductive classification we only have the training data. We use this data to train the model. When the model have been trained we use the model to predict labels of the never seen before test data.
In a inductive classification we are essentially trying to create a more generic model. While the transductive classification is more specific and will only work for the specific data used in the training.

Now i will introduce the concept of homophily.
Homophily is when a link between individuals (such as friendship or other social connection) is correlated with those individuals being similar in nature. For example, friends often tend to be similar in characteristics like age, social background and education level. This is very often seen in real data, when closely linked individuals are similar in nature. This also the case when looking at communities in graphs the more densely connected a community the more similar they are.
The suggestion here is that we can use the homophily to make certain predictions about the nodes that are closely linked with known node, we can essentially expect some of the attributes to be reflected in the nodes.

Now i would like to talk a bit about label propagation, it is a transductive classification algorithm.
Label propagation is a method of learning that is used to predict the labels of unlabeled nodes in a graph.
The idea is that we can use the labels of the nodes in the graph to predict the labels of the unlabeled nodes.
The algorithm works by starting with a set of labeled nodes and then iteratively adding the labels of the neighbors of the labeled nodes.
Each unlabeled node is seen as a distribution over the labels, by randomly selecting a label from the distribution and doing it multiple time until probabilities stop changing.
This is done until the labels of the unlabeled nodes are assigned with the most likely label.

Now i will be talking a bit about gibbs sampling.
Gibbs sampling is a method of learning that is used to predict the labels of unlabeled nodes in a graph.
When performing gibbs sampling we randomly select a node unlabeled and then we randomly select a label for the node.
Then we use the label to predict the labels of the neighbors of the node.
This is done until the labels of the unlabeled nodes are assigned with the most likely label.

Now i will talk a bit about the self study.
For the self study we were using a graph representing a social network with 71 lawyers.
We want to predict the label practice on some of the nodes so we remove it randomly from some of them.

Now we want to predict the missing practice on the nodes, using gibbs sampling.
We then implement gibbs sampling on the graph and predict the labels of the nodes.
The accuracy of the prediction is 78%, though this can chang with additional runs because of the random nature of the algorithm.

I the next task we performs gibbs sampling multiple times to see how the accuracy changes.
The results show that accuracy can change a lot.

## OLD
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