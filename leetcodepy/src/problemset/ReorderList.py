'''
Created on Oct 2, 2015

@author: mianmianba
'''

from common.ListNode import ListNode

class ReorderList(object):
    def solution(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        curp = head
        listLen = 0
        while curp:
            listLen += 1
            curp = curp.next
        if listLen <= 2: return
        else:
            halfLen = (listLen + 1) / 2
            firstTail = head
            for i in range(halfLen-1):
                firstTail = firstTail.next
            secondHead = firstTail.next
            curp = secondHead
            while curp.next:
                tmpp = curp.next
                curp.next = curp.next.next
                tmpp.next = secondHead
                secondHead = tmpp
                firstTail.next = secondHead
            firstHead = head
            while firstHead != firstTail:
                tmpp1 = firstHead.next
                tmpp2 = secondHead.next
                firstHead.next = secondHead
                secondHead.next = tmpp1
                firstTail.next = tmpp2
                firstHead = tmpp1
                secondHead = tmpp2
                