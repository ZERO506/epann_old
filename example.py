

from epann.experiments.experiment import Experiment

from convert_to_network import NetworkBuilder


num_generations, num_agents = 30, 5

exp = Experiment( num_generations, num_agents, verbose=True)

exp.run()



agent = 0

for gen in range( num_generations ):
    print '\n Generation: ', gen+1

    connections = exp.history[gen].genomes[agent].connections
    nodes = exp.history[gen].genomes[agent].nodes

    build = NetworkBuilder(nodes, connections)



