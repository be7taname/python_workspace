'''
Created on Sep 28, 2015

@author: mianmianba
'''

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.isWord = False
        self.children = [None] * 26
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curNode = self
        for cc in word:
            idx = ord(cc) - ord('a')
            if not curNode.children[idx]:
                curNode.children[idx] = WordDictionary()
            curNode = curNode.children[idx]
        curNode.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word == '.': 
            for i in range(26):
                if self.children[i]: 
                    if self.children[i].isWord == True: return True
            else: return False
        else:
            curNode = self
            wordLen = len(word)
            for i in range(wordLen):
                cc = word[i]
                if cc == '.':
                    for j in range(26):
                        if curNode.children[j]:
                            if curNode.children[j].search(word[i+1:]) == True: 
                                return True
                    else: return False
                else:
                    idx = ord(cc) - ord('a')
                    if curNode.children[idx]:
                        curNode = curNode.children[idx]
                    else:
                        return False
            return (True if curNode.isWord == True else False)
                    

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
