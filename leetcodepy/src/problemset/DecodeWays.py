'''
Created on Sep 20, 2015

@author: mianmianba
'''

class NumDecodings(object):
    def solutionDP(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        numDec = [0] * len(s)
        cnt = 0
        cb = ''
        for cc in s:
            if cnt == 0:
                if cc == '0': return 0
                else: 
                    numDec[cnt] = 1
            elif cnt == 1:
                if cc == '0':
                    if cb > '2': return 0
                    else: 
                        numDec[1] = 1
                        numDec[0] = 0
                elif cc > '0' and cc <= '6':
                    if cb > '2':
                        numDec[1] = 1
                    else:
                        numDec[1] = 2
                else:
                    if cb == '1': numDec[1] = 2
                    else: numDec[1] = 1    
            else:
                if cc == '0':
                    if cb == '1' or cb == '2':
                        numDec[cnt] = numDec[cnt - 2]
                        numDec[cnt - 1] = 0 
                    else:
                        return 0
                elif cc > '0' and cc <= '6':
                    if cb == '0' or cb >= '3':
                        numDec[cnt] = numDec[cnt-1]
                    else:
                        numDec[cnt] = numDec[cnt-1] + numDec[cnt-2]
                elif cc > '6':
                    if cb == '0' or cb >= '2':
                        numDec[cnt] = numDec[cnt-1]
                    else:
                        numDec[cnt] = numDec[cnt-1] + numDec[cnt-2]
            cb = cc
            cnt += 1
        return numDec[-1]
    
    def solutionDPOnline(self, s):
        if s=="" or s[0]=='0': return 0
        dp=[1,1]
        for i in range(2,len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp.append(dp[i-2])
            elif s[i-1]!='0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]
                        