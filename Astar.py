import numpy as np
from numpy import genfromtxt
import os


nodesFileName = os.getcwdb()
nodesFileName = nodesFileName.decode("utf-8")+u'\\Scene5_example\\nodes.csv'

nodes = genfromtxt(nodesFileName, delimiter=',')

edgesFileName = os.getcwdb()
edgesFileName = edgesFileName.decode("utf-8")+u'\\Scene5_example\\edges.csv'

edges = genfromtxt(edgesFileName, delimiter=',')

print (nodes)
print (edges)
