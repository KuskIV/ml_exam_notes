---
title: 12 - GNN
created: '2022-06-02T07:51:50.220Z'
modified: '2022-06-02T07:52:00.766Z'
---

# 12 - GNN
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


    