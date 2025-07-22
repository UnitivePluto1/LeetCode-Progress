# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        result = []

        while l1:
            num1.append(l1.val)
            l1 = l1.next

        while l2:
            num2.append(l2.val)
            l2 = l2.next

        head1 = tail1 = ListNode(0)
        carry = 0

        while num1 or num2 or carry:
            num1v = num1.pop() if num1 else 0
            num2v = num2.pop() if num2 else 0
            res = num1v + num2v + carry
            carry = res // 10
            res = res%10
            result.append(res)
        
        while result:
            temp = ListNode(result.pop())
            tail1.next = temp
            tail1 = tail1.next
            

        return head1.next
