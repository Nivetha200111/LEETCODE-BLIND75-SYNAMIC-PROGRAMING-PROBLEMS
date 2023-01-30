class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre, cur = None, slow
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
