from stack import Stack
from data_persistence import *
from memory_profiler import profile
import time
import sys


# Stack initialization

# Push first element

@profile
def insert_nodes(stack):
    for i in range(1000):
        stack.push('CULO')
    return stack

"""
@profile
def traverse(ll):
    tiempo = time.time()
    for node in ll:
        pass
    tiempo1 = time.time()
    total = tiempo1-tiempo
    print("Tardo ", total ,'segundos sin el pickle')
"""

def pickleit(playlist, name):
    pickle_object(playlist, name)
    tiempo = time.time()
    tiempo1 = time.time()
    total = tiempo1-tiempo
    print("El tiempo que tardo con pickle rick ", total )

@profile
def main():
    stack = Stack(13200000)
    stack = insert_nodes(stack)
    sys.setrecursionlimit(10000000)
    pickleit(stack,'messi')
    # guardar en pickle

main()

