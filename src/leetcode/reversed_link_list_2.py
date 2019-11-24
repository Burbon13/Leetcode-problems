# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return None
        if n == m:
            return head

        index = 1
        pointer = head

        if m == 1:
            last_before_list = None
        else:
            while index + 1 < m:
                pointer = pointer.next
                index += 1
            last_before_list = pointer
            pointer = pointer.next
            index += 1

        first_in_list = pointer
        index += 1
        before_pointer = pointer
        pointer = pointer.next

        while index <= n:
            next_pointer = pointer.next
            pointer.next = before_pointer
            before_pointer = pointer
            index += 1
            pointer = next_pointer

        if last_before_list is not None:
            last_before_list.next = before_pointer

        first_in_list.next = pointer

        return head if n > 1 else before_pointer


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
retur = Solution().reverseBetween(head, 1, 2)
