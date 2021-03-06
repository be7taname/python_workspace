'''
Created on Oct 2, 2015

@author: mianmianba
'''

class FindRepeatedDnaSequences(object):
    def solution(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        allseq = dict()
        dnaMap = {'A':0, 'C':1, 'G':2 ,'T':3}
        curseq = 0
        for i in range(len(s)):
            curseq <<= 2
            curseq ^= dnaMap[s[i]]
            curseq &= 0xFFFFF
            if i < 9: continue
            allseq[curseq] = allseq.get(curseq, 0) + 1
            if allseq[curseq] == 2: 
                ret.append(s[i-9:i+1])
        return ret
    