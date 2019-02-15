"""以scrapy爬虫框架举例，默认为深度优先搜索"""


def depth_tree(root):
    """深度优先搜索，基于递归"""
    if root is not None:
        print(root.data)
        if root._left is not None:
            return depth_tree(root._left)
        if root._right is not None:
            return depth_tree(root._right)


def level_tree(root):
    """广度优先，基于队列"""
    if root is None:
        return 
    my_queue = []
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.pop(0)
        print(node.data)
        if node.lchild is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)

