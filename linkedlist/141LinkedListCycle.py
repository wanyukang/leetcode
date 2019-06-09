#coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        worm = head
        rocket = head
        while rocket and rocket.next:   
            worm = worm.next
            rocket = rocket.next.next
            if worm == rocket:
                return True 
        return False