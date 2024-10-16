import numpy
import torch
from model import model

rain_values = ["none","light","heavy"]
maintenence_values = ["maintenence","no maintenence"]
train_values = ["on time","late"]
worldCup_values = ["affected","not affected"]
coffeeShop_values = ["open","closed"]
reception_values = ["interference","no interference"]
carCrash_values = ["crash","no crash"]
survival_values = ["survival","death"]
womanDoctor_values = ["male","female"]

probability = model.probability(
    torch.as_tensor(
        [
            [
                rain_values.index("light"),
                maintenence_values.index("maintenence"),
                train_values.index("late"),
                worldCup_values.index ("affected"),
                coffeeShop_values.index ("closed"),
                reception_values.index ("interference"),
                carCrash_values.index ("crash"),
                survival_values.index ("survival"),
                womanDoctor_values.index ("female"),
            ]
        ]
    )
)

print (probability)