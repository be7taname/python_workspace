'''
Created on Sep 15, 2015

@author: mianmianba
'''

class Calculate(object):
    def doCal(self, strn, stk):
        if not stk or stk[-1] == '(':
            stk.append(strn)
        else:
            if stk[-1] == '+':
                stk.pop()
                stk.append(str(int(strn) + int(stk.pop())))
            elif stk[-1] == '-':
                stk.pop()
                stk.append(str(int(stk.pop()) - int(strn)))
        
    def solutionStack(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        cnt = 0
        stck = []
        while cnt < sLen:
            ch = s[cnt]
            numStr = ""
            while ch >= '0' and ch <= '9':
                numStr += ch
                cnt += 1
                if cnt >= sLen: break
                ch = s[cnt]
            if numStr: self.doCal(numStr, stck)
            if ch == '+':
                stck.append(ch)
            elif ch == '-':
                stck.append(ch)
            elif ch == '(':
                stck.append(ch)
            elif ch == ')':
                numStr = stck.pop()
                stck.pop()
                self.doCal(numStr, stck)
            cnt += 1
        return int(stck.pop())

    def solution(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = ['0','1','2','3','4','5','6','7','8','9']
        signs = ['-', '+']
        res = 0
        sign = 1
        val = 0
        mode = 0
        parCnt = 0
        substr = []
        for cc in s:
            if cc == ')':
                parCnt -= 1
                if parCnt == 0:
                    val = self.solution(substr)
                    mode = 1
                else:
                    substr += cc
                continue
            if mode == -1:
                substr += cc
                if cc == '(': 
                    parCnt += 1
                continue
            if cc == '(':
                parCnt += 1
                mode = -1
                substr = []
                continue
            if mode == 0:
                if cc in digits:
                    mode = 1
                    if cc == '0': val = 0
                    elif cc == '1': val = 1
                    elif cc == '2': val = 2
                    elif cc == '3': val = 3
                    elif cc == '4': val = 4
                    elif cc == '5': val = 5
                    elif cc == '6': val = 6
                    elif cc == '7': val = 7
                    elif cc == '8': val = 8
                    elif cc == '9': val = 9
                elif cc in signs:
                    mode = 2
                    val = 0
                    if cc == '-': sign = -1
                    elif cc == '+': sign = 1
            elif mode == 1:
                if cc in digits:
                    val *= 10
                    if cc == '1': val += 1
                    elif cc == '2': val += 2
                    elif cc == '3': val += 3
                    elif cc == '4': val += 4
                    elif cc == '5': val += 5
                    elif cc == '6': val += 6
                    elif cc == '7': val += 7
                    elif cc == '8': val += 8
                    elif cc == '9': val += 9
                else:
                    res += sign*val
                    val = 0
                    if cc in signs:
                        mode = 2
                        if cc == '-': sign = -1
                        elif cc == '+': sign = 1
                    else:
                        mode = 0
                        sign = 1
            elif mode == 2:
                if cc in digits:
                    mode = 1
                    if cc == '0': val = 0
                    elif cc == '1': val = 1
                    elif cc == '2': val = 2
                    elif cc == '3': val = 3
                    elif cc == '4': val = 4
                    elif cc == '5': val = 5
                    elif cc == '6': val = 6
                    elif cc == '7': val = 7
                    elif cc == '8': val = 8
                    elif cc == '9': val = 9
                else:
                    val = 0
                    mode = 0
        res += sign*val
        return res
    