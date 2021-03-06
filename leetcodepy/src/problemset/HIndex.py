'''
Created on Sep 8, 2015

@author: mianmianba
'''
class HIndex(object):
    def solution(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        numPaper = len(citations)
        if numPaper == 0: return 0
        citations.sort(reverse=True);
        for i in range(numPaper):
            if citations[i] < i + 1: return i
        return i+1
    
    def solutionClean(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum(i < c for i, c in enumerate(sorted(citations, reverse = True)))
    
    def solutionFast(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        np = len(citations) 
        cnts = [0] * (np + 1)
        for c in citations:
            cnts[[c, np][c > np]] += 1
        sums = 0
        for h in range(np, 0, -1):
            if sums + cnts[h] >= h: return h
            sums += cnts[h]
        return 0
    