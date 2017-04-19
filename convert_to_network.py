
import numpy as np
from epann.core.tools.utils.activations import Activation

class NetworkBuilder:

    def __init__(self, node_genome, connection_genome):
        self.nodes = node_genome
        self.connections = connection_genome
        print self.nodes
        print self.connections

        self.inputs, self.hiddens, self.outputs = self.separate_nodes()
        print '\nInputs:', self.inputs, 'Hiddens:', self.hiddens, 'Outputs:', self.outputs

        self.activations = np.zeros(( len(self.nodes.keys()), 2))
        self.acts = Activation()

        self.connections_by_innodes, self.connections_by_outnodes = self.separate_connections()


        # Specific to the controller task
        self.observation_space = 9

        self.input_locations = self.calc_input_locations()
        self.hidden_locations = [ [0.0, 0.0] ]

        self.bias = [ 1.0 ]

        self.observations = self.form_inputs()



        self.evaluate()

    def calc_input_locations(self):
        xs = np.linspace(-1.0, 1.0, self.observation_space)
        return [ [ x, -1.0 ] for x in xs ]

    def form_inputs(self):
        current_input = {}
        input_count = 0
        for hidden_node in self.hidden_locations:
            for input_node in self.input_locations:
                current_input[input_count] = self.bias + input_node + hidden_node
                input_count += 1

        return current_input


    def separate_nodes(self):

        inputs = {(key if self.nodes[key]['type'] == 'input' else 'other'): value for key, value in self.nodes.items()}
        hiddens = {(key if self.nodes[key]['type'] == 'hidden' else 'other'): value for key, value in self.nodes.items()}
        outputs = {(key if self.nodes[key]['type'] == 'output' else 'other'): value for key, value in self.nodes.items()}

        del inputs['other']
        del hiddens['other']
        del outputs['other']

        return inputs, hiddens, outputs

    def separate_connections(self):

        connections_by_innodes = dict.fromkeys(self.nodes.keys(), [])
        connections_by_outnodes = dict.fromkeys(self.nodes.keys(), [])

        # Connections sorted by in_nodes
        print '\nConnections sorted by in_nodes:'
        for node in self.nodes.keys():

            current_connections = [[ connection, self.connections[connection]['out_node'] ] for connection in self.connections.keys() if self.connections[connection]['in_node'] == node]
            connections_by_innodes[node] = current_connections

            # Calculate the number of input connections for activation matrix
            self.activations[node, 1] = len( current_connections)

            print node, current_connections

        print '\nConnections sorted by out_nodes:'

        # Connections sorted by out_nodes
        for node in self.nodes.keys():
            current_connectionsR = [[ connection, self.connections[connection]['in_node'] ] for connection in self.connections.keys() if self.connections[connection]['out_node'] == node]
            connections_by_outnodes[node] = current_connectionsR

            print node, current_connectionsR


        return connections_by_innodes, connections_by_outnodes



    def evaluate(self):

        current_input = 3

        # Calculate the inputs
        for input in self.inputs:
            input_af = getattr(self.acts, self.nodes[input]['activation'])
            self.activations[input, 0] = input_af(self.observations[current_input][input])

        # Evaluate hiddens forward from their inputs
        for input in self.inputs:

            current_connections = self.connections_by_outnodes[input]

            while current_connections:

                connection = current_connections[0]
                connection_index = connection[0]

                activation = self.activations[input, 0] * self.connections[connection_index]['weight'] * self.connections[connection_index]['enable_bit'] # preactivation = x * weight * enable_bit
                hidden_out_node = connection[1]

                self.activations[hidden_out_node, 0] += activation
                self.activations[hidden_out_node, 1] -= 1

                current_connections.remove(connection)

            self.connections_by_outnodes[input] = current_connections

        # Check if hidden pre-activations are determined by other hidden nodes

        # First: calculate pre-activations for hidden nodes that have already been fully fed-forward.
        # for hidden in self.hiddens:
        #
        #     while self.activations:
        #
        #         current_connections = self.connections_by_outnodes[hidden]
        #
        #         shift_index = 0
        #
        #         connection = current_connections[shift_index]










        print '\n', self.activations

        print '\n Updated Connections by out_nodes:'
        for node in self.connections_by_outnodes.keys():
            print node, self.connections_by_outnodes[node]
