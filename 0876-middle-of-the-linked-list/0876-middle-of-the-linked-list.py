# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Move fast two steps and slow one step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # When fast hits the end, slow is at the middle
        return slow