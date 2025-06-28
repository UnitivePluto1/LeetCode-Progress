# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hmap = dict()
        curr = head
        dummy = ListNode()
        temp = dummy


        while curr:
            hmap[curr.val] = hmap.get(curr.val, 0) + 1
            curr = curr.next
        
        for num, val in hmap.items():
            if val == 1:
                dummy.next = ListNode(num)
                dummy = dummy.next

        return temp.next