'''
Created on Oct 19, 2015

@author: mianmianba
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.ListNode import ListNode

class DeleteDuplicates(object):
    def solution(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        dummy = ListNode(head.val-1)
        dummy.next = head
        last = dummy
        curr = head
        while curr != None and curr.next != None:
            if curr.val != curr.next.val:
                last = last.next
                curr = curr.next
            else:
                while curr.val == curr.next.val:
                    curr = curr.next
                    if curr.next == None:
                        break
                curr = curr.next
                last.next = curr
        return dummy.next
    
        