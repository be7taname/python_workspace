'''
Created on Sep 28, 2015

@author: mianmianba
'''

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.children = [None] * 26

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curNode = self.root
        for cc in word:
            idx = ord(cc) - ord('a')
            if not curNode.children[idx]:
                curNode.children[idx] = TrieNode()
            curNode = curNode.children[idx]
        curNode.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for cc in word:
            idx = ord(cc) - ord('a')
            if curNode.children[idx]:
                curNode = curNode.children[idx]
            else:
                return False
        return (True if curNode.isWord == True else False)
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for cc in prefix:
            idx = ord(cc) - ord('a')
            if curNode.children[idx]:
                curNode = curNode.children[idx]
            else:
                return False
        return True
        
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
