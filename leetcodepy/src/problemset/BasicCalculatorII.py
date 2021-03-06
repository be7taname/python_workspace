'''
Created on Sep 24, 2015

@author: mianmianba
'''

class Calculate(object):
    def compEqu(self, equStack, equSymbol):
        if not equStack:
            equStack.append(equSymbol)
            return
        if equStack[-1] == '*':
            equStack.pop()
            val1 = int(equStack.pop())
            equStack.append(str(val1 * int(equSymbol)))
        elif equStack[-1] == '/':
            equStack.pop()
            val1 = int(equStack.pop())
            equStack.append(str(val1 / int(equSymbol)))
        elif equStack[-1] == '+' or equStack[-1] == '-':
            if len(equStack) == 4:
                op = equStack.pop()
                val2 = int(equStack.pop())
                oldOp = equStack.pop()
                if oldOp == '+':
                    equStack.append(str(int(equStack.pop()) + val2))
                elif oldOp == '-':
                    equStack.append(str(int(equStack.pop()) - val2))
                equStack.append(op)
                equStack.append(equSymbol)
            else:
                equStack.append(equSymbol)
                
        
    def solution(self, s):
        """
        :type s: str
        :rtype: int
        """
        equStack = []
        strLen = len(s)
        cnt = 0
        while cnt < strLen:
            cc = s[cnt]
            if cc >= '0' and cc <= '9':
                curNumStr = cc
                cnt = cnt + 1
                while cnt < strLen: # either (cc is not a number) or (cnt == strLen and cc is a number) 
                    cc = s[cnt]
                    if cc >= '0' and cc <= '9':
                        curNumStr += cc
                        cnt += 1
                    else:
                        break
                self.compEqu(equStack, curNumStr)
            if cc in '+-*/':
                equStack.append(cc)
            cnt += 1
        if len(equStack) == 3:
            val2 = int(equStack.pop())
            op = equStack.pop()
            if op == '+':
                equStack.append(str(int(equStack.pop()) + val2))
            elif op == '-':
                equStack.append(str(int(equStack.pop()) - val2))
            elif op == '*':
                equStack.append(str(int(equStack.pop()) * val2))
            elif op == '/':
                equStack.append(str(int(equStack.pop()) / val2))
        return int(equStack.pop())
    
            
        
                