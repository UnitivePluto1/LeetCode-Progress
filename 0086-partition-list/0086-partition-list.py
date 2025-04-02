# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:



        head1=tail1=None
        head2=tail2 = None

        temp = head
        while temp:
            if temp.val < x:

                if not head1:
                    head1=tail1=temp


                else:
                    tail1.next=temp 
                   
                    tail1=tail1.next  
            else:    
                
                if not head2:
                    head2=tail2 = temp
                else:
                    tail2.next = temp
                    tail2=tail2.next
            temp = temp.next
        
        if not head1:
           return head2
        
        if tail2:
            tail2.next=None

        tail1.next = head2

        return head1