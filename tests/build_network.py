

import numpy as np

num_inputs = 144
num_outputs = 3

if num_inputs > 5:
    coords = np.random.randn(1, num_inputs)
else:
    coords = np.array([-1., 0., 0., 0., 1.])[np.newaxis, :]

# ----- Time = 0

weights = np.random.randn(num_inputs, num_outputs)

check0 = np.dot(coords, weights)
print check0

# ----- Time = 1

w_0 = np.zeros((num_inputs, num_inputs*num_outputs))
id = np.zeros((num_inputs*num_outputs, num_outputs))

for input in range(num_inputs):
    w_0[input, num_outputs * input:num_outputs * input + num_outputs] = weights[input, :]
    id[num_outputs*input:num_outputs*input+num_outputs, :] = np.identity(num_outputs)

check1 = np.dot(np.dot(coords, w_0), id)
print check1

# ----- Time = 2

id0 = np.identity(num_inputs*num_outputs)
check2 = np.dot( np.dot(np.dot(coords, w_0), id0), id )
print check2





