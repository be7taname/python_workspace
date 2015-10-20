'''
Created on Oct 19, 2015

@author: mianmianba
'''

class CombinationSum(object):
    def solution(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        prev = candidates[0] - 1
        res = []
        for i in range(len(candidates)):
            num = candidates[i]
            if num == prev: continue
            else: prev = num
            if num > target: return res
            if num == target: 
                res.append([target])
                return res
            thisRes = self.solution(candidates[i:], target - num)
            for ss in thisRes:
                ss.insert(0, num)
            res += thisRes
        return res
    
            