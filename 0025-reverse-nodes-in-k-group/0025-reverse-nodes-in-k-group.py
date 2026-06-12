class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Check if we have at least k nodes
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
            
        if count == k:
            # Reverse the first k nodes
            reversed_head = self._reverse(head, k)
            
            # Recurse for the remaining nodes
            head.next = self.reverseKGroup(curr, k)
            
            return reversed_head
        
        return head

    def _reverse(self, head, k):
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev