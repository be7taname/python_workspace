'''
Created on Sep 10, 2015

@author: mianmianba
'''

class MaxSubArray(object):
    def solutions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        if numsLen == 1: return nums[0]
        pmax = self.solutions(nums[1:numsLen])
        if nums[0] < 0:
            return (nums[0] if nums[0] > pmax else pmax)
        else:
            cumsum = []
            a = 0
            for i in range(len(nums)):
                a += nums[i]
                cumsum.append(a)
            cmax = max(cumsum)
            return (cmax if cmax > pmax else pmax)    
        
    def solutionFast(self, nums):
        findPos = 0
        max = nums[0]
        existPos = 0
        maxsum = 0
        for i in range(len(nums)):
            if findPos == 0:
                if nums[i] > 0:
                    existPos = 1
                    findPos = 1
                    startPos = i
                    lastPos = i
                    cumsum = nums[i]
                    p2psum = nums[i]
                    if p2psum > maxsum: maxsum = p2psum
            else:
                cumsum += nums[i]
                if nums[i] > 0:
                    lastPos = i
                    p2psum = cumsum
                    if p2psum > maxsum: maxsum = p2psum
                else:
                    if cumsum < 0:
                        if p2psum > maxsum: maxsum = p2psum
                        findPos = 0
            if existPos == 0:
                if nums[i] > max: max = nums[i]
        if existPos == 0: return max
        else: return maxsum
        
    def solutionBest(self, nums):
        cumsum = nums[0]
        maxsum = nums[0]
        for i in range(1, len(nums)):
            if cumsum > 0: cumsum += nums[i]
            else: cumsum = nums[i] 
            if cumsum > maxsum: maxsum = cumsum
        return maxsum    
        