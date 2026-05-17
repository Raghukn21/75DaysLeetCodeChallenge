# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Continue if there are nodes left in either list or a carry exists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Standard addition logic
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10
            
            # Add result to the new list
            curr.next = ListNode(new_digit)
            curr = curr.next
            
            # Move to next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next