'''
Created on Sep 27, 2015

@author: mianmianba
'''

class SimplifyPath(object):
    def solution(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathLen = len(path)
        cnt = 0
        pathQ = []
        while cnt < pathLen:
            cc = path[cnt]
            if cc == '/':
                if not pathQ or pathQ[-1] != '/':
                    pathQ.append(cc)
            elif cc == '.':
                dir = cc
                while cnt + 1 < pathLen:
                    cc = path[cnt + 1]
                    if cc == '/': break
                    else:
                        cnt += 1
                        dir += cc
                if dir == '.':
                    pass
                elif dir == '..':
                    pathQ.pop()
                    if pathQ: pathQ.pop()
                    else: pathQ.append('/')
                else:
                    pathQ.append(dir)
            else:
                dir = cc
                while cnt + 1 < pathLen:
                    cc = path[cnt + 1]
                    if cc == '/' or cc == '.': break
                    else: 
                        cnt += 1
                        dir += cc
                pathQ.append(dir)
            cnt += 1
        if pathQ[-1] == '/' and len(pathQ) > 1: pathQ.pop()
        return "".join(pathQ)
    
