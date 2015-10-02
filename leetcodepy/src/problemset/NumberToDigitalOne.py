'''
Created on Oct 1, 2015

@author: mianmianba
'''

class CountDigitOne(object):
    def solution(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        else:
            m = 1
            totCnt = 0
            while m <= n:
                a = n/m
                b = n%m
                totCnt += (a+8)/10*m + (a%10==1)*(b+1)
                m*=10
        return totCnt
