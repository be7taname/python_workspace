'''
Created on Oct 16, 2015

@author: mianmianba
'''

class NextPermutation(object):
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        if numsLen == 1: return
        for i in range(-1, -numsLen, -1):
            if nums[i-1] < nums[i]:
                nums[i:] = nums[i:][::-1]
                for j in range(i, 0):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        return
        else:
            nums.reverse()
        return
        
