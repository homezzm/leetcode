# 队列
class Queue_h:
    def __init__(self, size=100):
        self.size = size
        # 这个队列要有大小，要不没办法做队的一些状态判断
        self.queue = [0 for _ in range(size)]
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):
        if not self.is_filled():
            # 进队先把rear+1 再把元素写到rear的位置上
            # 取余数主要是为了能让队列变成环形
            self.rear = (self.rear + 1) % self.size
            # 把元素写到rear的位置上
            self.queue[self.rear] = element
        else:
            raise IndexError('队列满了！')

    def pop(self):
        if not self.is_empty():
            # 任何时候front都不指向元素 front+1才指向元素
            self.front = (self.front + 1) % self.size
            # 其实这个时候front指向的值是存在的，因队列都是通过这两个指针来判断状态的，
            # 所以队列中有以前的值也无所谓，没必须再写代码清除它
            return self.queue[self.front]
        raise IndexError('队列是空的！')

    def is_empty(self):
        # 判断是否是空队
        return self.rear == self.front

    def is_filled(self):
        # 判断是否队满
        return (self.rear + 1) % self.size == self.front


if __name__ == '__main__':
    q = Queue_h(5)
    # 注意队列满的条件是队首与队尾之间还空了一个，判断时使用
    # 所以push的数据只能是queue的最大长度-1
    for i in range(5):
        q.push(i)
