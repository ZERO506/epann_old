
from convert_to_network import NetworkBuilder

nodes = {0: {'activation': 'linear', 'type': 'input'}, 1: {'activation': 'linear', 'type': 'input'}, 2: {'activation': 'linear', 'type': 'input'}, 3: {'activation': 'linear', 'type': 'input'}, 4: {'activation': 'linear', 'type': 'input'}, 5: {'activation': 'sine', 'type': 'output'}, 6: {'activation': 'sine', 'type': 'output'}, 7: {'activation': 'gauss', 'type': 'hidden'}, 8: {'activation': 'sigmoid', 'type': 'hidden'}}

connections = {0: {'out_node': 0, 'in_node': 5, 'enable_bit': 0, 'weight': 0.2330524144473161}, 1: {'out_node': 0, 'in_node': 7, 'enable_bit': 1, 'weight': -0.6777230137503192}, 2: {'out_node': 7, 'in_node': 5, 'enable_bit': 1, 'weight': -0.6903680475625633}, 3: {'out_node': 3, 'in_node': 5, 'enable_bit': 1, 'weight': 0.248773878910518}, 4: {'out_node': 4, 'in_node': 5, 'enable_bit': 1, 'weight': 1.3153983729762055}, 5: {'out_node': 0, 'in_node': 6, 'enable_bit': 1, 'weight': 1.1504185111915837}, 6: {'out_node': 1, 'in_node': 6, 'enable_bit': 1, 'weight': -2.204995670375838}, 7: {'out_node': 2, 'in_node': 6, 'enable_bit': 0, 'weight': -0.19795255127532302}, 8: {'out_node': 3, 'in_node': 6, 'enable_bit': 1, 'weight': 0.15748718332879827}, 9: {'out_node': 4, 'in_node': 6, 'enable_bit': 1, 'weight': 0.595723118382152}, 14: {'enable_bit': 1, 'in_node': 8, 'weight': -0.720040908999588, 'out_node': 2}, 15: {'enable_bit': 1, 'in_node': 6, 'weight': 0.7288641247892953, 'out_node': 8}}


build = NetworkBuilder(nodes, connections)
