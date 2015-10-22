'''
Created on Oct 21, 2015

@author: mianmianba
'''

class LetterCombinations(object):
    def getString(self, digits, dict):
        if len(digits) == 1:
            return dict[digits]
        thisRes = self.getString(digits[1:], dict)
        res = []
        for letter in dict[digits[0]]:
            for ss in thisRes:
                res.append(letter + ss)
        return res
        
    def solution(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '': return []
        dict = {'2': ['a', 'b', 'c'], 
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        return self.getString(digits, dict)
        