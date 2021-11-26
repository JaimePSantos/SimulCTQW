import numpy as np

class State:
    def __init__(self,n,markedList):
        self.stateMat = np.zeros((n,1))
        for marked in markedList:
            self.stateMat[marked] = 1/np.sqrt(len(markedList))

    def getState(self):
        return self.stateMat

    def setState(self,newState):
        self.stateMat = newState

    def transformState(self,operator):
        self.stateMat = np.dot(operator,self.stateMat)