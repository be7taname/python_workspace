'''
Created on Sep 12, 2015

@author: mianmianba
'''

from common.TreeNode import TreeNode

class RightSideView(object):
    def solution(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rsvv = []
        if root == None: return rsvv
        treeQ = [root]
        curMostRightNode = root
        nxtMostRightNode = None
        while treeQ:
            thisNode = treeQ.pop(0)
            if thisNode.left != None: 
                treeQ.append(thisNode.left)
                nxtMostRightNode = thisNode.left
            if thisNode.right != None: 
                treeQ.append(thisNode.right)
                nxtMostRightNode = thisNode.right
            if thisNode == curMostRightNode:
                rsvv.append(curMostRightNode.val)
                curMostRightNode = nxtMostRightNode
        return rsvv
    