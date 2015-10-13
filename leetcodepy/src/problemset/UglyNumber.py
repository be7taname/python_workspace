'''
Created on Oct 12, 2015

@author: mianmianba
'''

class IsUgly(object):
    def solution(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        elif num == 1: return True
        else:
            while num%2 == 0:
                num /= 2
                if num == 1: return True
            while num%3 == 0:
                num /= 3
                if num == 1: return True
            while num%5 == 0:
                num /= 5
                if num == 1: return True
            return False
        
            
        