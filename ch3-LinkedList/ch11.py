"""
删除链表的倒数第n个节点
初始化两指针p，q
p先移动n步，q再移动
p的next指向null时，q的next指向就是倒数第n个节点
"""
def removeNthFromEnd(head, n):
    node = ListNode(0)
    node.next = head
    p1 = p2 = node
    for i in range(n):
        p1 = p1.next  # p1先移动n步
    while p1.next:  # p1,p2同时移动直到末尾
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next # p2指针跳过p2.next即可
    return node.next  # 返回头节点
