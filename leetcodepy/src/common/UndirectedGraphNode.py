'''
Created on Oct 15, 2015

@author: mianmianba
'''

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []
