class Elem(object):
    def __init__(self, val, min_val):
        self.val = val
        self.min_val = min_val


class MinStack(object):
    """
    https://leetcode-cn.com/problems/min-stack/
    """

    def __init__(self):
        self.min_stack = []

    def push(self, x):
        if self.isEmpty():
            self.min_stack.append(Elem(x, x))
        else:
            elem = Elem(x, min(x, self.min_stack[-1].min_val))
            self.min_stack.append(elem)

    def pop(self):
        if not self.isEmpty():
            self.min_stack.pop(-1)

    def top(self):
        if not self.isEmpty():
            return self.min_stack[-1].val
        else:
            return 0

    def getMin(self):
        if not self.isEmpty():
            return self.min_stack[-1].min_val
        else:
            return 0

    def isEmpty(self):
        return len(self.min_stack) == 0


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-1)
    print("getMin=", minStack.getMin())
    print("top=", minStack.top())
    minStack.pop()
    print("getMin=", minStack.getMin())
