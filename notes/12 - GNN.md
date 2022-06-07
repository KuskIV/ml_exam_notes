---
title: 12 - GNN
created: '2022-06-02T07:51:50.220Z'
modified: '2022-06-02T07:52:00.766Z'
---

# 12 - GNN
Graph Neural Networks (GNN) is the application of neural networks to the graph data structure. It is a powerful technique, which has recently gained a lot of traction in DL. The key ideas the GNN's revolve around is the idea of representing the nodes as vector embeddings for a concise and powerful representation, the edges could in theory also be represented through embeddings, but are typically not in the methods covered here. So how the edges are used in GNNs is that they denote the structure of the graph, they specify which to nodes have links between them and the weight of such edge if the edges are weighted, and they are used in the message passing algorithm also known as the Graph Convolutional Networks (GCN), this is a key idea, which we will expand upon. 

Before more formally specifying GNNs we will