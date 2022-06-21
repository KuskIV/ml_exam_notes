- What are communities
- Newman Girvan algorithm
- Modularity
- Node clustering with probabilistic mixture model

Hi i am going to be talking about Graph data community detection.

For this is will first be talking about what a community is.
A community is in the context of graphs a part of the graph that is more closely tied together internally than they are with the rest of the graph. The communities are essentially part of the network that interacts more frequently with each other. These communities tend to be more connected than the rest of the network. The closer a community is connected the more similar the to each other the community is, this is called homophile.   
Communities can have many different names and structure depending on the context. Sometimes called clusters, cohesive subgroups or modules. 
The different types of communities are:
- coherent subgroups, when we identify a single cluster.
- Graph clustering, when we split the graph into disjoint clusters.
- overlapping communities, when the communities overlap with each other.
- fuzzy clustering, when there are different degrees of membership in the communities.

Next i will explain the Newman Girvan algorithm.
The Newman Girvan algorithm is a method for detecting communities in a graph.
The Idea behind the algorithm is in essence very simple and be described in simple steps. 
I is important to understand betweeness centrality, this is a measure of how often a node is connected to another node, and is central part of the algorithm.
1. For every node in the graph we calculate the betweeness centrality.
2. Then we remove the edge with the highest betweeness centrality.
3. Then we calculate the betweeness centrality for every remaining edge.
4. We then repeat until the graph is empty.

We now a hierarchy of the different communities in the graph.
To evaluate which of these communities are the most connected to each other we can use the modularity.

Modularity is a measure of how well a community is connected to the rest of the graph.
So using this we can find the most connected communities. A high modularity score will have many connections within the community, but only a few connections outside the community.

The next thing i will be talking about is node clustering with probabilistic mixture model.
probabilistic mixture model or gaussian mixture model is a method for clustering data, that uses proportional mixing of gaussian distributions.
The identified clusters will also end up as gaussian distributions.

Now i will be talking about the self study.
For the self study we were using a graph representing a social network with 71 lawyers. The dataset has three different kinds of relationships described, but we will only be focusing on the friendship relationship. 
Each node in the graph has the following attributes:
- Practice
- Age
- Seniority
- Office
- Gender
- Status

Originally it is a directed graph but we turn it into a undirected one for simplicity sake.
We then define a function for measuring the modularity based on a community and an attribute.

In the first exercise we try to split the graph into varying amount of communities to identifying which have the best split. In the evaluation we can se that the highest modularity score achieved when we have 5 communities is 0.073.

Now we compute the modularity for each of the attributes.
From this we can see that status and office are the most connected attributes, for a community.
Status suggest 2 communities while office suggest 3 communities.
Based on the modularity score we can see that these two attributes are much better at making the correct community's than the newman girvan algorithm.






## OLD
Hi im going to be talking a bit about community detection.

Firstly what is a community?
A community is in the context of graphs a part of the graph that is more closely tied together internally than they are with the rest of the graph. The communities are essentially part of the network that interacts more frequently with each other.

When talking about communities it is also important to know what modularity in graph theory means. Modularity is essentially a measure of how well the graph is connected, measuring the density of the connections withing a community. A high modularity score will have many connections within the community, but only a few connections outside the community.

For the first task we will use the Newman-Girvan algorithm to find the communities in Lazega network. 

The Newman-Girvan algorithm is in essence very simple. The idea is that it measure the betweenness of all edges in the network, then removes the removed the edges with the highest betweenness score. The betweenness score is then recalculated for the remaining edges. This is repeated until the network is empty. In the end a dendrogram is constructed representing the community hierarchy. This can then be used to select the best community's using the modularity score.

Betweenness is based on the idea tha if two communities are joined by only a few intercommunitiy edges, then all paths through the network from vertices in one community to vertices in the other must pass along on of those few edges.

When performing the experiment:

Using the Newman-Girvan algorithm we find that the number of communities that yield the highest modularity is 5 with a score of 0.073. Looking at the attribute of the network and calculating the modularity score based on these attributes we can see that communities suggested by Status and office has a much higher modularity score than the one suggested by the Newman-Girvan algorithm.

Now ill quickly cover what a Gaussian Mixture Models. So what is a Mixture model?
A mixture model is essentially used when we want a model to account for multiple different distributions. The mixture model is constructed using mixture components that each represents a distribution in the mixture model. A gaussian mixture model is a mixture model that is constructed using gaussian distributions as mixture components.  

When applying Gaussian Mixture Models, in can be done using the Expectation Maximization algorithm. Using this algorithm, we start with a random guess for what the clusters are going to be, and then proceed to improve iteratively by alternating two steps:

1. Expectation: Assign each datapoint to a cluster probabilistically, meaning, the distance to the clusters.
2. Maximization: Update the parameters for the clusters (weighted mean location and variance-covariance matrix) based on the points in the cluster (weighted by their probability assigned in the first set)
