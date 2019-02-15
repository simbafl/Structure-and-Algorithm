"""
有效的括号，用栈思想解决
"""


def isValid(s):
    """
    type s: str
    rtype: bool
    """
    import collections
    stack = collections.deque()
    for i in s:
        if i in ["{", "(", "["]:
            stack.append(i)
        if i in ["}", ")", "]"]:
            if len(stack) != 0:
                tmp = stack.pop()
            else:
                return False
            if tmp == "(" and i != ")":
                return False
            if tmp == "{" and i != "}":
                return False
            if tmp == "[" and i != "]":
                return False
    return len(stack) == 0  # 栈为空则匹配完
