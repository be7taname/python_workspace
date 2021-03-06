'''
Created on Sep 6, 2015

@author: mianmianba
'''

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from TreeNode import TreeNode

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.treeStack = []
        if root == None: return
        self.treeStack.append(root)
        thisNode = root
        while thisNode.left != None:
            thisNode = thisNode.left
            self.treeStack.append(thisNode)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.treeStack) != 0
        
    def next(self):
        """
        :rtype: int
        """
        thisNode = self.treeStack.pop()
        curNode = thisNode.right
        while curNode != None:
            self.treeStack.append(curNode)
            curNode = curNode.left
        return thisNode.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())