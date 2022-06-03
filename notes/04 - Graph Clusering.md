---
attachments: [Clipboard_2022-06-03-13-15-57.png]
title: 04 - Graph Clusering
created: '2022-06-02T07:47:17.755Z'
modified: '2022-06-03T15:06:50.407Z'
---

# 04 - Graph Clusering

This lecture started on a segment of the course that is dedicated to machine learning with graph and networ data. In this lecture the focus was on a form of unsuperviced learning for graphs; community detectin, a.k.a. graph clusering.

## Communities

Informally, a community in a network is a group of nodes with greater ties internally than to the rest of the network.

The actors in a network tend to form groups of closely-knit connections. The groups are aslo called communities, clusters, cohesive subgroups or modues in different context. Rougly speaking, individuals interactin more frequently within a group that between groups.

![](@attachment/Clipboard_2022-06-03-13-15-57.png)

## Graph Clustering

When performing network clustering, it is the task of extracgint the natual community structure from networks of vertices and edges.

### Terminology and Notation

A cluster of $G=(V,E)$ is a partitioning of $C=\{ C_1, \dots, C_k \}$ of $V$

### Method Skeleton

Pick a quality measure for cluserings

Find an algorithm to (approzimately) determine the clusering with optimal quality.

## Edge Betweenness

Shortest path betweenness: We find the shortest path between all pairs of vertices and count how many run along each ege.

$$\beta(e)=\sum_{u,v\in V} \frac{\text{Numer of shortest path connection u, v going through e}}{\text{Numer of shortest paths connection u,v}}$$

Defined as: Number of shortest path passing the edge.

In order to find the shortest path between a partucular pair of vertizes can be done using breadth-first search, but a more efficient way is by using methods proposed by Newman and Brades, where Newman is implemented. But these are ouside the scope of this topic.

The betweenness score calculated in the slide, is also just one way of doing it. In the paper they discuss multiple ways. Another way is the random walk betweenness, where signals travel along a random about the network until they reach their destination. The expected net numer of time a random walk between a particular of vertizes will pass down a particular edge and sum over all vertex paris. 

Lastly where a unit resistance is placed on each edge of the network and unit current source and sink at a particular pair of vertices. The resulting current flow in the network will travel from source to sink along a multitude of paths, those with least resisteance carrying the greatest fraction of the current. the current-flow betweenness for and edge is defined to be the absolute value of the current along the edge summed over all source/sink paris.

One thing to note is that the last two are probably outside the scope of this presentation, as only the first way was introduced in the lecute.

## Newman, Girvan Algorithm

Newman-Girvan Algorithym produces a hierachy of $n$ clusterings.

Attributes of the algorithm:
- Iterative removal of edges from the network to split it into communities. The edges removed are being identified usin betweenneess measures.
- These are recalculated of the betweenness score after reach removal.

It differs from other work as it does not remove edges between vertex pairs with the lowest similarity, but on finding edges with the highest betweenness, where betweenness is some measure that favors edges that lie between communities and disfavors those that lie inside communities. Betweenness is based on the idea tha if two communities are joined by only a few intercommunitiy edges, then all paths through the network from vertices in one community to verticies in the other must pass along on of those few eges. Given a suitable set of paths, one can count ho many go along each ege in the graph and this number we then expect to be largest for the intercommunity edges, thus providing a method for identifying them.
Another way the method differs is in the inclusing of a recalulation step. If a standard divisive clustering was performed based on edge betweenness, the betweenness for all eges in the networ and the nremove edges in decreasing order of betweenness. The issue here is that once the first edge is removed, the betweenness values for the remaining edges will no longer reflect the network as it is now. This can give rise to unwanted behaviors. If two communities are joined by two edges, but for whatever reason, most pahts between the two flow along just one of those edged, then that edge will havea higher betweenness score and the otehr will not. AN algorithm that calculated betweennsses only once and then removed edges in the beteeenness order would remove the first edge early in the course of its operations, but the second might not get removed until much later. Thus the obvious division of the network ino two parts might not be discovered by the algorithm. In the worst case, the two parts themselves might be individually borken up before the divisoin between the two is made. The solution is to recalculate the betweenness score after the removal of each edge. This adds computational effort into the system, but it is deemed worth the cost.

The general from of the algorith mis as follows:
1. Calculate betweenness scores for all edges in the network
1. Find the edge with the highest score and remove it form the network. If two or more edges tie for the higest score, choose on of themat random.
1. Recalculate betweenness for all remaining edges
1. Repeat from step 1

Another issue is that the algorithm will be used on networks which are not know ahead of time, but how do we then know the found communities are good ones? This is a relevant problem, as this algorithm will always removed edges, even when there are no meaninfull communities in the network. In addition to this, the output is in the form of a dendrogram representing an entire nested hierarchy of possible community diviions for the network. So it is relevant to know which is the best one and where we should cut the dendrogram to get a sensible division of the network.

In order to address this question, a measure of quality is defined, called modularity. This measure is based on previous measure of assortative mixing proposed by Newman. Consider a particular division of a network into $k$ communities. Then define a $k \times k$ symmetric mateix __e__ whose element $e_{ij}$ is the fraction of all edges in the network that link vertices in community $i$ to vertives in community $j$. The trace in this matric Tr $e = \Sigma_i e_{ii}$ gives the fraction of edges in the network that connect vertices in the same community, and clearly a good division into communities should have a high value of this trace. The trace on its own is however not a good indicator of the quality of the divions since, for example, placing all vertices in a single community would give the maximal value of Tr $e = 1$ while given no information about community structue at all. So we further define the row (or column) sums $a_i=\Sigma_j e_{ij}$, which represents the fraction of edges tha connect to vertices in community $i$. In a network in which edges fall betseen vertices without regard for the communities they belong to, we would have $e_{ij}=a_ia_j$. Thus we can define a modularity measure by:

$$Q=\sum_i (e_{ii}-a^2_i) = \text{Tr e}-\| e^2\|$$

Where $\| x \|$ indicates the sum of the elements of the matric $x$. This quantity measures the fractino of the edges in the network that connectino vertices of the same type (i.e. within community edges) minus the expected value of the same quantity in a network with the same community divisions by random connection between the vertices. If the numer of within-community edges i no better than random, we well get $Q=0$. Values approaching $Q=1$, which is the maximum, indicate networks with strong community structure. In practice, values for such networks typically fall in the range from $0.3$ to $0.7$. Higher values are rare. Typically  we will calculate $Q$ for each split of a network into communities as we move down the dendogram, and look for local peask in its value, which indicate particularly satisfactory splits. Uwually there are one or two of such peaks.

## Mixture Model for Clustering

## Gaussian Mixture Models

Clustering is an unsupervised learning problem where we intend to find clusters of points in our dataset wit similar characteristics. When considering clustering methods, they can be hard (like K-Means) where each point is only assigned to one cluster. There is not uncertainty measure or probabilyty for other clusters the point could belong to. This is something Gaussian Mixture addresses, by represengin clusters as Gaussian distributions.

A Gaussian Mixture is a function cimprised of several Gaussians, each identified by $k \in \{1, \dots, K\}$, where $K$ is the number of clusters.Eahc Gaussian $k$ in the mixture is comprised of the following parameters:

- A mean $\mu$ defining the center
- A convoraiance $\Sigma$ defining the width

When applying Gaussian Mixture Models, in can be done using Expectation Maximization. Using this algorithm, we start with a random guess for what the clusters are going to be, and then proceed to improve iteratively by alternating two steps:

1. Expectation: Assign each datapoint to a cluster probailistically, meaning, the distance to the clusters.
1. Maximization: Update the parameters for the clusters (weighted mean location and variance-covariance matric) based on the points in the cluser (weighted by their probability assigned in the first set)

## Latent Mixture Random Graph Model

Graph Mixture Model




