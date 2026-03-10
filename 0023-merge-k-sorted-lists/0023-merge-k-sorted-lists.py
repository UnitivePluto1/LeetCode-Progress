# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for j in lists:
            if not j:
                continue
            curr = j
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        heapq.heapify(heap)

        ans=ListNode()
        val = ans
        while heap:
            val.next = ListNode(heapq.heappop(heap))
            val=val.next
        return ans.next

