'''
Created on Oct 5, 2015

@author: mianmianba
'''

class EvalRPN(object):
    def solution(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = set(['+', '-', '*', '/'])
        numStack = []
        for cc in tokens:
            if cc in op:
                val2 = numStack.pop()
                val1 = numStack.pop()
                if cc == '+':
                    numStack.append(val1 + val2)
                elif cc == '-':
                    numStack.append(val1 - val2)
                elif cc == '*':
                    numStack.append(val1 * val2)
                else:
                    numStack.append(int(1.0 * val1 / val2))
#                     if (val1 >= 0 and val2 >= 0) or (val1 <= 0 and val2 <= 0): 
#                         numStack.append(val1 / val2)
#                     else:
#                         numStack.append(-(-val1/val2))
            else:
                numStack.append(int(cc))
        return numStack[0]
    