"""
设计循环队列
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.cur_size = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cur_size < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            self.tail.pre = node
            node.pre.next = node
            self.cur_size += 1
            return True
        return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.cur_size > 0:
            node = self.head.next
            self.head.next = node.next
            node.next.pre = self.head
            self.cur_size -= 1
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return self.head.next.val

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return self.tail.pre.val

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.cur_size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.cur_size == self.size