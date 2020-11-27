
class OpenListItem:
    def __init__(self, openNode, nodeEstTotCost):
        self.openNode = openNode
        self.nodeEstTotCost = nodeEstTotCost
    def __repr__(self):
            return 'OpenNode({},{})'.format(self.openNode.order,
                                            self.nodeEstTotCost)
