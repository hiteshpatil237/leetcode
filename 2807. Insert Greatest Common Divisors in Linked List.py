# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current.next is not None:
            g = gcd(current.val, current.next.val)

            nxt = current.next
            current.next = ListNode(g, nxt)
            current = current.next.next
        
        return head