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

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """
           前序遍历
           generate a preorder iteration of position in the tree
        """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
 
    def _subtree_preorder(self, p):
        """generate a preorder iteration of position in subtree rooted at p"""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def positions(self):
        """generate an iteration of the tree's positions"""
        return self.preorder()

    # -----后序--------
    def postorder(self):
        """后序遍历"""
        if not self.is_empty():
            for p in self._subtree._postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """generate a postorder iteration of position in subtree rooted at p"""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    # ----中序--------
    def inorder(self):
        """中序遍历"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left()):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right()):
                yield other


class BinaryTree(Tree):
    """二叉树"""
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')
    def sibling(self, p):
        """return the brother node，None if p is root"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def chilren(self, p):
        """generate the child node of p"""
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
        """an anstraction representing the location of a single element"""
        def __init__(self, container, node):
            self._container = container
            self.node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """check position p is validate"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """rerurn the position instance for given node, for None if no node"""
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
        """place element e at the root of an empty tree and return new position"""
        if self._root is not None: raise ValueError('root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """create a new left child for position p, storing element e"""
        node = self._validate(p)
        if node._left is not None: raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """create a new right child for position p, storing element e"""
        node = self._validate(p)
        if node._right is not None: raise ValueError('right child exists')
        self._size += 1
        node.right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """replace the element at position p with e, and return old's element"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """
        Delete the node at position p
        return ValueError if position p is invalid or p has two children
        return the element that had been stored at position p
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two cildren')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent  # child's grandparent become parent
        if node is self._root:
            self._root = child  # child bocomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node.parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """
        把t1和t2分别合为p的左右子树，不会翻译ooo
        p节点必须为叶子节点才支持此操作，同时3个树必须为同一种类型
        """
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position p must be leaf') 
        if not type(self) is type(t1) is type(t2): raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty(): 
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set t1 instance to empty, GC collect
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None  # set t2 instance to empty, GC collect
            t2._size = 0

