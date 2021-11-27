import numpy as np


class State:
    def __init__(self, n, stateList=None):
        self._n = n
        self._stateMat = np.zeros((self._n, 1))
        if stateList is not None:
            self._stateList = stateList

    def __mul__(self, other):
        return self._stateMat * other

    def __rmul__(self, other):
        return other * self._stateMat

    def buildState(self):
        for state in self._stateList:
            self._stateMat[state] = 1 / np.sqrt(len(self._stateList))

    def getState(self):
        return self._stateMat

    def setState(self, newState):
        self._stateMat = newState

    def setDim(self,newN):
        self._n = newN

    def getDim(self,newN):
        return self._n

    def setStateList(self,newStateList):
        self._stateList = newStateList

    def getStateList(self):
        return self._stateList