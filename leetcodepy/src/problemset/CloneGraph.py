'''
Created on Oct 15, 2015

@author: mianmianba
'''

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from common.UndirectedGraphNode import UndirectedGraphNode

class CloneGraph(object):
    def solution(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None: return None
        nodeStack = [node]
        anode = UndirectedGraphNode(node.label)
        gmap = {node: anode}
        while nodeStack:
            oldNode = nodeStack.pop()
            newNode = gmap[oldNode]
            for aoldnode in oldNode.neighbors:
                if aoldnode in gmap:
                    anewnode = gmap[aoldnode]
                else:
                    anewnode = UndirectedGraphNode(aoldnode.label)
                    gmap[aoldnode] = anewnode
                    nodeStack.append(aoldnode)
                newNode.neighbors.append(anewnode)
        return gmap[node]
    
            