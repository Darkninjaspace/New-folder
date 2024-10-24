from pomegranate.distributions import Categorical, ConditionalCategorical
from pomegranate.markov_chain import*
from pomegranate.hmm import DenseHMM
import numpy

probs_Sophia = torch.tensor([
    [0.7,0.3]
    ])
sophia = Categorical(probs = probs_Sophia)

probs_Kitchen = torch.tensor([
    [0.2,0.8]
    ])
kitchen = Categorical(probs = probs_Kitchen)

probs_Start = torch.tensor([
    [0.5,0.5]
    ])
start = Categorical(probs = probs_Start)

probs_Transitions = torch.tensor([
    [0.7,0.3], #Sophia start: Sophia, Kitchen
    [0.2,0.8] #Kitchen start: Sophia, Kitchen
    ])
transistions = ConditionalCategorical(probs= [probs_Transitions])

states = [sophia,kitchen]
edges = [[0.7,0.3],[0.2,0.8]]
starts = [0.5,0.5]

model = DenseHMM(states, edges=edges, starts=starts)
observations = numpy.array([[[0],[0],[1],[0],[0],[0],[0],[1],[1]]])

print (model.predict(observations))