'''
Created on Sep 15, 2015

@author: mianmianba
'''
class SingleNumber(object):
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
            