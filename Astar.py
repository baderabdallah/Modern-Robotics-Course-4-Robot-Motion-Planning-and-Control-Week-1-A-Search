import numpy as np
from numpy import genfromtxt
import os

class node:
    def __init__(self, order, x, y, heuristicCostToGo):
        self.order = int(order)
        self.x = float(x)
        self.y = float(y)
        self.heuristicCostToGo = float(heuristicCostToGo)

nodesFileName = os.getcwdb()
nodesFileName = nodesFileName.decode("utf-8")+u'\\Scene5_example\\nodes.csv'

nodes = genfromtxt(nodesFileName, delimiter=',')

edgesFileName = os.getcwdb()
edgesFileName = edgesFileName.decode("utf-8")+u'\\Scene5_example\\edges.csv'

edges = genfromtxt(edgesFileName, delimiter=',')

nodeList = list()
for eachNode in nodes:
    n = node(eachNode[0],eachNode[1],eachNode[2],eachNode[3])
    nodeList.append(n)


for i in nodeList:
    print(i.order, i.x, i.y, i.heuristicCostToGo)
