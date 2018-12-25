"""
    伸展树
"""
class SplayTreeMap():
    def _rotate(self, p):
        pass
    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                # zig case
                self._rotate(p)
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                # zig-zag case
                self._rotate(parent)  # move parent up
                self._rotate(p)       # move p up
            else:
                # zig-zig case
                self._rotate(p)  # move p up
                self._rotate(p)  # move p up again
 
    def _reblance_insert(self, p):
        self._splay(p)
 
    def _reblance_delete(self, p):
        if p is not None:
            self._splay(p)
 
    def _reblance_access(self, p):
        self._splay(p)

