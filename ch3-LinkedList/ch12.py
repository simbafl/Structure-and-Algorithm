"""
合并两个有序链表
"""
def mergeTwoLists(l1, l2):
    # 迭代
    # 空间复杂度O(1), 时间复杂度O(m+n)
    dummy_head = node = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    node.next = l1 if l1 else l2
    return dummy_head.next


def mergeTwoLists2(l1, l2):
    # 递归
    # 空间复杂度O(m+n), 时间复杂度O(m+n)
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists2(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists2(l1, l2.next)
        return l2
