'''
Created on Sep 27, 2015

@author: mianmianba
'''

class IsValidBST(object):
    def solutions(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        if root.left == None and root.right == None:
            return True
        if root.left != None:
            (leftFlag, leftMin, leftMax) = self.MaxOrInvalid(root.left)
            if leftFlag == False: return False
            if leftMax >= root.val: return False
        if root.right != None:
            (rightFlag, rightMin, rightMax) = self.MaxOrInvalid(root.right)
            if rightFlag == False: return False
            if rightMin <= root.val: return False
        return True
        
    def MaxOrInvalid(self, root):
        if root.left == None and root.right == None:
            return (True, root.val, root.val)
        minVal, maxVal = root.val, root.val
        if root.left != None:
            (leftFlag, leftMin, leftMax) = self.MaxOrInvalid(root.left)
            if leftFlag == False: return (False, 0, 0)
            if leftMax >= root.val: return (False, 0, 0)
            minVal = leftMin
        if root.right != None:
            (rightFlag, rightMin, rightMax) = self.MaxOrInvalid(root.right)
            if rightFlag == False: return (False, 0, 0)
            if rightMin <= root.val: return (False, 0, 0)
            maxVal = rightMax
        return (True, minVal, maxVal)
    
        