'''
Created on Sep 27, 2015

@author: mianmianba
'''

class MaxProduct(object):
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        if numsLen == 1: return nums[0]
        else:
            curMax = nums[0]
            curMin = nums[0]
            maxAll = nums[0]
            for num in nums[1:]:
                if (curMin <= 0 and curMax <= 0 and num >= 0):
                    curMax, curMin = num, curMin*num
                elif (curMin <= 0 and curMax <= 0 and num < 0):
                    curMax, curMin = curMin*num, num
                elif (curMin <= 0 and curMax > 0 and num >= 0):
                    curMax, curMin = curMax*num, curMin*num
                elif (curMin <= 0 and curMax > 0 and num < 0):
                    curMax, curMin = curMin*num, curMax*num
                elif (curMin > 0 and curMax > 0 and num >= 0):
                    curMax, curMin = curMax*num, num
                elif (curMin > 0 and curMax > 0 and num < 0):
                    curMax, curMin = num, curMax*num
                if curMax > maxAll: maxAll = curMax
            return maxAll
        
                