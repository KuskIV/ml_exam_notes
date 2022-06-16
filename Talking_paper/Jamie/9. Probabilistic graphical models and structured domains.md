- Probabilistic models (syntax and semantics)
- Temporal models (Hidden Markov models)
- Plate notation
- Learning in structured models
- Bayesian learning


I will be presenting Probabilisti models. A **probabilistic model** is typically learned from data using **statistical learning techniques**. They typically apply **Probabilistic inference** algorithms to use models for prediction or structure analysis. **Probabilitis inference** is the task of deriving the probability of one or more random variables taking a specific cvalue or set of values.


 Now a **Probabilistic Graphical Model**:
- supports a structured specification of high-dimensional distributions in terms of low-dimensional factors
- its structured representation can be exploited for efficient learning and inference algorithms (sometimes ...)
- its graphical representation gives a human-friendly design and description possibilities

Some Advantages of probabilistic methods:
- Principled quantification of prediction uncertainties
- Robust and principled techniques to deal with incomplete information, missing data. 
- Provides a general model of the domain that can in principle be used to answer any inference query.
- Enables integration of domain knowledge. 
- Transparent and explainable.

Now I'm going to talk about **Hiddden Markov Models**, which enables modeling temporal sequences of events, in terms of the probabilities of certain events happening in certain states.
a **Hiddden Markov Model** consist of an Markov Chain(which is hidden) and a set of observed Variables.
The observed variable only depends on the current hidden state, and not on any other previous state.
The emission probabilities are the probabilities of some observed variable given a hidden state.

In **Bayesian inference** **plate notation** is a method of representing variables that reapeat in a graphical model. Instead of drawing each repreated variable individually, a plate or rectangle is used to group variables into a subngraph that repeat togheter and number is drawn on the plate to represent the number of repititions of the subgraph in the plate..


NEED WORK