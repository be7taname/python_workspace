'''
Created on Aug 29, 2015

@author: mianmianba
'''

class TwoSum(object):
    def solution(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in xrange(len(nums)):
            x = nums[i]
            if target-x in dict:
                return [dict[target-x]+1, i+1] # using tuple will be faster than using list
            dict[x] = i



