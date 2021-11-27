import numpy as np


class State:
    def __init__(self, n, stateList=None):
        self._n = n
        self._stateMat = np.zeros((self._n, 1))
        self._stateList = None
        if stateList is not None:
            self._stateList = stateList

    def __mul__(self, other):
        return self._stateMat * other

    def __rmul__(self, other):
        return other * self._stateMat

    def buildState(self):
        if self._stateList is not None:
            for state in self._stateList:
                self._stateMat[state] = 1 / np.sqrt(len(self._stateList))

    def setDim(self,newN):
        self._n = newN

    def getDim(self):
        return self._n

    def setStateList(self,newState):
        self._stateList = newState

    def getStateList(self):
        return self._stateList

    def setState(self, newState):
        self._n = newState.getDim()
        self._stateList = newState.getStateList()
        self._stateMat = newState.getState()

    def getState(self):
        return self._stateMat