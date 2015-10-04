'''
Created on Oct 3, 2015

@author: mianmianba
'''

class RestoreIpAddresses(object):
    def IsValidIp(self, s):
        sLen = len(s)
        if s[0] == '0':
            if sLen > 1: return False
            else: return True
        else:
            if int(s) <= 255: return True
            else: return False
            
    def FindIpAddress(self, s, num):
        sLen = len(s)
        if sLen == 0: return []
        if num == 1:
            if self.IsValidIp(s):
                return [s]
            else:
                return []
        else:
            if sLen < num:
                return []
            else:
                allIps = []
                if sLen >= 2:
                    subIps = self.FindIpAddress(s[1:], num-1)
                    if subIps != []:
                        for subIp in subIps:
                            allIps.append(s[0] + '.' + subIp)
                if sLen >= 3:
                    if self.IsValidIp(s[0:2]):
                        subIps = self.FindIpAddress(s[2:], num-1)
                        if subIps != []:
                            for subIp in subIps:
                                allIps.append(s[0:2] + '.' + subIp)
                if sLen >= 4:
                    if self.IsValidIp(s[0:3]):
                        subIps = self.FindIpAddress(s[3:], num-1)
                        if subIps != []:
                            for subIp in subIps:
                                allIps.append(s[0:3] + '.' + subIp)
                return allIps
                
    def solution(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s == '': return []
        return self.FindIpAddress(s, 4)
    