#coding: utf-8


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """def reverseList(self, head: ListNode) -> ListNode:
        """
        pre_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = next_node
        return pre_node