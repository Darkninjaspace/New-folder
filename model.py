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
        [0.1,0.9] #chance if world cup affected coffee shop being open or not
    ]
)

coffeeShop = ConditionalCategorical(
    [
        [
            [
                [0.2,0.8], #world cup affected train late shop closed, world cup affected train late shop open
                [0.3,0.7], #world cup affected train on time shop closed, world cup affected train on time shop open
            ],
            [
                [0.7,0.3], #world cup not affected train on time shop closed, world cup affected train on time shop open
                [0.8,0.2], #world cup not affected train on time shop closed, world cup affected train on time shop open
            ],
        ]
    ]
)

reception = ConditionalCategorical(
    [
        [
            [
                [0.95,0.05], #no rain yes interference, no rain no interference
            ],
            [
                [0.9,0.1], #light rain yes interference, light rain no interference
            ],
            [
                [0.75,0.25], #heavy rain yes interference, heavy rain no interference
            ],
        ]
    ]
)

carCrash = ConditionalCategorical(
    [
        [
            [
                [0.2,0.8], #no rain world cup affected crash, no rain world cup affected no crash
                [0.1,0.9], #no rain world cup not affected crash, no rain world cup not affected no crash
            ],
            [
                [0.4,0.6], #light rain world cup affected crash, light rain world cup not affected no crash
                [0.3,0.7], #light rain world cup not affected crash, light rain world cup not affected no crash
            ],
            [
                [0.65,0.35], #heavy rain world cup affected crash, heavy rain world cup not affected no crash
                [0.5,0.5], #heavy rain world cup not affected crash, heavy rain world cup not affected no crash
            ],
        ]
    ]
)

survival = Categorical(
    [
        [0.01,0.99], #chance of car crash death at low speeds, chance of car crash survival at low speeds
    ],
)

womanDoctor = Categorical(
    [
        [0.49,0.51], #chance of female doctor, chance of male doctor
    ],
)

model = BayesianNetwork()

model.add_distributions ([rain, maintenence, train, worldCup, coffeeShop, reception, carCrash, survival, womanDoctor]) #add all probabilities here

model.add_edge (rain,maintenence) #edge means that first thing influences the second (adds direction of influence)
model.add_edge (rain,train)
model.add_edge (maintenence,train)
model.add_edge (train, coffeeShop)
model.add_edge (worldCup, coffeeShop)
model.add_edge (rain, reception)
model.add_edge (rain, carCrash)
model.add_edge (worldCup, carCrash)

#world cup, train affect coffee shop closed
#rain, maintenence affect train
#rain affects cell reception 
#world cup and rain affect car crash
#chance that doctor in london that is single is woman