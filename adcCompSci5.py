from pomegranate import*
import numpy as np
from pomegranate.distributions import*
from pomegranate.bayesian_network import BayesianNetwork

rain = categorical(
    [
        [0.7,0.2,0.1] #no rain, light rain, heavy rain
    ]
)

maintenence = conditional_categorical(
    [
        [0.4,0.6], #chance of no rain, maintenence chance
        [0.2,0.8], #change of light rain, maintenence chance
        [0.1,0.9] # change of heavry rain, maintenence chance
    ]
)

train = conditional_categorical(
    [
        [
            [
                [0.8,0.2], #no rain yes maintenence on time, no rain yes maintenence late
                [0.9,0.1], #no rain no maintenence on time, no rain no maintenence late
            ],
            [
                [0.6,0.4], #light rain yes maintenence on time, light rain yes maintenence late
                [0.7,0.3], #light rain no maintenence on time, light rain no maintenence late
            ],
            [
                [0.4,0.6], #heavy rain no maintenence on time, heavy rain no maintenence late
                [0.5,0.5], #heavy rain no maintenence on time, heavy rain no maintenence late
            ],
        ]
    ]
)

model = BayesianNetwork()
model.add_distributions ([rain, maintenence, train]) #add all probabilities here
model.add_edge (rain,maintenence) #edge means that first thing influences the second (adds direction of influence)