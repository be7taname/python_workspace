'''
Created on Oct 22, 2015

@author: mianmianba
'''

class MyPow(object):
    def solution(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1.0
        neg = 0
        if n < 0: 
            n = -n
            neg = 1
        if n == 1: 
            if neg: return 1/x
            else: return x
        else:
            t = self.solution(x, n/2)
            if n%2 == 0:
                if neg:
                    return 1/(t*t)
                else:
                    return t*t
            else:
                if neg:
                    return 1/(t*t*x)
                else:
                    return t*t*x
