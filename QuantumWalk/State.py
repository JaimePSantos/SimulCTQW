import numpy as np

class State:
    def __init__(self,n,markedList):
        self._stateMat = np.zeros((n,1))
        for marked in markedList:
            self._stateMat[marked] = 1/np.sqrt(len(markedList))

    def __mul__(self,other):
        return self._stateMat*other

    def __rmul__(self,other):
        return other*self._stateMat

    def getState(self):
        return self._stateMat

    def setState(self,newState):
        self._stateMat = newState