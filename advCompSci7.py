from pomegranate.distributions import Categorical, ConditionalCategorical
from pomegranate.markov_chain import*
from pomegranate.hmm import DenseHMM
import numpy

probs_Start = torch.tensor([
    [0.5,0.5]
    ])
start = Categorical(probs = probs_Start)

probs_Transitions = torch.tensor([
    [0.7,0.3], #Sophia start: Sophia, Kitchen
    [0.2,0.8] #Kitchen start: Sophia, Kitchen
    ])
transistions = ConditionalCategorical(probs= [probs_Transitions])

model = MarkovChain([start,transistions])
model.sample(1)

print(model.sample)

"my mom"
"traffic"

[0.7,0.3]#Sophia start: Sophia, Kitchen 
[0.2,0.8]#Kitchen start: Sophia, Kitchen

probs_Sophia = torch.tensor([
    [0.7,0.3]
    ])
probs_Kitchen = torch.tensor([
    [0.2,0.8]
    ])