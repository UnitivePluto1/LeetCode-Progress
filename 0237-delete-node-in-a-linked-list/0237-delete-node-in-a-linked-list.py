# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        Next = curr

        Next = curr.next
        curr.val = Next.val
        curr.next = Next.next

        Next.val = None
        Next.next = None