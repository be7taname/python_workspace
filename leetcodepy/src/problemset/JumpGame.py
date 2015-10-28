'''
Created on Oct 27, 2015

@author: mianmianba
'''

class CanJump(object):
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxIdx = 0
        endIdx = len(nums)-1
        if endIdx == 0: return True
        for i in range(endIdx):
            if i > maxIdx: return False
            nxtIdx = nums[i] + i
            if nxtIdx >= endIdx: return True
            if nxtIdx > maxIdx:
                maxIdx = nxtIdx
        return False
    