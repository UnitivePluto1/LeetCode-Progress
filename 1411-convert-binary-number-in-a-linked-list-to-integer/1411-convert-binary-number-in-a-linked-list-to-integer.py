# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head
        value = 0

        while curr:
            value = value * 10 + curr.val
            curr = curr.next
        
        return int(str(value),2)