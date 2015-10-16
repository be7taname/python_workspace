'''
Created on Oct 15, 2015

@author: mianmianba
'''
import collections

class GroupAnagrams(object):
    def solution(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dict = collections.defaultdict(list)
        for s in strs:
            dict[str(sorted(s))].append(s)
        for value in dict.values():
            res.append(sorted(value))
        return res
    