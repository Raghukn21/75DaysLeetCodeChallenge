class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        # Loop until the two pointers meet
        while pA != pB:
            # If pA reaches the end, jump to headB, else move to next
            pA = pA.next if pA else headB
            
            # If pB reaches the end, jump to headA, else move to next
            pB = pB.next if pB else headA

        # Either they met at the intersection or both are None
        return pA