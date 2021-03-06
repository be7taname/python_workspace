'''
Created on Sep 14, 2015

@author: mianmianba
'''

class FractionToDecimal(object):
    def solution(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator < 0: 
            denominator = -denominator
            numerator = -numerator
        if numerator < 0:
            numerator = -numerator
            sign = -1
        else:
            sign = 1
        intPart = numerator / denominator
        remainder = numerator - denominator * intPart
        if remainder == 0: return str(sign*intPart)
        # remVisited = [0] * denominator
        remVisited = []
        remVisited.append(remainder)
        fracPart = []
        rep = 0
        while remainder != 0:
            newFrac = remainder * 10 / denominator
            remainder = remainder * 10 - newFrac * denominator
            fracPart.append(newFrac)
            if remainder not in remVisited: remVisited.append(remainder)
            else:
                rep = 1
                index = remVisited.index(remainder)
                break 
        if rep == 0:
            ss = '{}.{}'.format(intPart, "".join([str(n) for n in fracPart]))
        else:
            ss = '{}.{}({})'.format(intPart, "".join([str(n) for n in fracPart[:index]]), "".join([str(n) for n in fracPart[index:]]))
        if sign == -1:
            return "-" + ss
        else:
            return ss
            
            
            
            