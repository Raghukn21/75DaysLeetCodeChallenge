# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # 1. Save the next node so we don't lose the rest of the list
            next_node = curr.next
            
            # 2. Flip the pointer to point backwards
            curr.next = prev
            
            # 3. Move the 'prev' and 'curr' pointers one step forward
            prev = curr
            curr = next_node
            
        # At the end, 'prev' will be pointing to the new head (the old tail)
        return prev