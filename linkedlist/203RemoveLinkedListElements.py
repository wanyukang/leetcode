#coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        new_head = ListNode(0)
        new_head.next = head
        curr_node = new_head
        while curr_node and curr_node.next:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return new_head.next