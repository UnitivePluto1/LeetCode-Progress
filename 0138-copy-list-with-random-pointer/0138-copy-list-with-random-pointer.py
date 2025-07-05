"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {None:None}
        curr = head

        while curr:
            hash[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            temp = hash[curr]
            temp.next = hash[curr.next]
            temp.random = hash[curr.random]
            curr = curr.next

        return hash[head]
            