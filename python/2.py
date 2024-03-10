from typing import Optional, List, Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'{self.val}, {self.next}'


class Solution:

    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = (l1, l2)
        result = ListNode(0)
        res_ptr = result
        carry = 0
        for ii in range(100):
            val_1 = 0
            val_2 = 0
            if ptr1 is not None:
                val_1 = ptr1.val
                ptr1 = ptr1.next

            if ptr2 is not None:
                val_2 = ptr2.val
                ptr2 = ptr2.next

            res_ptr.val = (carry + val_1 + val_2) % 10
            carry = (carry + val_1 + val_2) // 10
            if ptr1 is not None or ptr2 is not None or carry > 0:
                res_ptr.next = ListNode(0)
                res_ptr = res_ptr.next
            else:
                break
        return result

    def addTwoNumbers2(self,
                       l1: Optional[ListNode],
                       l2: Optional[ListNode]) -> Optional[ListNode]:
        total = []
        carry = 0
        list1 = []
        list2 = []
        list1ptr = l1
        list2ptr = l2
        for a in range(100):
            list1.append(list1ptr.val)
            list1ptr = list1ptr.next
            if list1ptr is None:
                break

        for a in range(100):
            list2.append(list2ptr.val)
            list2ptr = list2ptr.next
            if list2ptr is None:
                break

        if len(list1) < len(list2):
            list1
        for a, b in zip(list1, list2):
            c = a + b + carry
            carry = 0
            if c > 10:
                c = c - 10
                carry = 1
                total.append(c)
            else:
                total.append(c)

        print(total)
        head = ListNode(total)
        ptr = head
        for i, v in enumerate(total):
            ptr.val = v

            if i < len(total) - 1:
                ptr.next = ListNode()
        return head


print(Solution().addTwoNumbers(
    ListNode(1, ListNode(2, ListNode(1))),
    ListNode(1, ListNode(3))))
