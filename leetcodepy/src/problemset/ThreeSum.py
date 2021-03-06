'''
Created on Sep 7, 2015

@author: mianmianba
'''

class ThreeSum(object):
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        all3sum = []
        for i in range(0, len(nums)-2):
            if nums[i] > 0: break
            elif i > 0 and nums[i] == nums[i-1]: continue
            else:
                head = i+1
                tail = len(nums)-1
                while tail > head:
                    thisSum = nums[i] + nums[head] + nums[tail]
                    if thisSum > 0:
                        tail -= 1
                        while tail >= 0 and nums[tail] == nums[tail+1]:
                            tail -= 1
                    elif thisSum < 0:
                        head += 1
                        while head < len(nums) and nums[head] == nums[head-1]:
                            head += 1
                    else:
                        all3sum.append((nums[i], nums[head], nums[tail]))
                        head += 1
                        while head < len(nums) and nums[head] == nums[head-1]:
                            head += 1
                        tail -= 1
                        while tail >= 0 and nums[tail] == nums[tail+1]:
                            tail -= 1
                    
        return all3sum