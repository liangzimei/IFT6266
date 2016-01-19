import class_mlp
import utils_functions as utils
from class_mlp import MLP

network = MLP([28*28, 20, 20, 20, 10], utils.rect)
errTrain, errValid, errTest = network.train()
utils.plot(errTrain, errValid, errTest)


