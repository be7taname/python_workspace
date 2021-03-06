'''
Created on Sep 19, 2015

@author: mianmianba
'''

from common.TreeNode import TreeNode
class SortedArrayToBST(object):
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        numsLen = len(nums)
        if numsLen == 0:
            return None
        elif numsLen == 1:
            return TreeNode(nums[0])
        else:
            root = TreeNode(nums[numsLen/2])
            root.left = self.solution(nums[:numsLen/2])
            root.right = self.solution(nums[numsLen/2+1:])
        return root
    
