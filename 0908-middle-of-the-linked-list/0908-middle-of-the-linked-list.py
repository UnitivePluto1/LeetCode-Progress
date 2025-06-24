# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        mid = None
        cnt = 0
        while curr:
            cnt+=1
            curr = curr.next
        midcnt = cnt//2
        curr = head
        while midcnt != 0:
            midcnt -=1
            curr = curr.next
        return curr