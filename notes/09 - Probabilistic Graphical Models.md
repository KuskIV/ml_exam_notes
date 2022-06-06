---
title: 09 - Probabilistic Graphical Models
created: '2022-06-02T07:49:26.203Z'
modified: '2022-06-02T07:50:02.823Z'
---

# 09 - Probabilistic Graphical Models

In probabilistic graphical models, the focus on the Hiddden Markov Model, which enables modeling temporal sequences of events, in terms of the probabilities of certain events happening in certain states.

Formally we characterize a HMM as a 5-tuple of the form $(S, V, A, B, \pi)$ where:

> - $S = \{s_1, ..., s_N\}$ is the set of **states**
> - $V = \{v_1, ..., v_M\}$ is the set of possible **observations** in the states (sensor measurements in TD lingo)
> - $A$ is the **transition matrix**, which is a NxN matrix, where N is the number of states, and  $a_{ij} = P(q_{t+1} = S_i | q_t = S_j)$ is the probability of transitioning from state i at the time t to state j at the time t+1, if one can not transtion from one state to another of course then $a_{ij} = 0$
> - $B$ is the **observation symbol probability distribution** in state j, it is given by $B = \{b_j(k)\}$, where $b_j(k) = P(V_k at t | q_t = S_j)$ that is it denotes the probabilitiy of observing the symmbol $V_k$ at time $t$ in state $S_j$
> - $\pi$ is the **initial state distribution**, it is given by $\pi = \{\pi\}$, where $\pi = P(q_1 = S_i)$ that is it denotes the probabilitiy of starting in state $S_i$

Now what can we use such a HMM to? 

Now given an appropriate 5-tuple $(S, V, A, B, \pi)$  we can use the model as a generator to give an observation sequence $O = O_1, O_2, \ldots, O_T$, where each obseration $O_t$ is a member of the set $V$ and $T$ is the length of the sequence, the process is as follows:

1. We sample a state $q_1 = S_i$ from the initial state distribution $\pi$
2. We sample an observation $O_1 = V_k$ from the observation symbol probability distribution $B$ at state $q_1$
3. We sample a state $q_2 = S_j$ from the transition matrix $A$ at state $q_1$
4. Now we can go back to step one to sample $O_{t+1}$ if $t + 1 \leq T$, otherwise we are done.
