- Probabilistic models (syntax and semantics)
- Inference in probabilistic graphical models
- Maximum likelihood learning
- The EM algorithm 

## NEW
Hi im going to be talking about the probabilistic graphical models. 
I will briefly cover bayesian learning, and then hidden markov models.
But firstly ill introduce the concept of probabilistic graphical models, the ideas behind Maximum likelihood learning and the EM algorithm.

Probabilistic graphical models are a type of graphical model that is used to model the dynamics of a system. A probabilistic graphical model two different types of variables these are: 
- State variables, these are the variables that are used to describe the state of the system at each point in time.
- Observation variables, these these describe what can be observed from the system at each point in time.

The maximum likelihood learning is probabilistic approach to determine values fro parameters of a model. The goal is to find the parameters that maximize the likelihood of the data. To sum up maximum likelihood learning is A technic to find the parameters that maximize the likelihood of the data. 

Now to the EM algorithm, expectation maximization. EM is a way to find the maximum likelihood parameters of a model. EM is a iterative algorithm that is used to find the maximum likelihood parameters of a model.

The EM algorithm generally works consists of the following steps:
I. Initialization of the parameters of the model.
II. Expectation step, where the model is estimated based on the data.
III. Maximization step, where the model is updated based on the estimated parameters.

Now to bayesian learning, is a probabilistic method to determine the parameters of a model. 
This is done by having a prior distribution over the parameters of the model. Using bayes rule we then combine the prior distribution with the likelihood of the data. This gives us the posterior distribution over the parameters of the model. In bayesian learning we treat the parameters of the model as the latent variables, meaning that the parameters are not directly known to the user. 

Bayesian learning is an example of static graphical models. Thus we work under the assumption that the parameters are independent of each other.

An example of dynamic, temporal graphical models is the hidden markov model.
Hidden markov models are a type of probabilistic graphical model that is used to model the temporal dynamics of a system.
They are used to model the dynamics of a system, with the assumption that the probability of a state is directly related to the probability of the previous state.
In hidden markov models we cannot observe the stats themselves, but only the results from the observations. What we try to estimate is the probability of the system being in a certain state. The probability of the hidden states is essentially what we try to estimate in the hidden markov model. This helps to describe the dynamics of the system.

A hidden markov model two different types of variables these are:
- State variables, these are the variables that are used to describe the state of the system at each point in time.
- Observation variables, these these describe what can be observed from the system at each point in time.

Emission matrix: The sensor model specifies the probability of detection by each given the state. Example this tells us what the probability of someone having a umbrella when the state is rain.
Transition matrix: The transition matrix specifies the probability of transitioning between the different states.

To summarize hidden markov models are a type of probabilistic graphical model that is used to model the temporal dynamics of a system, without knowing the state of the system.




## OLD
Hi im going to be talking about probabilistic graphical models. 

Firstly ill talk a bit about the uses for probabilistic graphical models. They are often used in the context of machine learning and statistical analysis.

There are certain advantages of using probabilistic graphical models these are:
- Principled quantification of prediction uncertainties.
- Robust and principled techniques to deal with incomplete.information, missing
data.
- Provides a general model of the domain that can in principle be used to answer
any inference query.
- Enables integration of domain knowledge.
- Transparent and explainable.

If the data is missing certain points it is possible to use the maximum likelihood estimator to fill in the missing data. Essentially MLL gives us the probability of a certain event happening. To do this we attempt to find the value that maximizes the likelihood. Maximum likelihood estimation is commonly used in statistical analysis, where it helps to find the best fit to the data.

However if we are missing a general parameter of the distribution we can not use the maximum likelihood estimator. Instead we have to utilize a iterative algorithm called the EM algorithm.

Now ill be talking a bit about the EM algorithm, it is closely related to Bayesian inference.
The EM algorithm is the expectation maximization algorithm. It is a method for learning the parameters of a probabilistic model. 
The EM algorithm generally works consists of the following steps:
I. Initialization of the parameters of the model.
II. Expectation step, where the model is estimated based on the data.
III. Maximization step, where the model is updated based on the estimated parameters.

The expectation step and the maximization step are then repeated until the model converges. The parameters of distribution are often the variance and mean of the distribution.

Correctness of the em-algorithm is important. The em-algorithm is not guaranteed to converge to the correct solution. It can only guarantee that it finds the local maximum. To account for this it is common to run the algorithm multiple times with different starting points and select the best solution.  
