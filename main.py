# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

from QuantumWalk.State import State
from QuantumWalk.graphs import Graph
from QuantumWalk.Hamiltonian import Hamiltonian
from QuantumWalk.Operator import Operator
from QuantumWalk.QuantumWalk import QuantumWalk


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 5
    t=1
    gamma=1
    marked = [int(n/2)]
    initState = State(n,marked)
    initState.buildState()
    print(initState.getState())

    graph = Graph({}).linegraph(n)
    # print(graph)

    hamilt = Hamiltonian(n,graph)
    hamilt.buildHam()
    print(hamilt.getHam())
    # hamilt.setHam(graph)
    # print(hamilt.getHam())

    # op = Operator(hamilt,t,gamma)
    # # print(op.getOperator())
    #
    # walk = QuantumWalk(initState,op).getWalk()
    # # print(walk.getWalk())
    #
    # probs = np.zeros((n,1))
    # for x in range(n):
    #     probs[x]=walk[x]*np.conjugate(walk[x])
    # print(probs)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
