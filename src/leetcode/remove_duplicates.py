# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None

        last_head = head
        current_head = head.next

        while current_head is not None:
            if last_head.val != current_head.val:
                last_head.next = current_head
                last_head = current_head
            current_head = current_head.next

        last_head.next = None

        return head
