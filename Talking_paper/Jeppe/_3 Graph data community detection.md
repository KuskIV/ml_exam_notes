- What are communities
- Newman Girvan algorithm
- Modularity
- Node clustering with probabilistic mixture model

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
