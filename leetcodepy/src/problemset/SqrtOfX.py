'''
Created on Oct 14, 2015

@author: mianmianba
'''

class MySqrt(object):
    def solutionFast(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        if x < 4: return 1
        elif x < 9: return 2
        else:
            nxtGuess = x/2
            guess = 0
            while guess - nxtGuess != 1:
                guess = nxtGuess
                nxtGuess = guess/2 + x/2/guess
            guess2 = nxtGuess * nxtGuess
            if guess2 == x:
                return nxtGuess
            elif guess2 < x:
                if (nxtGuess+1)*(nxtGuess+1) <= x:
                    return nxtGuess+1
                else:
                    return nxtGuess
            else:
                return nxtGuess-1
            
            

    def solution(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        if x < 4: return 1
        elif x < 9: return 2
        else:
            maxx = x/2
            minx = 1
            while maxx - minx > 1:
                guess = (minx + maxx) / 2
                guess2 = guess * guess
                if guess2 > x:
                    maxx = guess
                elif guess2 < x:
                    minx = guess
                else:
                    return guess
            return minx
        