'''
Created on Oct 19, 2015

@author: mianmianba
'''

class Permute(object):
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsLen = len(nums)
        if numsLen == 1: return [[nums[0]]]
        res = []
        visited = []
        for i in range(numsLen):
            if nums[i] in visited:
                continue
            else:
                visited.append(nums[i])
            thisRes = self.solution(nums[0:i] + nums[i+1:])
            for ss in thisRes:
                ss.append(nums[i])
            res += thisRes
        return res
    
            
                