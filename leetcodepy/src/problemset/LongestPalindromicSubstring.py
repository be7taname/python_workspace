'''
Created on Sep 5, 2015

@author: mianmianba
'''
class LongestPalindrome(object):
    def findPalindromeAtCenter(self, s, c1, c2):
        while c1 >= 0 and c2 < len(s) and s[c1] == s[c2]:
            c1 -= 1
            c2 += 1
        return s[c1+1:c2]
        
    def solution(self, s):
        sLen = len(s)
        if sLen == 1:
            return s
        maxLen = 0
        for i in range(sLen):
            strA = self.findPalindromeAtCenter(s, i, i)
            if len(strA) > maxLen:
                maxLen = len(strA)
                maxStr = strA
            if i+1 < sLen:
                strA = self.findPalindromeAtCenter(s, i, i+1)
                if len(strA) > maxLen:
                    maxLen = len(strA)
                    maxStr = strA
        return maxStr
        
    def solutionRecursive(self, s):
        """
        :type s: str
        :rtype: str
        """
        strLen = len(s)
        if strLen == 1:
            return s
        strA = self.solutionRecursive(s[1:])
        lenA = len(strA)
        if strLen - lenA >= 2:
            newLong = True
            for i in range((lenA+2)/2):
                if s[i] != s[lenA+1-i]:
                    newLong = False
                    break
        else:
            newLong = False
        if newLong:
            return s[:lenA+2]
        else:
            newLong = True
            for i in range((lenA+1)/2):
                if s[i] != s[lenA-i]:
                    newLong = False
                    break
            if newLong:
                return s[:lenA+1]
            else:
                return strA
    