'''
Created on Oct 1, 2015

@author: mianmianba
'''

from common.ListNode import ListNode

class AddTwoNumbers(object):
    def solution(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curp = head
        c3 = 0
        while l1 and l2:
            cursum = c3 + l1.val + l2.val
            if cursum >= 10:
                c3 = 1
                cursum -= 10
            else:
                c3 = 0
            curp.next = ListNode(cursum)
            curp = curp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            cursum = c3 + l1.val
            if cursum >= 10:
                c3 = 1
                cursum -= 10
            else:
                c3 = 0
            curp.next = ListNode(cursum)
            curp = curp.next
            l1 = l1.next
        while l2:
            cursum = c3 + l2.val
            if cursum >= 10:
                c3 = 1
                cursum -= 10
            else:
                c3 = 0
            curp.next = ListNode(cursum)
            curp = curp.next
            l2 = l2.next
        if c3 == 1:
            curp.next = ListNode(1)
        return head.next
            
            