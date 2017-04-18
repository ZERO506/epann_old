
import numpy as np
from epann.core.tools.utils.activations import Activation

class NetworkBuilder:

    def __init__(self, node_genome, connection_genome):
        self.nodes = node_genome
        print self.nodes.keys()
        self.connections = connection_genome

        self.inputs, self.hiddens, self.outputs = self.separate_nodes()

        print '\nInputs:', self.inputs
        print 'Hiddens:', self.hiddens
        print 'Outputs:', self.outputs

        self.activations = np.zeros(( len(self.nodes.keys()), 2))


        self.connection_bank = self.separate_connections()


        self.acts = Activation()


        self.observation_space = 9

        self.input_locations = self.calc_input_locations()
        self.hidden_locations = [ [0.0, 0.0] ]

        self.bias = [ 1.0 ]

        self.observations = self.form_inputs()

        self.evaluate()

    def calc_input_locations(self):
        xs = np.linspace(-1.0, 1.0, self.observation_space)
        return [ [ x, -1.0 ] for x in xs ]

    def separate_nodes(self):

        inputs = {(key if self.nodes[key]['type'] == 'input' else 'other'): value for key, value in self.nodes.items()}
        hiddens = {(key if self.nodes[key]['type'] == 'hidden' else 'other'): value for key, value in self.nodes.items()}
        outputs = {(key if self.nodes[key]['type'] == 'output' else 'other'): value for key, value in self.nodes.items()}

        del inputs['other']
        del hiddens['other']
        del outputs['other']

        return inputs, hiddens, outputs

    def separate_connections(self):
        connect_trackR = dict.fromkeys(self.nodes.keys(), [])
        connect_track = dict.fromkeys( self.nodes.keys(), []  )

        print '\n'

        for node in self.nodes.keys():

            current_connections = [[ connection, self.connections[connection]['out_node'] ] for connection in self.connections.keys() if self.connections[connection]['in_node'] == node]
            connect_track[node] = current_connections

            self.activations[node, 1] = len( current_connections)

            print node, current_connections

        print '\n'

        for node in self.nodes.keys():
            current_connectionsR = [[ connection, self.connections[connection]['in_node'] ] for connection in self.connections.keys() if self.connections[connection]['out_node'] == node]
            connect_trackR[node] = current_connectionsR
            # self.activations[node, 1] = len( current_connections)

            print node, current_connectionsR


        return connect_track

    def form_inputs(self):
        current_input = {}
        input_count = 0
        for hidden_node in self.hidden_locations:
            for input_node in self.input_locations:
                current_input[input_count] = self.bias + input_node + hidden_node
                input_count += 1

        return current_input

    def evaluate(self):

        current_input = 3

        # Calculate the inputs
        for input in self.inputs:
            input_af = getattr(self.acts, self.nodes[input]['activation'])
            self.activations[input, 0] = input_af(self.observations[current_input][input])

        # # Calculate the hiddens
        # pass_check = dict( (key, len(self.connection_bank[key])) for key in self.hiddens   )
        # while all(not(i>0) for i in pass_check.keys()):
        #     for hidden in self.hiddens:
        #


        # all(not (i > 0) for i in hiddens)

        # # Calculate the hiddens
        # for hidden in self.hiddens:
        #     print hidden, self.connection_bank[hidden]
        #
        # # Calculate the outputs
        # for output in self.outputs:
        #     print output, self.connection_bank[output]

        print self.activations
