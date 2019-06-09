#coding: utf-8


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """def middleNode(self, head: ListNode) -> ListNode:
        """
        if not head:
            return None
        worm = head
        rocket = head
        while rocket and rocket.next:
            worm = worm.next
            rocket = rocket.next.next
        return worm