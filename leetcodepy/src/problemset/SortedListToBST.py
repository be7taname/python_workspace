'''
Created on Sep 13, 2015

@author: mianmianba
'''

from common.TreeNode import TreeNode
from common.ListNode import ListNode
class SortedListToBST(object):
    def genBstFromList(self, listHead, listLen):
        if listLen == 1:
            tn = TreeNode(listHead.val)
            return (tn, listHead.next)
        elif listLen == 0:
            return (None, listHead)
        else:
            (leftTree, listHead) = self.genBstFromList(listHead, listLen/2)
            root = TreeNode(listHead.val)
            root.left = leftTree
            (root.right, listHead) = self.genBstFromList(listHead.next, listLen - listLen/2 - 1)
            return (root, listHead)
        
    def solution(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        thisListNode = head
        listNodeCnt = 0
        while thisListNode:
            listNodeCnt += 1
            thisListNode = thisListNode.next
        if listNodeCnt == 0: return None
        (root, head) = self.genBstFromList(head, listNodeCnt)
        return root
    