'''
Created on Sep 22, 2015

@author: mianmianba
'''

class LadderLength(object):
    def diffOne(self, word1, word2, wordLen):
        numDiff = 0
        for i in range(wordLen):
            if word1[i] != word2[i]:
                if numDiff == 0:
                    numDiff = 1
                else:
                    return False
        return False if numDiff == 0 else True
        
    def solution(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord: return 1
        wordList.add(endWord)
        wordList.discard(beginWord)
        wordLen = len(beginWord)
        curSet = set()
        for word in wordList:
            if self.diffOne(word, beginWord, wordLen):
                if word == endWord: return 2
                else:
                    curSet.add(word)
        wordList -= curSet
        curLevel = 2
        while wordList:
            curLevel += 1
            change = 0
            nxtSet = set()
            for wordR in wordList:
                for wordC in curSet:
                    if self.diffOne(wordR, wordC, wordLen):
                        change = 1
                        if wordR == endWord: return curLevel
                        else:
                            nxtSet.add(wordR)
                        break
            if change == 0: return 0
            wordList -= nxtSet
            curSet = nxtSet
        return 0           

    def solutionBFS(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord: return 1
        wordList.discard(beginWord)
        wordList.add(endWord)
        wordTreeQ = [beginWord]
        wordLen = len(beginWord)
        curLevel = 1
        lastWordInCurLevel = beginWord
        lastWordInNxtLevel = ""
        while wordTreeQ:
            curWord = wordTreeQ.pop(0)
            for i in range(wordLen):
                wd1 = curWord[:i]
                wd2 = curWord[i+1:]
                for cc in 'abcdefghijklmnopqrstuvwxyz':
                    tryWord = wd1 + cc + wd2
                    if tryWord in wordList:
                        if tryWord == endWord: return curLevel + 1
                        else: 
                            wordTreeQ.append(tryWord)
                            wordList.remove(tryWord)
                            lastWordInNxtLevel = tryWord
            if curWord == lastWordInCurLevel:
                lastWordInCurLevel = lastWordInNxtLevel
                curLevel += 1
        return 0
