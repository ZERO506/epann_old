
import numpy as np


class NeuralNetwork():

    def __init__(self):

        self.num_inputs = 5
        self.num_outputs = 3

        self.weights = self.init_weights()

        self.num_mutations = 3

        self.mutate()


    def init_weights(self):
        weights = [self.num_inputs, self.num_outputs] #np.random.randn(self.num_inputs, self.num_outputs)
        return dict.fromkeys(range(1), weights)


    def add_layer(self):

        connections_to_split = np.random.randint(len(self.weights.keys()))

        split_dims = self.weights[connections_to_split]

        value1, value2 = [ split_dims[0], split_dims[0] ], [ split_dims[0], split_dims[1]]

        weights = dict.fromkeys(range(len(self.weights) + 1))

        # Update weights before and including split
        for layer in range(connections_to_split):
            weights[layer] = self.weights[layer]

        # Update the newly generated weights
        weights[connections_to_split] = value1
        weights[connections_to_split+1] = value2

        # Update weights after the splot
        for layer in range(connections_to_split+2, max(weights.keys())+1):
            weights[layer] = self.weights[layer-1]

        return weights


    def mutate(self):
        print self.weights, '\n'
        for mutation in range(self.num_mutations):
            self.weights = self.add_layer()
            print self.weights



nn = NeuralNetwork()
# for layer in nn.weights.keys():
#     print nn.weights[layer]
#

# num_outputs = 1
# num_inputs = 5
#
# weights = np.random.randn(num_inputs, num_outputs)
# updated = np.diagflat(weights)
# ones = np.ones((num_inputs, num_outputs))
#
# identity = np.identity(updated.shape[0])
