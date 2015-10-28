'''
Created on Oct 21, 2015

@author: mianmianba
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.ListNode import ListNode
class ReverseBetween(object):
    def solution(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        for i in range(m-1):
            p1 = p1.next
        pf = p1.next
        for j in range(n-m):
            t = p1.next
            p1.next = pf.next
            pf.next = pf.next.next
            p1.next.next = t
        return dummy.next
    
        