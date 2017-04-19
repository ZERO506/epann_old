
from epann.core.population.genome.cppn import CPPN
from epann.core.tools.utils.structs import Structs

cppn = CPPN()
modify = Structs()

def adapt_genomes(nodes, connections, mod):
    if mod:
        nodes[6] = modify.generate_node('hidden')
        nodes[7] = modify.generate_node('hidden')

        connections[1]['enable_bit'] = 0
        connections[len(connections)] = modify.generate_connection([1, 6])
        connections[len(connections)] = modify.generate_connection([6, 5])

        connections[3]['enable_bit'] = 0
        connections[len(connections)] = modify.generate_connection([3, 7])
        connections[len(connections)] = modify.generate_connection([7, 5])

    return nodes, connections

def build_NN(nodes, connections):
    outputs = range(cppn.num_inputs, cppn.num_inputs + cppn.num_outputs)
    inputs = range(cppn.num_inputs)
    hiddens = list( set(cppn.nodes.keys()) - set(outputs + inputs))
    print outputs, inputs, hiddens

cppn.nodes, cppn.connections = adapt_genomes(cppn.nodes, cppn.connections, False)
build_NN(cppn.nodes, cppn.connections)