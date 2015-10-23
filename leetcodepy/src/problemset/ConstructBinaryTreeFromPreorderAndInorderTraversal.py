'''
Created on Oct 21, 2015

@author: mianmianba
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common.TreeNode import TreeNode
class BuildTree(object):
    def solutionMem(self, preorder, inorder):
        return self.AddTreeNode(preorder, 0, len(preorder), inorder, 0, len(inorder))
    
    def AddTreeNode(self, preorder, prestart, preend, inorder, instart, inend):
        nodesLen = preend - prestart
        if nodesLen == 0: return None
        elif nodesLen == 1: return TreeNode(preorder[prestart])
        root = TreeNode(preorder[prestart])
        rootIdx = inorder.index(preorder[prestart]) - instart
        root.left = self.AddTreeNode(preorder, prestart+1, prestart+rootIdx+1, inorder, instart, instart+rootIdx)
        root.right = self.AddTreeNode(preorder, prestart+rootIdx+1, preend, inorder, instart+rootIdx+1, inend)
        return root
        
    def solution(self, preorder, inorder): # not memory efficient since every recursive created new preorder/inorder lists
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        nodeLen = len(preorder)
        if nodeLen == 0: return None
        elif nodeLen == 1: return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        for rootIdx in range(nodeLen):
            if inorder[rootIdx] == preorder[0]: break
        root.left = self.solution(preorder[1:rootIdx+1], inorder[:rootIdx])
        root.right = self.solution(preorder[rootIdx+1:], inorder[rootIdx+1:])
        return root
    
        