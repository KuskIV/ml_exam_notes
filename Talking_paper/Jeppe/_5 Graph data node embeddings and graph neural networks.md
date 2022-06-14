- Node embeddings: shallow and functional
- Message passing updates
- Elements of GNN architectures (Skip connections, attention)
- GNNs for node classification, graph classification and link prediction

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

Message passing is the idea that each node has neighbours and then these neighbours pass their embedding to the node, and the node performs some aggregation of these embeddings, hence its own embedding will depend on its neighbours, that is the graph structure.

For the first task we observe the effects of changing the epochs, the results show that more is better and we are at 100% accuracy at 60 epochs consistently. A larger number of hidden dimensions also seems to improve the accuracy.

For teh next task we create a new graph as can be seen below, we than mark each nodes that a two or less links away from the originals marked nodes.

We train the models on this new graph and see that the accuracy for the train set 1.0 and 0.99 for the test set.
Initialy this seems to be simple task, but To show that the model is inherently transductive we will generate new dataset, where we move the two  nodes.

This results in a much worse performance from the previose experiment, but we can see that the model is still transductive.