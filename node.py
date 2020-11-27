from numpy import genfromtxt
import os
import csv

class Node:
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
    @staticmethod
    def parse_nodes_data(nodesFileName):
        nodeList=list()
        nodesData = genfromtxt(nodesFileName, delimiter=',')
        for eachNode in nodesData:
            n = Node(eachNode[0],eachNode[1],eachNode[2],eachNode[3])
            nodeList.append(n)
        return nodeList
    @staticmethod
    def write_closed_node_list(closedNodeListFileName, closedNodeList):
        path = list()
        for node in closedNodeList:
            path.append(node.openNode.order)
        path_folder = os.path.abspath(closedNodeListFileName)

        with open(path_folder, 'w', newline='') as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(path)
            
    @staticmethod
    def add_children_nodes_to_nodeList(nodeList, edgeList):
        for eachEdge in edgeList:
            #Child nodes
            parentNode =  nodeList[eachEdge.parentNodeId-1]
            childNode = nodeList[eachEdge.childNodeId-1]
            parentNode.childNode.append(childNode)
            #Child costs.
            parentNode.childCost.append(eachEdge.cost)