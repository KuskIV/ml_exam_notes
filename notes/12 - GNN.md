---
title: 12 - GNN
created: '2022-06-02T07:51:50.220Z'
modified: '2022-06-02T07:52:00.766Z'
---

# 12 - GNN
Key litterature:
- MJ slides from moodle page
- [Graph Representation Learning, Hamilton](https://www.morganclaypool.com/doi/pdfplus/10.2200/S01045ED1V01Y202009AIM046?casa_token=tfO_fJZSzq4AAAAA:FTog3f3bZ6Cu91JsYmkN9Ytw0O3cmVSFB93iquBnbbOCItyf9_jJxFcwbJ9_Htc_5V-Tnk3lmqQp)

Graph Neural Networks (GNN) is the application of neural networks to the graph data structure. It is a powerful technique, which has recently gained a lot of traction in DL. The key ideas the GNN's revolve around is the idea of representing the nodes as vector embeddings for a concise and powerful representation, the edges could in theory also be represented through embeddings, but are typically not in the methods covered here. So how the edges are used in GNNs is that they denote the structure of the graph, they specify which to nodes have links between them and the weight of such edge if the edges are weighted, and they are used in the message passing algorithm also known as the Graph Convolutional Networks (GCN), this is a key idea, which we will expand upon. 

Before more formally specifying GNNs we will consider some of the use cases of GNNs. We consider three overall categories of use cases:
1. **Node Classification**: 
    - The goal here is to classify nodes represented through their embedding vector in classes
    - Is a user in a social network going to vote democrat or republican?
    - Is a sensor in a sensor network going to fail within the next 30 days?
    - Has a computer in a computer network been hacked?
2. **Link Prediction**
    - The goal here is to predict the links between nodes represented through their embedding vector. It could be whether a certain edge exists between two nodes or not, or it could be classifying the type of edge between two nodes.
    - Are two proteins interacting?
    - Is there a ’capital of’ relation between Sacramento and California?
    - Is user A going to become a follower of user B?
3. **Network classification**
    - Here the goal is to classify the entire graph.
    - Is a molecule a mutagen?
    - Is molecule a drug for a disease?

> **Graph Definition** 
>- A graph is given by $G=(V,E)$ where $V$ is a set of vertices and $E$ is a set of edges.
>- An edge exists between two nodes $u,v \in V$ iff $(u,v) \in V$ 
>- In an undirected graph for $u,v \in V \ if \ (u,v) \in E \rightarrow (v,u) \in E$ (symmetric)
>- An adjacency matrix is a $N\times N$ matrix $\textbf{A}$ where $\textbf{A}_{ij} = 1$ if there is and edge between nodes $i$ and $j$ and $0$ else. It can also be any real value, when representing a weight. $N = |V|$

We primarily consider undirected graphs.

> **Graph in Node Classification Setting**
- $G = ((V_l,V_u),E,A_t,Y)$
    - $V_l$ is the set of labeled nodes
    - $V_u$ is the set of unlabeled nodes
    - $E$ is the binary edge relation as above 
    - $A_t$ is the attributes 
    - $Y$ is the labels

Consider slide here to pose the Node Classification problem:
<img src="..\attachments\gnn_node_class.png" width="500px">

In Node Classification we consider the distinction between between the transductive and inductive setting.

**Transductive Node Classification Setting**
- The graph here is fixed, that is cannot be changed/extended during inference. So we **know** already all existing vertices, so we can rely on havin a fixed set of nodes (this is a limitation of the transductive setting).
- ➥ all nodes Vu that need to be classified already known when learning the classifier
- "Transfer" learning from one part of the graph to another part of the graph.

**Inductive Node Classification Setting**
- Here a Graph $G = ((V_l, V_u), E, A, Y)$ is used for training (possibly V_u = ∅).
- Nodes that are classified can be new nodes, which are added to $G$, or even nodes in a different graph $G'$
- Hence it has much more flexibility

Before considering the GNN we will consider a more classical approach, known as the Random Graph Model.

It consists of a two-stage sampling procedure for graphs: Given a graph $G=(V,E)$.

1. Step 1: for each node $v_i \in V$ sample latent coordinates $\mathbf{z}_i \in \mathbb{R}^d$ according to a Gaussian Mixture model:
    - $\mathbf{z_i} ~ \sum_{j=1}^k \lambda_j \mathcal{N}(\mu_j,\sum_j)$
1. Step 2: for each pair of nodes $v_i,v_j \in V$ sample the value of an Boolean edge variable $E_{i,j}$ according to logistic regression model dependent on Euclidean distance between latent coordinates: 
    - $P(E_{i,j} | \mathbf{z}_i,\mathbf{z}_j) = \frac{\exp(\alpha - \beta||\mathbf{z_i} - \mathbf{z_j}||)}{1 + \exp(\alpha - \beta||\mathbf{z_i} - \mathbf{z_j}}$

**Representation Learning**
In the following we will focus on how to obtain embeddings for the nodes. 

Here we consider two distinctions **shallow embeddings** and **functional embeddings**.

**Shallow Embedding**

So what is shallow embeddings? Shallow embeddings where you take all the nodes give them an id, an then assign them initially a vector embedding i specified dimensionality, and then you optimize exclusively this embedding, disregarding other structural information. A way to learn/optimize the first randomly intiazlied shallow embeddings is through the reconstruction loss.
In the reconstruction loss we aim to reconstruct the adjacency matrix, with for example squared error loss. Specifically consider: A graph $G= (V,E)$ we proceed in the following steps.
1. Select dimensionality $d$
2. For each node $v_i \in V$ sample a vector $\mathbf{z}_i \in \mathbb{R}^d$ and fix it as its initial node embedding. Sampling can be from $\mathcal{N}(0,1)$ for example.
3. Minimize the following construction loss:

    - $\mathcal{L}(G) = \sum_{i,j \in V} (\mathbf{z}_i^\intercal \mathbf{z}_i - \mathbf{A_{i,j}})^2$

4. Repeat step 3. until convergence.

A limitation of the shallow embedding is that they are inherently transductive, the embeddings depends on the specific training graph, and new nodes would not have id's/interpretation in that setting. Usable for Link prediction given this reconstruction loss above. More advanced forms of reconstruction loss are given in the litterate [hamilton]

**Functional Embedding**
- We can use for Link prediction or Node Classification.
- Given: one or several graphs
- Learn a function $f: (V,E,A_t,Y), i \in V \rightarrow \textbf{z}_i $ maps nodes in a graph to a vector embedding.
- Optimization in the space of parameters (weights) W defining the function.
- Minimize a task specific loss function (node/edge/graph classification error)
- Examples: graph kernels, GNNs
- works in inductive setting, hence also for transductive setting.

**GNNs with Message Passing/Graph Convolutions**
In the following we will discuss GNNs with message passing. There is a conenction with message passing and convolutions. Message passing is the idea that each node has neighbours and then these neighbours pass their embedding to the node, and the node performs some aggregation of these embeddings, hence its own embedding will depend on its neighbours, that is the graph structure. Now convultion operation is known from images, now think of a pixel as a node, now the kernel aggregates information from surrounding pixels, that is for example a 3x3 kernel will look at the surrounding pixels and aggregate the pixel values, similarly the message passing is "convolving" the embeddings of the neighbours. That is why we talk about the connection between message passing and convolution operation.

Consider the following slide showing GNN message passing:
<img src="..\attachments\gnn_message_passing.png" width="500px">
- We can see at step 0 we initalize the vector embeddings
- then at subsequent steps we use message passing, here we can see $\mathbf{W}^k \in \mathbf{R}^{d^{k+1}\times d^k}$ is the weight matrix for learning the weights of the nodes own embedding, $\mathbf{U}^k \in \mathbf{R}^{d^{k+1}\times d^k}$ is weight matrix for learning weights of the sum aggregation of the neighbours, and then $f$ is nonlinear activation function for example $\text{ReLU}(x) = max(x,0)$. 
- below the slide give concise notation using full matrix notation to denote the exact same computation.

Slide below show how we can use a Graph Convolutional Network (GCN) (GNN with message passing) for node classification:
<img src="..\attachments\gcn_arch_node_class.png" width="500px">
- so in the final layer we can output the number of logits we want for a multi-class classification problem or binary output for single-class classification.

However there is an issue with the GCN so far, that is it depends on the arbitrary ordering of the adjacency matrix, but we want an permutation invariant GNN, so here it is important to specify the initial embeddings not based node identifiers for example one-hot encoding, as then it would only work in transductive setting, but we must use for example attribute information to characterize the node embedding.

Additionally the update function suggested above, will lead to numerical instability for nodes with large neighbour set. This can simply be solved by using normalization, see slide here:
<img src="..\attachments\gnn_numerical_inst.png" width="500px">
- the second which also considers also the number of neighbours of the neighbours, is more smart in that, it will be larger value for neightbours with small number of other neighbours, so it will increase importance of the special neighbours, which not many others are connected too.

**Attention weighthing of neigbours**
In the basic above aggregation we just some all the neighbours, without considering which is more important. We can improve on this by using the attention mechanism, which will compute using some function $f$ the weighting factor $\alpha$ of the node and the neighbour to aggregate over. See slide here:
<img src="..\attachments\gnn_attention_weighting.png" width="500px">
- more options for $f$ is found in the litterature, for example the well known Bahdanau attention mechanism.

**Skip connection**
Imagine having many layers of message propagation, it can result in the following issues:
 - in the all nodes in the network will start converging to far away neighbours(there are more of those), 
 - over-smoothning all nodes become more/too similar,

Here we can use skip connections to remediate this issue.
- It encourages preservation of the information contained in $h^k(i)$ when constructing $h^{k+1}(i)$, a simple solution is seen from slide here:
<img src="..\attachments\gnn_skip_connection.png" width="500px">

**Use case overview**
In the following we will discuss how to extend the GCN to address the tasks of node classification, link prediction, and graph classification.

Node classification we have discuss above, see slide above.

Graph classificatino see slide here:
<img src="..\attachments\gcn_arch_graph_class.png" width="500px">

Link prediction see slide here:
<img src="..\attachments\gcn_arch_link_prediction.png" width="500px">

So now with GCN, we can just get new graph or new nodes, compute their initial embeddings and then use the learned weights, to propagate the embeddings through the network, and then solve the respective task. When using general attributes from the embedding and not node id's we can use for inductive setting, (which implies also transductive setting).