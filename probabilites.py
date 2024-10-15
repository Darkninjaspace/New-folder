import numpy
import torch
from model import model

rain_values = ["none","light","heavy"]
maintenence_values = ["maintenence","no maintenence"]
train_values = ["on time","late"]
worldCup_values = ["affected","not affected"]
coffeeShop_values = ["open","closed"]
probability = model.probability(
    torch.as_tensor(
        [
            [
                rain_values.index("light"),
                maintenence_values.index("maintenence"),
                train_values.index("on time"),
                worldCup_values.index ("affected"),
                coffeeShop_values.index ("open")
            ],
        ]
    )
)

print (probability)