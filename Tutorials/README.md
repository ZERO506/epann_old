# epann
## Evolutionary Plastic Artificial Neural Networks

***A Python package for implementing Compositional Pattern Producing Network (CPPN) variants for indirectly encoding artificial neural networks.***

- Purpose:
1. Greater understanding of the HyperNEAT algorithm and indirect encoding variants for evolving a populations of neural networks.
2. Practice in package management.
3. General purpose research pipeline for appyling EPANN neuroevolution techniques to a variety of environments.
4. Genomes create *plastic* ANNs that learn within the generation. Genome reflects features of that learning that can be altered during evolution.

- Example:
Currently, the file example.py will create a population of Compositional Pattern Producing Networks (CPPNs), randomly generate an evaluation for each agent, and perform cross-over and mutation within each species wrt that fitness. Output: Node & connection genomes for an agent in the first generation, followed by the updated node & connection genomes for that same agent in the final generation. 

*Clone the repository and run: *    python example.py


- Details:
As deep learning becomes more essential for building solutions to machine learning problems, it becomes clear that a broader definition of solution characteristics required for a kind of task is needed, such that model selection and discovery is better optimized for future problems. Likewise, as deep learning has been inspired by the study of biological nervous systems, theoretical neuroscience can benefit from this context in the development of better theories of biological neural networks. 

A solution ( either a machine learning model or a biological nervous systems ) requires a representation to define their location in the space of possible solutions. The field of *neuroevolution* approaches this problem of evolving neural networks, and the representations chosen can be classified into on of two classes. *Direct encodings* represent the parameters of a solution directly - that is, every parameter (i.e. ANN connection weight) is represented with a single gene in the genome representation of that solution. The problem with representations that fall within this class is that as the number of parameters grows, as in the millions of weights that describe a convolutional neural network trained on ImageNet classes, its representation as a solution would require just as many genes as there are parameters. With this representation, an effective solution is a single point that must be discovered within a space of solutions with millions of dimensions. As the number of parameters grows, direct encodings make solution discovery infeasible. 

Ideally, we would like to be able to compress a solution into a representation that has significantly less components than the number of parameters in the model solution it represents. The *Indirect encoding* class of solution representations (genomes) that accomplishes this in different ways, though usually parameter compression is possible by leveraging regularity of the connectivity in a solution. 

While this package has goals of including many different indirect encoding methods, at this point it focuses primarily on the Hyper-NEAT family of algorithms, which comes from the original implementation of Kenneth Stanley. Specifically, since it is the goal to apply these algorithms to many different kinds of environments and tasks (especially those available within the OpenAIGym and Universe packages), this package focuses on the **adaptiveES-HyperNEAT algorithm**. 

# adaptiveES-HyperNEAT algorithm
First introduced in [?], adaptiveES-HyperNEAT solved an important problem in the original implementations of HyperNEAT, namely the characteristics of a transformation between a genome and hidden node locations in the final phenotype. This will be addressed more specifically below. 

The algorithm has four different parts that reflect major changes in representing the genome of a neural network indirectly. 

1. NEAT - The NEAT algorithm [?] was developed by Kenneth Stanley as a method for evolving neural networks (NeuroEvolution of Augmenting Topologies). NEAT, though in this form remained an example of a *direct encoding* strategy, provided major stepping stones toward the *indirect* techniques used in this package. A population is defined as a collection of simple neural networks with a certain number of input and ouput nodes (representing control sensor and effectors) fully-connected without any hidden nodes. That way, individual solutions differ from the others in a population only by the weights of these connections. 



blah

