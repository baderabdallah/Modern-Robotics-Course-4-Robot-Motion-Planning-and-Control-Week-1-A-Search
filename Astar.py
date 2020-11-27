import numpy as np
import os
from operator import add
from pathlib import Path
from node import Node 
from edge import Edge
from openListItem import OpenListItem


if __name__ == "__main__":
    #Lists decleration
    nodeList = list()
    edgeList = list()

    #openNodeList is updated throught the A* algorithm
    openNodeList = list()
    #closedNodeList is the final soltuion of the A* algorithm
    closedNodeList = list()

    #Usually when the algorithm is done by hand those four lists are the four rows
    pastCostList = list()
    parentNodesList = list()
    heuristicCostToGoList = list()
    estTotalCost = list()

    #Parsing information about the nodes
    nodesFileName = os.getcwdb()
    nodesFileName = nodesFileName.decode("utf-8")+u'\\Scene5_example\\nodes.csv'
    nodeList = Node.parse_nodes_data(nodesFileName)

    #initializing the goal node as the last node from the nodeList
    goalNode = nodeList[-1]

    #Parsing information about the edges
    edgesFileName = os.getcwdb()
    edgesFileName = edgesFileName.decode("utf-8")+u'\\Scene5_example\\edges.csv'
    edgeList = Edge.parse_edge_data(edgesFileName)

    #Definition of the lists that are the attributes of the algorithm i.e. final path = f(parentNodeList, pastCostList, heuCostList, estTotalCost)
    parentNodesList = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    pastCostList = [0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    for node in nodeList:
        heuristicCostToGoList.append(node.heuristicCostToGo)
    estTotalCost = list( map(add, pastCostList, heuristicCostToGoList) )

    #Extracting children information for each parent from edgeList, and connecting the children to their parents in nodeList
    Node.add_children_nodes_to_nodeList(nodeList, edgeList)

    #A* algorithm starts following the psudo code from the course
    
    #First node is appended
    openNodeList.append(OpenListItem(nodeList[0],
                        estTotalCost[0]))
    
    #Go on if open list is not empty!
    while not(len(openNodeList) == 0):
        count = 0
        current = openNodeList[0]

        #add first node in the open list to the closed list
        closedNodeList.append(current)

        #Break out of loop if goal is reached!
        if current.openNode.order == goalNode.order:
            break

        #first node was added to closed list. it is not need now in the open list.
        openNodeList.pop(0)

        #follow the algorithm and produce the open list sorted in increasing order of total estimated cost.
        for eachChild in current.openNode.childNode:
            parentNodesList[eachChild.order - 1] = current.openNode.order
            cost = current.openNode.childCost[count]
            pastCostList[eachChild.order - 1] = cost  
            estTotalCost = list (map(add, pastCostList, heuristicCostToGoList))
            if not any(x.openNode == eachChild for x in closedNodeList):
                if any(x.openNode.order == eachChild.order for x in openNodeList):
                    popOut = next((x for x in openNodeList if x.openNode.order == eachChild.order), None)
                    openNodeList.pop(openNodeList.index(popOut))
                    openNodeList.append(OpenListItem(eachChild, estTotalCost[eachChild.order-1]))
                else:
                    openNodeList.append(OpenListItem(eachChild, estTotalCost[eachChild.order-1]))

            count = count + 1
        openNodeList.sort(key=lambda x: x.nodeEstTotCost, reverse=False)
        #Go back to the start of the loop to add the first element of the open list into the closed list

    #Algorithm is done! Now write the solution path into disk
    closedNodeListFileName = "Scene5_example/path.csv"
    Node.write_closed_node_list(closedNodeListFileName, closedNodeList)
