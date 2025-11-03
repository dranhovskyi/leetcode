# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Optimal solution Complexity: O(max(n,m)), Space Complexity: O(1) or O(max(n, m))
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0

        while l1 != None or l2 != None or carry != 0: 
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            sum = x + y + carry

            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next

        return dummyHead.next

        