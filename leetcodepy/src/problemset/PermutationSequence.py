'''
Created on Oct 13, 2015

@author: mianmianba
'''

class GetPermutation(object):
    def solution(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        num = [x for x in range(1, n+1)]
        limit = [1]
        for i in range(1, n-1):
            limit.append(limit[i-1]*(i+1))
        k = k-1
        for i in range(n-1):
            thisLimit = limit.pop()
            idx = k/thisLimit
            res += str(num.pop(idx))
            k %= thisLimit
        res += str(num.pop())
        return res
    