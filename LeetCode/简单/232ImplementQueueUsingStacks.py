class MyQueue(object):

    def __init__(self):
        """
        Initialize your val structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)  # 1,2

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) > 0:
            return self.stack2.pop(-1)
        else:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop(-1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) > 0:
            return self.stack2[-1]
        elif len(self.stack1) > 0:
            return self.stack1[0]
        return -1

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
