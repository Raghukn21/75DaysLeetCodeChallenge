# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list or single-node list
        if not head:
            return head
        
        curr = head
        
        # Traverse until the second to last node
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Duplicate found! Skip the next node
                curr.next = curr.next.next
            else:
                # No duplicate, move to the next distinct element
                curr = curr.next
                
        return head