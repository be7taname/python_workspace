'''
Created on Oct 5, 2015

@author: mianmianba
'''

import collections

class ContainsNearbyAlmostDuplicate(object):
    def solutionDict(self, nums, k, t):
        numsDict = collections.OrderedDict()
        for i in range(len(nums)):
            key = nums[i]/max(1, t)
            for m in (key, key-1, key+1):
                if m in numsDict and abs(nums[i]-numsDict[m]) <= t:
                    return True
            numsDict[key] = nums[i]
            if i >= k:
                numsDict.popitem(last=False)
        return False
        
    def solution(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        numsLen = len(nums)
        if numsLen == 1: return False
        if k >= numsLen: k = numsLen - 1
        for i in range(k+1):
            for j in range(i+1, k+1):
                if abs(nums[i] - nums[j]) <= t: return True
        for i in range(k+1, numsLen):
            for j in range(i-k, i):
                if abs(nums[i] - nums[j]) <= t: return True
        return False
                
        