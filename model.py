from pomegranate import*
import numpy as np
from pomegranate.distributions import*
from pomegranate.bayesian_network import BayesianNetwork

rain = Categorical(
    [
        [0.7,0.2,0.1], #no rain, light rain, heavy rain
    ],
)

maintenence = ConditionalCategorical(
    [
        [
            [0.4,0.6], #chance of no rain, maintenence chance
            [0.2,0.8], #change of light rain, maintenence chance
            [0.1,0.9], #change of heavry rain, maintenence chance
        ],
    ]
)

train = ConditionalCategorical(
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

worldCup = Categorical(
    [
        [0.7,0.3] #chance if world cup affected coffee shop being open or not
    ]
)

coffeeShop = ConditionalCategorical(
    [
        [
            [
                [0.7,0.3], #world cup affected train late shop closed, world cup affected train late shop open
                [0.5,0.5], #world cup affected train on time shop closed, world cup affected train on time shop open
            ],
            [
                [0.4,0.6], #world cup not affected train on time shop closed, world cup affected train on time shop open
                [0.3,0.7], #world cup not affected train on time shop closed, world cup affected train on time shop open
            ],
        ]
    ]
)

model = BayesianNetwork()

model.add_distributions ([rain, maintenence, train]) #add all probabilities here

model.add_edge (rain,maintenence) #edge means that first thing influences the second (adds direction of influence)
model.add_edge (rain,train)
model.add_edge (maintenence,train)

#world cup, train affect coffee shop closed
#rain, maintenence affect train