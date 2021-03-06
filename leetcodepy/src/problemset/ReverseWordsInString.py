'''
Created on Sep 20, 2015

@author: mianmianba
'''
class ReverseWords(object):
    def solutionOneline(self, s):
        return " ".join(s.split()[::-1])
        
    def solution(self, s):
        """
        :type s: str
        :rtype: str
        """
        sLen = len(s)
        wordList = []
        i = 0
        while i < sLen:
            cc = s[i]
            if cc != " ":
                curWord = cc
                i += 1
                while i < sLen:
                    cc = s[i]
                    if cc == " ": break
                    curWord += cc
                    i += 1
                wordList.append(curWord)
            if cc == " ":
                i += 1
        revS = ""
        while wordList:
            revS += (wordList.pop() + " ")
        return revS[:-1]
    