-  Probabilistic models (syntax and semantics)
-  Temporal models (Hidden Markov models)
-  Plate notation
-  Learning in structured models
-  Bayesian learning

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


