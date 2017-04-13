

from epann.experiments.experiment import Experiment


num_generations, num_agents = 30, 36

exp = Experiment( num_generations, num_agents, verbose=True)

exp.run()



#
gen, agent = 0, 26

print exp.history[gen].genomes[agent].connections
print exp.history[gen].genomes[agent].nodes
# print [ exp.history[gen].genomes[agent].connections[connection]['weight'] for connection in exp.history[gen].genomes[agent].connections.keys()]

gen, agent = num_generations-1, 26

print '\n', exp.history[gen].genomes[agent].connections
print exp.history[gen].genomes[agent].nodes

# print [ exp.history[gen].genomes[agent].connections[connection]['weight'] for connection in exp.history[gen].genomes[agent].connections.keys()]

# something somethin