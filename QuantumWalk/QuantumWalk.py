import numpy as np

class QuantumWalk:
    def __init__(self,state,operator):
        self._state = state.getState()
        self._operator = operator.getOperator()
        self._finalState = np.dot(self._operator,self._state)

    def setWalk(self,state,operator):
        self._state = state.getState()
        self._operator = operator.getOperator()
        self._finalState = np.dot(self._operator,self._state)

    def getWalk(self):
        return self._finalState