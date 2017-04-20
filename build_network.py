

import numpy as np

num_inputs = 3
num_outputs = 2

# Time = 0

weights = np.random.randn(num_inputs, num_outputs)
w_0 = np.zeros((num_inputs, num_inputs*num_outputs))
id = np.zeros((num_inputs*num_outputs, num_outputs))

for input in range(num_inputs):
    w_0[input, 2*input:2**(input+1)] = weights[input, :]
    id[2*input:2*input+2, :] = np.identity(2)

print w_0
print id

check = np.dot(w_0, id)
print weights
print check


# 0 - 00, 11
# 1 - 20, 31
# 2 - 40, 51

# test = np.arange(num_inputs*num_inputs*num_outputs).reshape(num_inputs, num_inputs*num_outputs)
# print test
# for input in range(num_inputs):
#     print test[input, 2*input:2**(input+1)]


# Time = 1



# # Time = 1
#
# print '\nTime 1\n'
#
# a, b = np.diagflat(weights), np.ones((weights.shape[0], weights.shape[1]))
# print 'W:\n', weights
#
# print 'W1:\n', b
# print 'W0:\n', a
#
# test = np.dot(a, b)
# print 'test:\n',test
# print 'W\n', weights
#
# # Time = 2a
#
# print '\nTime 2a\n'
#
# c, d = np.diagflat(b), np.ones((b.shape[0], b.shape[1]))
#
# print 'W2:\n', d
# print 'W1:\n', c
# print 'W0:\n', a
#
# test = np.dot(a, np.dot(c, d))
# print 'test:\n',test
# print 'W\n', weights
#
# # Time = 2a
#
# print '\nTime 2b\n'
#
# e, f = a, np.identity(a.shape[0])
#
# print 'W2:\n', b
# print 'W1:\n', f
# print 'W0:\n', e
#
# test = np.dot(e, np.dot(f, b))
# print 'test:\n',test
# print 'W\n', weights

