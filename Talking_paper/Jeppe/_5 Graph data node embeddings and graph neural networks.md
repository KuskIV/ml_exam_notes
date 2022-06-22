- Node embeddings: shallow and functional
- Message passing updates
- Elements of GNN architectures (Skip connections, attention)
- GNNs for node classification, graph classification and link prediction

## NEW
Hi im going to be talking about graph data node embeddings and graph neural networks. 
There are two types of node embeddings that i will be talking about.
An embedding is used to represent a vector in a lower dimensional space.
For graphs the embedding is a vector used to represent the nodes in a graph.
The two types that are frequently used are, shallow embeddings and functional embeddings.
Shallow embeddings optimize directly in the space of the embedding vectors. 
Functional embeddings we learn the embedding vectors by optimizing the loss function.

Now that i covered what is meant by embeddings i will be talking about message passing in graph neural network.
Conceptually message passing is very simple, we just need to know how to update the embedding vectors.
This is do trough multiple iterations called rounds in message passing.
In each round we update the embedding vectors of the nodes in the graph, based on the embedding vectors of the neighbors.
Essentially by doing this we are obtaining information about the graph, from the perspective of the nodes. The more round we perform message passing the information we obtain. 
The actual performance of the message passing in simply aggregating the embedding vectors of the neighbors, with some activation function.
When we decide we have performed enough rounds we can use the embedding vectors to predict the labels of the nodes.
I think the easiest way to think about this to think a about convocational neural networks and the idea of a convocational layer. Where the kernel is a matrix of the same size as the embedding vector, and the kernel is applied to each part of image, to obtain a lower dimensional vector representation.

What can we actually use this graph for when all embedding vectors are updated?.
The application generally falls into three different categories.

Node classification is essentially the same as labeling the nodes in a graph. We have some node without a class aka label and we want to predict the class of the nodes.
Graph classification is when  we have a graph and we want to predict the class of the entire graph. An example of this could be a graph of a social network, and we want to know what type of network the network is.
Link prediction is when we have a graph and we want to predict the probability that two nodes are connected. Essentially we want to predict the probability that two nodes are connected.

Now i will be talking a bit about the self study
For the exercises a gnn has been constructed in the first task we experiment with how the accuracy of the model changes when we change the parameters.
We change the number of epochs and the number of hidden units in the gnn.
From the epochs we can see that the accuracy of the model is increasing, but at a round 100 epochs, we start to see symptoms of overfitting.

Changing the number of hidden units seems to indicated that more is better, but this does come with performance costs.

For the next task we create a new network following the same rules. We color two spot in the graph and then mark each node that is less or equal to 2 steps away.
The result from this are good, bu we expects that the accuracy will fall drastically if we try to provide it with a new graph. This i because it is inherently tranductive.

When testing the rained model on a new graph we can immediately see that it performs much worse than the model that we trained on the same graph.

If i have time i want to talk a bit about:
Tranductive classification and inductive classification.

In transductive classification we have all of the data both the training and the test data. We use this data to train the model and then we use the model to predict labels for the test data.

In inductive classification we only have the training data. We use this data to train the model. When the model have been trained we use the model to predict labels of the never seen before test data.
## OLD
Hi im going to be talking about graph neural networks.
Firstly im going to talk about what a graph neural network is.
And briefly cover some aspect of their architecture.

Graph Neural Networks (GNN) is the application of neural networks to the graph data structure.
The key ideas the GNN's revolve around is the idea of representing the nodes as vector embeddings for a concise and powerful representation.

So how the edges are used in GNNs is that they denote the structure of the graph, they specify which to nodes have links between them and the weight of such edge if the edges are weighted, and they are used in the message passing algorithm also known as the Graph Convocational Networks (GCN), this is a key idea, which we will expand upon.

There are generally three use cases of GNNs:
1. **Node Classification**
2. **Link Prediction**
3. **Network classification**

Since i mentioned both embedding and message passing ill also quickly talk about them.

There are two types of node embeddings:
- **Shallow embeddings**: Shallow embeddings where you take all the nodes give them an id, an then assign them initially a vector embedding in a specified dimensionality, and then you optimize exclusively this embedding, disregarding other structural information.
- **functional embeddings**: Here we learn a function that can map the nodes in a graph to the vector embeddings, and then we optimize this function.

Message passing is the idea that each node has neighbors and then these neighbors pass their embedding to the node, and the node performs some aggregation of these embeddings, hence its own embedding will depend on its neighbors, that is the graph structure.

For the first task we observe the effects of changing the epochs, the results show that more is better and we are at 100% accuracy at 60 epochs consistently. A larger number of hidden dimensions also seems to improve the accuracy.

For teh next task we create a new graph as can be seen below, we than mark each nodes that a two or less links away from the originals marked nodes.

We train the models on this new graph and see that the accuracy for the train set 1.0 and 0.99 for the test set.
Initially this seems to be simple task, but To show that the model is inherently transductive we will generate new dataset, where we move the two  nodes.

This results in a much worse performance from the previous experiment, but we can see that the model is still transductive.