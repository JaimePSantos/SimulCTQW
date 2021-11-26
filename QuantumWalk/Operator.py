from scipy import linalg

class Operator:
    def __init__(self,ham,time=None,gamma=None):
        self._ham = ham
        if(time is None):
            self._time = 0
        elif(gamma is None):
            self._gamma = 1
        else:
            self._time = time
            self._gamma = gamma
        self._operator = linalg.expm(-1j*self._gamma*self._ham*self._time)

    def setOperator(self,newHam,newTime = None, newGamma = None):
        self._ham = newHam
        if(newTime is None):
            self._time = 0
        elif(newGamma is None):
            self._gamma = 1
        else:
            self._time = newTime
            self._gamma = newGamma
        self._operator = linalg.expm(-1j*self._gamma*self._ham*self._time)

    def getOperator(self):
        return self._operator