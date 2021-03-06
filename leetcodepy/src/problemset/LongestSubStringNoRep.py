'''
Created on Sep 8, 2015

@author: mianmianba
'''
class LengthOfLongestSubstring(object):
    def solution(self, s):
        """
        :type s: str
        :rtype: int
        """
        aset = set()
        alist = []
        maxLen = 0
        for c in s:
            if c in aset:
                curLen = len(aset)
                if curLen > maxLen: maxLen = curLen
                letter = alist.pop(0)
                while letter != c:
                    aset.remove(letter)
                    letter = alist.pop(0)
                alist.append(c)
            else:
                aset.add(c)
                alist.append(c)
        else:
            curLen = len(aset)
            if curLen > maxLen: maxLen = curLen
        return maxLen
    
            