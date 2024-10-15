import numpy
import torch
from model import model

rain_values = ["none","light","heavy"]
maintenence_values = ["maintenence","no maintenence"]
train_values = ["on time","late"]
probability = model.probability(
    torch.as_tensor(
        [
            [
                rain_values.index("none"),
                maintenence_values.index("maintenence"),
                train_values.index("on time")
            ],
        ]
    )
)

print (probability)