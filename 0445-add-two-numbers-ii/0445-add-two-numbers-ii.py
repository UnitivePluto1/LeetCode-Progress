# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        rev1 = rev(l1)
        rev2 = rev(l2)

        head1 = tail1 = ListNode(0)
        carry = 0

        while rev1 or rev2 or carry:
            l1v = rev1.val if rev1 else 0
            l2v = rev2.val if rev2 else 0
            res = l1v+l2v+carry
            carry = res // 10
            res = res%10
            temp = ListNode(res)
            tail1.next = temp
            tail1 = tail1.next
            rev1 = rev1.next if rev1 else 0
            rev2 = rev2.next if rev2 else 0
        return rev(head1.next)
