import numpy as np
from numpy import genfromtxt
import os
from operator import add

class node:
    def __init__(self, order, x, y, heuristicCostToGo):
        self.order = int(order)
        self.x = float(x)
        self.y = float(y)
        self.heuristicCostToGo = float(heuristicCostToGo)
        self.childNode = list()
        self.childCost = list()
        
    def __repr__(self):
        return 'Node({},{},{},{})'.format(self.order,
                                         self.x,
                                         self.y,
                                         self.heuristicCostToGo)

nodesFileName = os.getcwdb()
nodesFileName = nodesFileName.decode("utf-8")+u'\\Scene5_example\\nodes.csv'
nodesData = genfromtxt(nodesFileName, delimiter=',')

nodeList = list()
for eachNode in nodesData:
    n = node(eachNode[0],eachNode[1],eachNode[2],eachNode[3])
    nodeList.append(n)

class edge: 
    def __init__(self, childNodeId, parentNodeId, cost):
        self.childNodeId = int(childNodeId)
        self.parentNodeId = int(parentNodeId)
        self.cost = float(cost)

edgesFileName = os.getcwdb()
edgesFileName = edgesFileName.decode("utf-8")+u'\\Scene5_example\\edges.csv'
edgesData = genfromtxt(edgesFileName, delimiter=',')

edgeList = list()
for eachEdge in edgesData:
    m = edge(eachEdge[0], eachEdge[1], eachEdge[2])
    edgeList.append(m)

## Append child nodes and their CostsToGo to their parent nodes.
for eachEdge in edgeList:
    #Child nodes
    parentNode =  nodeList[eachEdge.parentNodeId-1]
    childNode = nodeList[eachEdge.childNodeId-1]
    parentNode.childNode.append(childNode)
    #Child costs.
    parentNode.childCost.append(eachEdge.cost)


class openListItem:
    def __init__(self, openNode, nodeEstTotCost):
        self.openNode = openNode
        self.nodeEstTotCost = nodeEstTotCost
    def __repr__(self):
            return 'OpenNode({},{})'.format(self.openNode.order,
                                            self.nodeEstTotCost)

closedNodeList = list()

initialPastCostList = [0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

heuristicCostToGoList = list()
for node in nodeList:
    heuristicCostToGoList.append(node.heuristicCostToGo)
estTotalCost = list()
pastCostList = initialPastCostList
estTotalCost = list( map(add, pastCostList, heuristicCostToGoList) )

parentNodesList = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
openNodeList = list()

openNodeList.append(openListItem(nodeList[0],
                    estTotalCost[0]))
print(openNodeList[0].openNode,openNodeList[0].openNode.childNode )

count = 0
for eachChild in openNodeList[0].openNode.childNode:
    parentNodesList[eachChild.order - 1] = openNodeList[0].openNode.order
    cost = openNodeList[0].openNode.childCost[count]
    pastCostList[eachChild.order - 1] = cost  
    estTotalCost = list (map(add, pastCostList, heuristicCostToGoList))
    openNodeList.append(openListItem(eachChild, estTotalCost[eachChild.order-1]))
    count = count + 1


for i in nodeList:
    print(i.order, i.x, i.y, i.heuristicCostToGo)
    if i.childNode:
        print(i.childNode)

print(openNodeList)
print(estTotalCost)