# 双向队列
from collections import deque


# q = deque()  # 双向的就是四个操作了，单向的就只有push和pop
# q.append(1)  # 入队 从右边加 队尾进队
# q.popleft()  # 出队 从左边出 队首出队
#
# q.appendleft(2) #从左边进队 队首进队
# q.pop() #队尾出队

# q = deque([1,2,3,4,5],5)
# #参数1：初始时可以给队列直接加入一些元素
# #参数2：队列最大的长度
# #注意：python中如果队满了就自动出队，不会报错
# q.append(6)
# #这时弹出的值就是2而不是1了，因为1已经自动出队了
# #队里还有[2,3,4,5,6]
# print(q.popleft())

def tail(n):
    with open('dequeTest.txt', 'r', encoding='UTF-8') as file:
        # args1:file相当于一个列表
        # args2:n队列的最大值，如果队满了就自动出队
        q = deque(file, n)
        return q


if __name__ == '__main__':
    print(tail(5))  # 可以读取这个文件的后5行内容
