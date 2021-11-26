class Hamiltonian:
    def __init__(self,graph):
        self._graph = graph
        self._ham = self._graph.adjacency_matrix()

    def __mul__(self,other):
        print("Hello")
        return self._ham*other

    def __rmul__(self,other):
        return other*self._ham

    def setHam(self,newGraph):
        self._graph = newGraph
        self._ham = self._graph.adjacency_matrix()

    def getHam(self):
        return self._ham