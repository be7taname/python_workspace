'''
Created on Oct 3, 2015

@author: mianmianba
'''

class Multiply(object):
    def solution(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        num1Len = len(num1)
        num2Len = len(num2)
        prodLen = num1Len + num2Len
        prod = [0] * prodLen
        for i in range(num1Len):
            a = ord(num1[i]) - 48
            for j in range(num2Len):
                b = ord(num2[j]) - 48
                prod[i+j] += a*b
        res = []
        for i in range(len(prod)):
            c = prod[i]
            res.insert(0, str(c%10))
            if i != prodLen - 1:
                prod[i+1] += (c/10)
        for i in range(len(res)-1):
            if res[i] != '0': break
        else:
            i += 1
        return "".join(res[i:]) 
        # return str(int(num1)*int(num2))