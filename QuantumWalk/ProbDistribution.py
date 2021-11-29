import numpy as np


class ProbDistribution:
    def __init__(self,state):
        self._n = state.getDim()
        self._stateMat = state.getState()
        self._probVec = np.zeros((self._n, 1))

