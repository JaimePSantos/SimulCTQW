import numpy as np

class State:
    def __init__(self,N,nList):
        self.stateMat = np.zeros((N,1))
        for n in nList:
            self.stateMat[n] = 1/np.sqrt(len(nList))

    def getState(self):
        return self.stateMat

    def setState(self,newState):
        self.stateMat = newState

    def transformState(self,operator):
        self.stateMat = np.dot(operator,self.stateMat)