'''
Created on Sep 20, 2015

@author: mianmianba
'''

class Divide(object):
    def solution(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        pos = 1
        if divisor == 0: return 2147483647
        if dividend < 0:
            dividend = -dividend
            pos ^= 1
        if divisor < 0:
            divisor = -divisor
            pos ^= 1
        res = 0
        while dividend >= divisor:
            curDiv = divisor << 1
            numShift = 1
            while dividend >= curDiv:
                numShift += 1
                curDiv <<= 1
            numShift -= 1
            res += (1 << numShift)
            dividend -= (divisor << numShift)
        if pos == 1 and res > 2147483647:
            res = 2147483647
        return (res if pos == 1 else -res)
    