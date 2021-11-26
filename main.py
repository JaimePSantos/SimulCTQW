# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from QuantumWalk.State import State
from QuantumWalk.graphs import Graph
from QuantumWalk.Hamiltonian import Hamiltonian
from QuantumWalk.Operator import Operator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 10
    t=1
    gamma=1
    marked = [int(n/2)]
    state = State(n,marked)
    print(state.getState())

    graph = Graph({}).linegraph(n)

    hamilt = Hamiltonian(graph)
    hamilt.setHam(graph)
    print(hamilt.getHam())

    op = Operator(hamilt,t,gamma)
    print(op.getOperator())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
