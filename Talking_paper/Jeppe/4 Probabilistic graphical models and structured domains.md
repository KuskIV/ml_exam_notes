-  Probabilistic models (syntax and semantics)
-  Temporal models (Hidden Markov models)
-  Plate notation
-  Learning in structured models
-  Bayesian learning


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

Hi im going to be talking about the probabilistic graphical models and structured domains. Firstly i will briefly cover hidden markov models.


Markov model and hidden markov models are build on the same principle. The hidden markov model is a probabilistic model that is built on the Markov assumption. The Markov assumption is that the probability of a state is directly related to the probability of the previous state.

Hidden markov models are a type of probabilistic graphical model that is used to model the temporal dynamics of a system. A hidden markov model two different types of variables these are:
- State variables, these are the variables that are used to describe the state of the system at each point in time.
- Observation variables, these these describe what can be observed from the system at each point in time.

In hidden markov models we cannot observe the stats themselves, bu only the results from the observations. What we try to estimate is the probability of the system being in a certain state. The probability of the hidden states is essentially what we try to estimate in the hidden markov model. This helps to describe the dynamics of the system.

When looking at the implementation we can see that it takes three input as parameters.

prior model: This is the probability of the system being in a certain state at the start of the system.

trans model: This is the probability of transitioning between the different states.

sensor model/emission matrix: The sensor model specifies the probability of detection by each given the state. Example this tells us what the probability of someone having a umbrella when the state is rain.

The data is then the actual observations of the system.

Now i would like to talk about our exercise 2 from the self study. We need to determine which meteorologist to believe based on the data.

Thus we make a transition matrix for each one of them, and create a HMM for each of them. We then use the HMM to determine which meteorologist to believe. We calculate the log likelihood of the data for each of them. and find that the meteorologist 2 is more likely to be right based on the data.


