'''
Created on Sep 21, 2015

@author: mianmianba
'''
class LargestNumber(object):
    def mycmp(self, x, y):
        return -1 if x + y > y + x else 1
    
    def solution(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numstr = [str(num) for num in nums]
        numstrSort = sorted(numstr, cmp = self.mycmp)
        res = "".join(numstrSort)
        for i in range(len(res)):
            cc = res[i]
            if cc != '0': break
        res = res[i:]
        return res
    