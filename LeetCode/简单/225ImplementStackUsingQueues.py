from collections import deque


class MyStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.empty(): return 0
        return self.stack.pop()

    def top(self):
        if self.empty(): return 0
        # 看栈顶 先把对队最后一个数弹出来，然后在放进去
        val = self.stack.pop()  # 重另一个方向弹出就能
        self.push(val)
        return val

    def empty(self):
        return len(self.stack) == 0


if __name__ == '__main__':
    # ["MyStack", "push", "push", "top", "pop", "empty"]
    # [[], [1], [2], [], [], []]
    #[null,null,null,2,2,false]
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    print(obj.empty())

    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
