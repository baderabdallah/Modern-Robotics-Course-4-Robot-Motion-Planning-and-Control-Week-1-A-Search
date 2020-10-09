import numpy as np
from numpy import genfromtxt
import os

class node:
    def __init__(self, order, x, y, heuristicCostToGo):
        self.order = int(order)
        self.x = float(x)
        self.y = float(y)
        self.heuristicCostToGo = float(heuristicCostToGo)
        self.childNode = list()
        
    def __repr__(self):
        return 'Node({},{},{},{})'.format(self.order,
                                         self.x,
                                         self.y,
                                         self.heuristicCostToGo)

nodesFileName = os.getcwdb()
nodesFileName = nodesFileName.decode("utf-8")+u'\\Scene5_example\\nodes.csv'
nodes = genfromtxt(nodesFileName, delimiter=',')

nodeList = list()
for eachNode in nodes:
    n = node(eachNode[0],eachNode[1],eachNode[2],eachNode[3])
    nodeList.append(n)

class edge: 
    def __init__(self, childNodeId, parentNodeId, cost):
        self.childNodeId = int(childNodeId)
        self.parentNodeId = int(parentNodeId)
        self.cost = float(cost)

edgesFileName = os.getcwdb()
edgesFileName = edgesFileName.decode("utf-8")+u'\\Scene5_example\\edges.csv'
edges = genfromtxt(edgesFileName, delimiter=',')

edgeList = list()
for eachEdge in edges:
    m = edge(eachEdge[0], eachEdge[1], eachEdge[2])
    edgeList.append(m)

for eachEdge in edgeList:
    nodeList[eachEdge.parentNodeId-1].childNode.append(nodeList[eachEdge.childNodeId-1])

initialPastCostList = [0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

heuristicCostToGoList = list()
for node in nodeList:
    heuristicCostToGoList.append(node.heuristicCostToGo)

pastCostList = initialPastCostList
estTotalCost = pastCostList + heuristicCostToGoList

parentNodesList = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

openNodeList = list()

closedNodeList = list()

for i in nodeList:
    print(i.order, i.x, i.y, i.heuristicCostToGo)
    