"""
[Int]: [1->4->5, 1->2->3, 2->6]

[Out]: 1->1->2->2->3->4->5->6
思路：
把所有链表的节点加到数组中，然后排序
对数组中的节点按顺序取出再构造成一个链表
"""

def mergeKLists(lists):
    res = []
    for i in lists:
        while i:
            res.append(i.val)
            i = i.next
    if res == []:
        return []
    res.sort()
    l = ListNode(0)
    first = l
    while res:
        l.next = ListNode(res.pop(0))
        l = l.next
    return first.next

"""
可以使用优先级队列或堆
"""
def mergeKLists(lists):
    import heapq
    l = ListNode(0)
    first = l
    p = list()
    for i in lists:
        if i:
            heapq.headppush(p, (i.val, i))
    while len(p) > 0:
        first.next = heapq.heappop(p)[1]
        first = first.next
        if first.next:
            heapq.heappush(p, (first.next.val, first.next))
    return first.next
