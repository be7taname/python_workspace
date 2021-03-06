'''
Created on Oct 22, 2015

@author: mianmianba
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.TreeNode import TreeNode
class ZigzagLevelOrder(object):
    def solution(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None: return res
        treeStack = [root]
        nxtLastNode = None
        lastNode = root
        thisRes = []
        direction = 1
        while treeStack:
            curNode = treeStack.pop(0)
            thisRes.append(curNode.val)
            if curNode.left:
                treeStack.append(curNode.left)
                nxtLastNode = curNode.left
            if curNode.right:
                treeStack.append(curNode.right)
                nxtLastNode = curNode.right
            if curNode == lastNode:
                if direction == 1:
                    res.append(thisRes)
                elif direction == 0:
                    res.append(thisRes[::-1])
                lastNode = nxtLastNode
                thisRes = []
                direction ^= 1
        return res
                    