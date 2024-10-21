from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        p1 = l1
        p2 = l2

        while p1 is not None or p2 is not None or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
    
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10

            current.next = ListNode(new_digit)
            current = current.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy_head.next
