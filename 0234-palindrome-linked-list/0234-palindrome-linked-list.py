# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head
        while curr:
            nextT=curr.next
            curr.next = prev
            prev = curr
            curr = nextT
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = slow

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        rev = self.reverse(slow)
        while rev:
            if head.val!=rev.val:
                return False
            head = head.next
            rev = rev.next
        return True