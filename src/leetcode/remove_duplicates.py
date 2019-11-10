# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None

        last_duplicate_value = -999999999999
        to_return = None
        last_pointer = None

        pointer = head
        while pointer is not None:
            if pointer.next is not None and pointer.next.val == pointer.val:
                last_duplicate_value = pointer.val
                pointer = pointer.next
                continue
            if pointer.val == last_duplicate_value:
                pointer = pointer.next
                continue

            if to_return is None:
                to_return = pointer
                last_pointer = pointer
            else:
                last_pointer.next = pointer
                last_pointer = pointer

            pointer = pointer.next

        if last_pointer is not None:
            last_pointer.next = None
        return to_return
