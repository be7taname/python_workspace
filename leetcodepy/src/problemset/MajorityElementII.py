'''
Created on Oct 12, 2015

@author: mianmianba
'''

class MajorityElementII(object):
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1 = 0; n2 = 0
        k1 = None; k2 = None
        for x in nums:
            if k1 != None and x == k1:
                n1 += 1
            elif k2 != None and x == k2:
                n2 += 1
            elif n1 == 0:
                k1 = x
                n1 = 1
            elif n2 == 0:
                k2 = x
                n2 = 1
            else:
                n1 -= 1
                n2 -= 1          
        n1 = 0; n2 = 0
        for x in nums:
            if x == k1: n1 += 1
            elif x == k2: n2 += 1
        res = []
        if n1 > len(nums)/3: res.append(k1)
        if n2 > len(nums)/3: res.append(k2)
        return res
                                                    