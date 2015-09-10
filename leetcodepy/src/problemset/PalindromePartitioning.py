'''
Created on Sep 9, 2015

@author: mianmianba
'''

class PalindromePartitioning(object):
    def solution(self, s):
        partition = []
        result = []
        self.findPartition(s, 0, partition, result)
        return result
        
    def checkPalindrome(self, ss):
        for i in range(len(ss)/2):
            if ss[i] != ss[len(ss)-1-i]:
                return False
        else:
            return True
                 
    def findPartition(self, s, start, partition, result):
        if start == len(s):
            result.append(list(partition))
        else:
            for i in range(start, len(s)):
                if self.checkPalindrome(s[start:i+1]):
                    partition.append(s[start:i+1])
                    self.findPartition(s, i+1, partition, result)
                    partition.pop()

    # version from Internet, looks better
    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True
    
    def dfs(self, s, stringlist):
        if len(s) == 0: PalindromePartitioning.res.append(stringlist)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist+[s[:i]])
            
    def partition(self, s):
        PalindromePartitioning.res = []
        self.dfs(s, [])
        return PalindromePartitioning.res                
