from numpy import genfromtxt
import os


class Edge:
    def __init__(self, childNodeId, parentNodeId, cost):
        self.childNodeId = int(childNodeId)
        self.parentNodeId = int(parentNodeId)
        self.cost = float(cost)

    @staticmethod
    def parse_edge_data(edgesFileName):
        edgeList = list()
        edgesData = genfromtxt(edgesFileName, delimiter=',')
        for eachEdge in edgesData:
            m = Edge(eachEdge[0], eachEdge[1], eachEdge[2])
            edgeList.append(m)
        return edgeList
