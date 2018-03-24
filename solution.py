#!/usr/bin/env python3

import sys, os
import copy
from functools import reduce
import json

class Vertex:

    """
        Vertex implementation for each possible step from initial configuration
    """
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr):
        self.connectedTo[nbr] = 0

    def getConnections(self):
        return self.connectedTo.keys()


class Graph:
    """
        Graph implementation for all the possible steps and their connections(subsequent steps)
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None


    def addEdge(self,f,t):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(t)



class StepGenerator:
    """
        Generates all possible steps from the initial conf by making one change at a time.
        The steps are added to the graph such that the final graph has all possible steps and 
        their connections

        This graph is used to find a path from initial conf to final conf.
        Since there are multiple paths possible, the obtained path can be 
        minimized further by finding farthest neighbour to each node and eliminating
        intermediate steps.
    """
    def __init__(self, capacity, initial_conf, final_conf, g):

        self.capacity = capacity
        self.initial = initial_conf
        self.final = final_conf 
        self.graph = g
        self.graph.addVertex(initial_conf)
        self.found = False
        self.path = []


    def step(self, initial):

        diff = tuple(x - y for x,y in zip(self.capacity, initial))

        new_node = False
        for i in range(len(diff)):
            for j in range(len(initial)):
                step = list(copy.deepcopy(initial))
                if i != j:
                    if diff[i] <= initial[j]:
                        step[i] = self.capacity[i]
                        step[j] = initial[j] - diff[i]

                    else:
                        step[i] += initial[j]
                        step[j] = 0
                step_tuple = tuple(step)
                if step_tuple not in self.graph.vertList:
                    self.graph.addVertex(step_tuple)
                    # self.graph.addEdge(initial, step_tuple)
                    if step_tuple == self.final:
                        self.found = True
                    else:
                        self.step(step_tuple)
                    new_node = True
                self.graph.addEdge(initial, step_tuple)

        if new_node == False:
            return

    def find_path(self, node, visited):
        
        if node == self.final:
            self.path.append(node)
            return True
        if self.final in self.path:
            return True
        elif node not in visited:
            visited.append(node)
            nbr = self.graph.getVertex(node).getConnections()
            if all([z in visited for z in nbr]) and self.final not in self.path:
                self.path.pop()
                return False
            else:
                for n in list(set(nbr).difference(set(visited))):
                    self.path.append(node)
                    result = self.find_path(n, visited)
                    if not result:
                        self.path.pop()
                    return result


    def minimize_steps(self, minpath):
        node = minpath[-1]
        if node == self.final:
            return minpath
        nbr = list(self.graph.getVertex(node).getConnections())
        next = None
        for item in self.path:
            if item in nbr:
                next = item

        minpath.append(next)
        return self.minimize_steps(minpath)


class MainEntry:

    """
        Takes the input configurations, validates them and calls the sequence of
        procedures to find the path for valid inputs
    """

    def process_input(self, capacity, initial, final):
        if len(initial) != len(capacity) or len(final)\
            != len(capacity):
            raise ValueError("Initial and final configurations should be same length as capacity")

        for i in range(len(capacity)):
            if capacity[i] < initial[i] or capacity[i]\
                < final[i]:
                raise ValueError("Capacity of vessel cannot be exceeded in initial and final conf")

            if capacity[i] < 0 or initial[i] < 0 or \
                final[i] < 0:
                raise ValueError("Any state cannot have a negative value")

        adder = lambda x,y:x+y
        if reduce(adder, initial) != reduce(adder, final):
            raise ValueError("Total of initial and final configuration should be same")

        g = Graph()
        s = StepGenerator(capacity, initial, final, g)
        s.step(initial)
        if s.found:
            s.find_path(initial, [])
            return(s.minimize_steps([initial]))
        else:
            return("Not possible")


if __name__ == "__main__":
    capacity = eval(input("Enter capacity:"))
    initial_conf = eval(input("Enter initial_conf:"))
    final_conf = eval(input("Enter final conf:"))

    instance = MainEntry()
    try:
        result = instance.process_input(capacity, initial_conf, final_conf)
    except ValueError as ve:
        sys.exit(ve)

    print("Result: ", result)




