class Tree(object):
    """普通树"""
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')
        def __ne__(self, other):
            return not (self == other)
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    def num_children(self):
        raise NotImplementedError('must be implemented by subclass')
    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    def is_root(self, p):
        return self.root() == p
    def is_leaf(self, p):
        return self.num_children(p) == 0
    def is_empty(self):
        return len(self) == 0

class BinaryTree(Tree):
    """二叉树"""
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def sibling(self, p):
        """返回兄弟节点，root节点返回None"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def chilren(self, p):
        """迭代孩子节点"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    """基于链表二叉树"""
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
             self._element = element
             self._parent = parent
             self._left = left
             self.right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self.node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other_node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
    """返回给定节点的位置"""
        return self.Position(self.node) if node is not None else None
   
#-------------- 公开访问方法 ---------------
    def __init__(self):
        self._root = None 
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
  
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
  
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None: raise ValueError('root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: raise ValueError('right child exists')
        self._size += 1
        node.right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        retrun old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:raise ValueError('p has two cildren')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node.parent = node
        return node._element

    
