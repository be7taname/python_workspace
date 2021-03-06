'''
Created on Oct 5, 2015

@author: mianmianba
'''

class CountNodes(object):
    def getRightNodes(self, root, rightLevel):
        leftLevel = 0
        curNode = root
        while curNode.left != None:
            leftLevel += 1
            curNode = curNode.left
        if leftLevel == rightLevel: return (1<<(leftLevel+1))-1
        else:
            if leftLevel == 1: return 2
            else:
                numLeftNodes = self.getLeftNodes(root.left, leftLevel-1)
                numRightNodes = self.getRightNodes(root.right, rightLevel-1)
                return numLeftNodes + numRightNodes + 1
        
    def getLeftNodes(self, root, leftLevel):
        rightLevel = 0
        curNode = root
        while curNode.right != None:
            rightLevel += 1
            curNode = curNode.right
        if leftLevel == rightLevel: return (1<<(leftLevel+1))-1
        else:
            if leftLevel == 1: return 2
            else:
                numLeftNodes = self.getLeftNodes(root.left, leftLevel-1)
                numRightNodes = self.getRightNodes(root.right, rightLevel-1)
                return numLeftNodes + numRightNodes + 1
        
    def solutionTwo(self, root):
        if root == None: return 0
        else:
            leftLevel = 0
            curNode = root
            while curNode.left != None:
                leftLevel += 1
                curNode = curNode.left
            rightLevel = 0
            curNode = root
            while curNode.right != None:
                rightLevel += 1
                curNode = curNode.right
            if leftLevel == rightLevel: return (1<<(leftLevel+1))-1
            else:
                if leftLevel == 1: return 2
                else:
                    numLeftNodes = self.getLeftNodes(root.left, leftLevel-1)
                    numRightNodes = self.getRightNodes(root.right, rightLevel-1)
                    return numLeftNodes + numRightNodes + 1
            
    def cntLevel(self, root):
        if root.left == None:
            return (0, 1, True)
        else:
            (leftLevel, leftNodes, leftComp) = self.cntLevel(root.left)
            if leftComp == False:
                return (leftLevel+1, leftNodes, False)
            else:
                if root.right == None:
                    return (leftLevel+1, leftNodes, False)
                else:
                    (rightLevel, rightNodes, rightComp) = self.cntLevel(root.right)
                    if rightLevel < leftLevel:
                        return (leftLevel+1, leftNodes, False)
                    elif rightComp == True:
                        return (leftLevel+1, leftNodes+rightNodes, True)
                    else:
                        return (leftLevel+1, leftNodes+rightNodes, False)
        
    def solution(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        (level, nodes, comp) = self.cntLevel(root)
        return (1<<level) - 1 + nodes
    