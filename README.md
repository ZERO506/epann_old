# epann
## Evolutionary Plastic Artificial Neural Networks

***A Python package for implementing Compositional Pattern Producing Network (CPPN) variants for indirectly encoding artificial neural networks.***


More and more scientists are applying deep neural networks to their data problems every day. Usually, the factors that determine the characteristics of that network are largely based on their own expertise, and their ability to alter available deep learning software to fit the needs of their data. In general, however, it may not be clear without significant experience the criteria by which one network architecture is appropriate.

In order to address this problem, the field of neuroevolution has strove to design representations of neural network architectures, in an attempt to create systems that automatically determine the model that would provide good performance by some measure. The field itself takes inspiration from biology - biological neural networks are a product of not only within-generation learning but also development and evolution. Natural selection determines classes of solutions that persist in a particular niche, and development and learning does what it can with those initial conditions. 

When applying this perspective to the design of artificial neural networks, that is, that a particular deep learning model exists as one solution in a space of all possible solutions, its location within that space is entirely dependent on what we choose as an effective representation for that solution.

Early in the field, it was common to represent an artificial neural network with a string of bits, where each gene in this bitstring genome represented the individual weights for each connection in the final network, an approach referred to as *direct encoding*. This approach quickly was seen as problematic as larger models with many more parameters were needed to solve more complex problems. As the sizes of these solutions grow, their genomes would also have to grow at the same rate. In some of the largest convolutional neural networks, over a million weights and associated parameters would have to be represented by a string of over a million numbers. This N-dimensional space of possible genomes would become entirely unfeasible to explore. 

With this problem in mind, there have been numerous attempts to develop *indirect encodings* of artificial neural networks which exploit the regularity in a particular model to compress it's representation to some set of parameters M << N.
