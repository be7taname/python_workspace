'''
Created on Oct 6, 2015

@author: mianmianba
'''

class FourSum(object):
    def solutionFast(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numsLen, rslt, twosumMap = len(nums), set(), {}
        nums.sort()
        if numsLen < 4: return []
        else:
            for i in range(numsLen-1):
                for j in range(i+1, numsLen):
                    thisSum = nums[i] + nums[j]
                    if thisSum not in twosumMap:
                        twosumMap[thisSum] = [(i, j)]
                    else:
                        twosumMap[thisSum].append((i, j))
            for i in range(numsLen-3):
                for j in range(i+1, numsLen-2):
                    key = target - nums[i] - nums[j]
                    if key in twosumMap:
                        for idx in twosumMap[key]:
                            if idx[0] > j:
                                rslt.add((nums[i], nums[j], nums[idx[0]], nums[idx[1]]))
        return [list(x) for x in rslt]
            
        

    def solution(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        numsLen = len(nums)
        res = []
        if numsLen < 4: return None
        else:
            for i in range(numsLen-3):
                if i > 0 and nums[i] == nums[i-1]: continue
                for j in range(i+1, numsLen-2):
                    if j > i+1 and nums[j] == nums[j-1]: continue
                    head = j+1
                    tail = numsLen-1
                    while head < tail:
                        thisSum = nums[i] + nums[j] + nums[head] + nums[tail]
                        if thisSum == target:
                            res.append([nums[i], nums[j], nums[head], nums[tail]])
                            head += 1
                            while head < tail and nums[head] == nums[head-1]:
                                head += 1
                            tail -= 1
                            while head < tail and nums[tail] == nums[tail+1]:
                                tail -= 1
                        elif thisSum < target:
                            head += 1
                            while head < tail and nums[head] == nums[head-1]:
                                head += 1
                        elif thisSum > target:
                            tail -= 1
                            while head < tail and nums[tail] == nums[tail+1]:
                                tail -= 1
        return res
                            