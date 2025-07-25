# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        current = head

        while current != None:
            nextN = current.next
            current.next = new
            new = current
            current = nextN
        return new
