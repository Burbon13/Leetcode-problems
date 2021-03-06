class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        list_size = self._calc_list_size(head)
        return self._my_sort(head, list_size)

    def _calc_list_size(self, head):
        list_size = 0

        while head is not None:
            head = head.next
            list_size += 1

        return list_size

    def _my_sort(self, head, list_size):
        if list_size == 1:
            return head

        left_list, left_size, right_list, right_size = self._separate_list(head, list_size)
        self._concat(left_list, left_size, right_list, right_size)
        return left_list

    def _separate_list(self, head, list_size):
        half_size = list_size // 2
        it = head

        while half_size > 0:
            it = it.next
            half_size -= 1

        return head, list_size // 2, it, list_size - (list_size // 2)

    def _concat(self, left_list, left_size, right_list, right_size):
        if left_list is None:
            return right_size
        if right_size is None:
            return left_list

        if right_list.val < left_list.val:
            right_list, left_list = left_list, right_list
            left_size, right_size = right_size, left_size

        to_ret = left_list

        while right_list is not None:
            if left_list.val <= right_list.val and (left_list.next is None or left_list.next.val >= right_list.val):
                next_right = right_list.next
                right_list.next = left_list.next
                left_list.next = right_list
                right_list = next_right


        return to_ret


def converter(list):
    to_ret = ListNode(list[0])
    it = to_ret
    for x in list[1:]:
        it.next = ListNode(x)
        it = it.next
    return to_ret


def pprt(node):
    print('=====')
    while node is not None:
        print(node.val, end=' ')
        node = node.next


solution = Solution()
a = solution.sortList(converter(
    [1, 3, 3, 1, 3, 1, 3, 3, 2, 3, 2, 2, 1, 1, 1, 3, 2, 2, 1, 1, 2, 2, 2, 3, 3, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 3, 3, 2,
     2, 3, 2, 3, 2, 2, 2, 1, 1, 3, 2, 3, 3, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 3, 1, 3, 1, 1, 1, 2, 1, 2, 2, 2, 1, 3, 2, 2,
     2, 3, 3, 2, 3, 3, 1, 1, 2, 2, 1, 2, 1, 3, 2, 1, 3, 3, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3, 3, 3, 1, 1, 3, 2,
     1, 1, 2, 1, 3, 3, 2, 2, 1, 3, 1, 3, 1, 3, 2, 2, 3, 2, 3, 2, 2, 1, 2, 3, 1, 3, 1, 2, 3, 3, 2, 3, 3, 3, 1, 1, 2, 3,
     1, 2, 3, 2, 1, 1, 2, 3, 1, 1, 3, 1, 2, 2, 3, 2, 1, 3, 1, 2, 1, 3, 2, 1, 1, 2, 2, 2, 1, 3, 1, 3, 2, 3, 3, 1, 1, 3,
     1, 2, 1, 2, 3, 1, 2, 1, 1, 3, 1, 3, 3, 1, 1, 1, 2, 2, 1, 3, 1, 2, 2, 3, 2, 1, 3, 2, 1, 3, 2, 2, 3, 3, 2, 2, 1, 3,
     2, 2, 2, 2, 2, 3, 2, 2, 3, 1, 3, 2, 1, 3, 2, 1, 2, 3, 3, 3, 1, 2, 2, 3, 1, 1, 2, 2, 3, 2, 1, 1, 1, 1, 1, 3, 2, 2,
     2, 1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 1, 3, 3, 1, 3, 1, 2, 2, 1, 2, 3, 2, 3, 3, 1, 2, 3, 2, 2, 3, 3, 2, 1, 3, 2, 2, 2,
     3, 3, 3, 1, 1, 2, 1, 1, 2, 3, 3, 3, 1, 3, 2, 2, 1, 2, 2, 1, 2, 3, 1, 3, 2, 2, 3, 3, 3, 1, 2, 3, 2, 1, 3, 1, 1, 2,
     2, 1, 1, 1, 2, 2, 3, 1, 3, 1, 2, 3, 3, 3, 2, 2, 3, 1, 1, 1, 3, 2, 1, 1, 3, 1, 2, 3, 3, 3, 2, 1, 2, 3, 2, 3, 2, 1,
     3, 2, 2, 2, 2, 1, 1, 3, 1, 1, 1, 3, 2, 2, 2, 1, 2, 3, 2, 3, 2, 2, 1, 2, 3, 2, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 1, 2,
     3, 3, 3, 1, 3, 2, 2, 3, 1, 1, 3, 1, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 3, 3, 3, 1, 2, 2, 2, 2, 3, 3, 1, 2,
     2, 3, 1, 3, 1, 2, 1, 2, 2, 3, 3, 1, 3, 3, 2, 1, 3, 1, 1, 3, 1, 2, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 2, 2, 2, 1, 1, 3,
     2, 2, 2, 3, 1, 3, 3, 3, 1, 1, 3, 1, 3, 2, 3, 1, 2, 3, 2, 2, 3, 3, 3, 1, 2, 1, 2, 1, 2, 3, 1, 2, 2, 2, 1, 1, 1, 2,
     2, 1, 2, 1, 1, 1, 3, 2, 1, 2, 3, 2, 2, 2, 1, 2, 3, 2, 2, 1, 3, 3, 3, 1, 2, 3, 3, 1, 1, 3, 3, 1, 1, 2, 1, 2, 3, 1,
     2, 3, 2, 2, 3, 2, 1, 3, 1, 3, 1, 2, 2, 2, 2, 1, 2, 3, 3, 2, 2, 2, 3, 2, 2, 1, 2, 2, 3, 1, 3, 1, 1, 1, 2, 3, 3, 2,
     2, 3, 3, 2, 3, 1, 1, 2, 2, 2, 3, 2, 2, 1, 1, 3, 2, 2, 3, 3, 3, 3, 1, 2, 3, 3, 1, 3, 3, 1, 2, 2, 1, 3, 2, 3, 3, 2,
     3, 2, 1, 2, 1, 2, 2, 3, 3, 2, 3, 3, 1, 1, 2, 1, 3, 2, 2, 3, 1, 2, 1, 3, 1, 1, 3, 3, 3, 3, 2, 3, 3, 3, 1, 3, 2, 2,
     2, 3, 3, 1, 2, 1, 2, 3, 2, 2, 2, 2, 3, 3, 1, 1, 3, 3, 2, 1, 3, 2, 2, 3, 2, 3, 2, 2, 2, 3, 1, 2, 1, 3, 2, 2, 1, 2,
     2, 3, 2, 2, 2, 2, 2, 1, 1, 2, 1, 3, 3, 2, 2, 2, 1, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 1, 3, 3, 1, 3, 2, 2, 2, 2, 2, 1,
     2, 2, 3, 3, 3, 1, 2, 3, 1, 3, 2, 2, 2, 2, 3, 1, 1, 1, 3, 2, 3, 3, 2, 3, 1, 2, 1, 2, 2, 1, 2, 2, 3, 3, 1, 2, 3, 2,
     2, 3, 3, 1, 1, 1, 2, 1, 2, 3, 3, 2, 2, 2, 2, 3, 1, 1, 1, 3, 3, 1, 1, 1, 3, 3, 3, 2, 3, 3, 1, 1, 1, 2, 3, 2, 2, 2,
     2, 1, 2, 2, 3, 1, 3, 1, 2, 3, 1, 3, 3, 1, 2, 3, 2, 2, 3, 3, 1, 1, 2, 1, 2, 3, 3, 3, 2, 1, 2, 1, 2, 3, 1, 2, 2, 1,
     2, 2, 2, 1, 2, 3, 3, 3, 3, 1, 2, 1, 3, 1, 1, 2, 1, 3, 1, 3, 2, 3, 2, 3, 3, 1, 2, 2, 2, 3, 3, 2, 1, 1, 3, 1, 2, 1,
     3, 1, 2, 1, 2, 2, 2, 1, 3, 1, 1, 2, 2, 1, 2, 1, 2, 3, 3, 1, 1, 3, 1, 1, 1, 2, 2, 3, 1, 3, 3, 3, 3, 2, 2, 1, 3, 2,
     3, 2, 2, 1, 3, 3, 2, 1, 2, 1, 2, 2, 3, 1, 2, 2, 1, 2, 2, 3, 1, 3, 3, 2, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 3,
     3, 2, 2, 1, 1, 3, 2, 2, 2, 3, 3, 3, 1, 2, 2, 1, 1, 3, 3, 3, 2, 2, 2, 2, 3, 1, 2, 1, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1,
     1, 3, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 3, 1, 1, 3, 1, 2, 1, 3, 2, 2, 3, 1, 2, 3, 3, 2, 3, 1, 1, 2, 2, 3, 3, 2, 2, 1,
     2, 2, 1, 2, 2, 1, 2, 1, 3, 2, 1, 2, 3, 1, 1, 2, 3, 2, 2, 2, 3, 2, 3, 3, 1, 1, 1, 3, 3, 1, 1, 2, 1, 1, 1, 2, 3, 3,
     2, 3, 3, 3, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 3, 1, 1, 2, 3, 1, 2, 3, 2, 1, 2, 2, 1, 3, 3, 2, 2, 1, 2,
     1, 3, 1, 3, 2, 1, 1, 3, 2, 3, 1, 1, 2, 3, 1, 1, 1, 3, 2, 2, 3, 2, 3, 1, 2, 2, 3, 1, 3, 2, 1, 1, 3, 2, 2, 1, 3, 2,
     1, 2, 3, 3, 1, 3, 3, 3, 1, 1, 2, 1, 1, 2, 3, 3, 2, 2, 3, 2, 1, 1, 2, 3, 1, 1, 3, 2, 3, 2, 1, 2, 3, 2, 1, 1, 1, 1,
     3, 2, 3, 2, 3, 1, 3, 2, 1, 3, 1, 3, 3, 2, 2, 3, 2, 3, 1, 3, 2, 1, 2, 2, 2, 3, 3, 2, 1, 2, 3, 1, 1, 3, 1, 2, 2, 2,
     3, 2, 3, 1, 1, 2, 1, 1, 3, 1, 3, 2, 1, 1, 1, 3, 1, 1, 3, 3, 3, 3, 1, 2, 3, 2, 3, 2, 1, 2, 1, 3, 1, 3, 1, 2, 2, 3,
     2, 3, 2, 3, 3, 3, 3, 1, 1, 2, 2, 3, 1, 1, 3, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 2, 3, 1, 2, 3, 3,
     1, 1, 3, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 3, 3, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 3, 2, 2,
     2, 3, 1, 3, 1, 2, 2, 2, 3, 3, 3, 2, 1, 2, 1, 1, 3, 3, 2, 3, 1, 2, 1, 2, 2, 3, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 2,
     3, 1, 1, 3, 1, 3, 2, 3, 1, 1, 1, 2, 1, 1, 2, 2, 2, 3, 2, 2, 2, 1, 3, 1, 1, 1, 1, 2, 3, 2, 3, 2, 2, 1, 3, 1, 2, 1,
     2, 1, 2, 2, 3, 1, 2, 3, 3, 2, 1, 1, 3, 2, 3, 1, 3, 1, 1, 1, 2, 3, 2, 1, 3, 3, 1, 3, 3, 3, 3, 2, 2, 3, 3, 1, 3, 2,
     2, 3, 3, 2, 3, 3, 3, 1, 1, 2, 2, 2, 2, 1, 3, 3, 1, 3, 2, 2, 3, 1, 2, 1, 1, 3, 1, 1, 2, 1, 1, 3, 1, 1, 3, 2, 2, 2,
     2, 2, 3, 2, 1, 3, 3, 2, 1, 1, 2, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 3, 2, 2, 2, 1, 3, 3, 2, 3, 2, 1, 1, 3, 3, 1,
     3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 3, 1, 2, 2, 1, 2, 2, 1, 1, 2,
     3, 1, 2, 2, 2, 3, 3, 1, 1, 3, 2, 3, 2, 2, 3, 1, 2, 1, 1, 1, 2, 3, 3, 1, 1, 2, 1, 2, 3, 3, 2, 2, 3, 1, 3, 3, 3, 3,
     1, 1, 3, 2, 2, 3, 2, 1, 3, 1, 3, 2, 1, 2, 1, 2, 1, 3, 2, 3, 1, 3, 2, 2, 3, 3, 3, 1, 2, 3, 3, 1, 1, 2, 1, 2, 1, 3,
     2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 3, 2, 1, 2, 2, 1, 1, 2, 3, 3, 1, 3, 2, 2, 3, 3, 2, 1, 3, 2, 1, 3, 3, 2, 2, 1,
     3, 2, 1, 3, 2, 3, 2, 2, 1, 2, 1, 1, 3, 1, 1, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 1, 1, 2, 2, 1, 2,
     2, 2, 3, 2, 1, 2, 1, 2, 3, 1, 1, 1, 3, 1, 2, 3, 2, 3, 2, 2, 2, 3, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 1, 3, 2, 2, 3,
     3, 3, 2, 1, 2, 2, 1, 3, 2, 2, 1, 2, 3, 1, 3, 3, 1, 3, 3, 2, 2, 1, 1, 2, 3, 1, 1, 3, 3, 1, 3, 3, 3, 3, 2, 3, 1, 2,
     2, 1, 1, 1, 1, 1, 3, 1, 3, 2, 3, 2, 1, 2, 2, 1, 2, 3, 2, 1, 1, 3, 2, 3, 2, 3, 3, 1, 2, 1, 2, 3, 3, 2, 3, 3, 2, 3,
     2, 3, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 2, 1, 3, 3, 3, 1, 2, 3, 3, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 3, 3, 2, 1, 3, 1, 1,
     1, 2, 2, 1, 3, 3, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 1, 3, 1, 2, 3, 3, 1, 2, 2, 1, 1, 2, 1, 1, 3, 3, 2, 3, 3, 1, 2, 3,
     3, 2, 2, 3, 1, 2, 3, 3, 3, 3, 1, 2, 3, 1, 2, 2, 1, 1, 3, 1, 2, 3, 3, 1, 2, 2, 1, 3, 2, 3, 2, 1, 2, 1, 3, 2, 3, 1,
     1, 1, 2, 3, 1, 3, 2, 2, 2, 2, 2, 3, 1, 2, 2, 1, 2, 2, 3, 2, 2, 1, 3, 1, 2, 2, 2, 1, 2, 3, 1, 1, 3, 2, 3, 2, 3, 3,
     2, 1, 3, 2, 1, 3, 2, 2, 3, 1, 1, 3, 3, 1, 2, 3, 2, 1, 3, 3, 3, 3, 1, 1, 3, 1, 3, 2, 2, 3, 3, 1, 3, 1, 1, 2, 1, 1,
     3, 1, 1, 2, 3, 3, 1, 1, 3, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 3, 2, 1, 3, 1, 2, 1, 3, 3, 1, 3, 3, 2, 2, 2, 3, 1, 3, 1,
     2, 2, 2, 3, 1, 3, 3, 1, 3, 3, 2, 3, 1, 1, 2, 2, 2, 2, 3, 1, 1, 2, 3, 1, 1, 3, 1, 3, 1, 1, 3, 3, 2, 2, 1, 3, 2, 2,
     2, 2, 3, 1, 1, 1, 2, 1, 1, 1, 2, 2, 3, 2, 1, 2, 1, 1, 2, 3, 2, 1, 1, 1, 2, 2, 3, 3, 1, 3, 1, 2, 2, 1, 2, 2, 1, 1,
     1, 1, 2, 1, 1, 1, 1, 3, 2, 3, 1, 3, 3, 1, 3, 1, 2, 1, 1, 1, 2, 3, 3, 2, 1, 1, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 2, 1,
     3, 2, 2, 2, 3, 2, 1, 1, 3, 2, 1, 2, 2, 1, 1, 2, 1, 2, 3, 2, 1, 3, 2, 2, 2, 3, 1, 3, 2, 1, 3, 2, 1, 1, 1, 3, 1, 1,
     1, 2, 2, 2, 2, 2, 3, 2, 3, 1, 3, 1, 3, 3, 2, 3, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 1, 3, 2, 1, 1]))
pprt(a)
