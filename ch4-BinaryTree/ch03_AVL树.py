"""
    AVL树
"""


class AVLTreeMap():
    class _Node():
        __sloats__ = '_height, _left, _right, _parent, _element'

        def __init__(self, element, parent=None, left=None, right=None):
            self._height = 0

        def left_height(self):
            return self._left._height if self._left is not None else 0
        
        def right_height(self):
            return self._right._height if self._right is not None else 0
 
    def _relink(self, parent, child, make_left_child):
        """正确关联父亲和孩子节点"""
        if make_left_child:
            parent._left = child   # 使child成为左节点，child允许为None
        else:
            parent._right = child   # 使child成为右节点，child允许为None
        if child is not None:
            child._parent = parent   # 如果child存在，指向父节点(定义双指针)
 
    def _rotate(self, p):
        """旋转节点和原来的祖父母节点进行关联"""
        a = p._node
        b = a._parent
        c = b._parent
        if c is None:    # 这种情况是b为根节点，旋转之后a变为根节点
            self._root = a
            x._parent = None
        else:
            self._relink(c, a, b == c._left)  # 如果b为c的左节点，就直接使a变为c的左节点
        if a == b._left:                      # 如果a也为b的左节点，就使a的右节点变为b的左节点
            self._relink(b, a._right, True)
            self._relink(a, b, False)
        else:								  # 如果a也为b的右节点，就使a的右节点变为b的右节点
            self._relink(b, a._left, False)
            self._relink(a, b, True)
 
    def _restructure(self, x):
        """判断需要旋转一次还是两次"""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):  # 此时三个节点在一条直线上，旋转一次, 使y成为root节点
            self._rotate(y)
            return y
        else:					
            self._rotate(x)	 # 旋转一次, 使三个节点成为一条线
            self._rotate(x)  # 旋转两次，使三个节点变平衡
            return x
 
    def _recompute_height(self, p):
        """计算树的高度"""
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())
 
    def _isbalanced(self, p):
        """判断树是否平衡"""
        return abs(p._node.left_height() - p._node.right_height()) <= 1
 
    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)
 
    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)
 
    def _rebalance(self, p):
        """恢复树的平衡"""
        while p is not None:
            old_height = p._node._height
            if not self._rebalance(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)
 
    def _reblance_insert(self, p):
        """插入操作后重新使树平衡"""
        self._rebalance(p)
 
    def _reblance_delete(self, p):
        """删除操作后重新使树平衡"""
        self._rebalance(p)