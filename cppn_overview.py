
from epann.core.tools.utils.activations import Activation
from epann.core.population.population import Population
from epann.core.tools.utils.mutations import Mutations

class InitializedAgent:
    def __init__(self, agent):
        self.nodes = agent.nodes
        self.connections = agent.connections
        self.acts = Activation()
                
    def evaluate(self, current_start, current_end):
        current_input = current_start + current_end + [1.0]
        total = 0
        for node in range(len(current_input)):
            input_act = getattr(self.acts, self.nodes[node]['activation'])
            a = input_act(current_input[node]) * self.connections[node]['weight'] * self.connections[node]['enable_bit']
            total += a
            
        output_act = getattr(self.acts, self.nodes[5]['activation'])
            
        return output_act(total)


class ComplexAgent:
    def __init__(self, agent):

        self.genome = agent

        self.nodes = agent.nodes
        self.connections = agent.connections

        self.acts = Activation()
        self.mut = Mutations()

        # complexify the genome
        self.complexify_initial_genome()

    def complexify_initial_genome(self):

        # Add two new nodes to the genome
        innovation_number = len(self.connections)

        self.connections, self.nodes, innovation_number = self.mut.add_node(self.genome, 1.1, innovation_number)
        self.genome.connections, self.genome.nodes = self.connections, self.nodes

        self.connections, self.nodes, innovation_number = self.mut.add_node(self.genome, 1.1, innovation_number)
        self.genome.connections, self.genome.nodes = self.connections, self.nodes

        # Add a new connection to the genome
        self.connections, self.nodes, innovation_number = self.mut.add_connection(self.genome, 1.1, innovation_number)
        self.genome.connections, self.genome.nodes = self.connections, self.nodes


    def evaluate(self, current_start, current_end):
        current_input = current_start + current_end
        total = 0
        for node in range(len(current_input)):
            pass


num_agents = 5

pop = Population(num_agents)
current_agent = pop.genomes[0]

agent = ComplexAgent(current_agent)
print agent.nodes
print agent.connections
