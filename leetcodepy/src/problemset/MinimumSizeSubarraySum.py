'''
Created on Oct 15, 2015

@author: mianmianba
'''

class MinSubArrayLen(object):
    def solution(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        sidx = -1; eidx = 0
        suma = 0; minlen = len(nums) + 1; curlen = 0
        while sidx < eidx and eidx <= len(nums):
            if suma >= s:
                if curlen < minlen: minlen = curlen
                if sidx != -1:
                    suma -= nums[sidx]
                    curlen -= 1
                sidx += 1
            else:
                if eidx == len(nums): break
                suma += nums[eidx]
                eidx += 1
                curlen += 1
        if minlen > len(nums): return 0
        else: return minlen
        