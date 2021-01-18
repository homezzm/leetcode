import random
from cal_time import *


# 堆排序
def sift(li, low, high):
    """
    调整堆，小分堆
    :param li: 列表
    :param low: 堆的根节点位置(堆底) 指针
    :param high:堆的最后一个元素的位置（堆顶） 指针
    :return:
    """
    i = low  # i最开始是根节点（堆顶）
    j = 2 * i + 1  # j开始是左孩子
    temp = li[low]  # 把堆顶存起来
    # 在接下来的循环中要一直比对temp与j的大小，
    # i指向的是要去的位置(空位)，j指向的是空位下的左/右孩子
    # while的条件j<=high就是要保证j不超过堆顶
    while j <= high:  # 只要j有数，没有越界，就一直比较
        # j初始时是左孩子，堆的向下调整需要temp与左右孩子进行对比，
        # 谁大谁上，所以左孩子和右孩子要先比较大哪个更大
        # li[j+1]就是右孩子，因为堆存储的左孩子与右孩子是相邻的
        # 如果右孩子大，不交换，把指针指向右孩子即可
        # 需要注意可能会出现没有右孩子的情况，所以要在if中增加个条件[j + 1 <= high]
        # 来保证右孩子有且没有越界
        if j + 1 <= high and li[j + 1] < li[j]:  # *所以基于对比来排序的算法都可以通过改变比较运算符来控制输出的是升序还是降序
            j = j + 1  # 把j指向右孩子，就是两个孩子中更大的那具
        # 接下来要看是j上到i的位置，还是temp放回去
        # 孩子的领导能力是否比退下来的temp领导力大，如果大就让孩子当领导
        if li[j] < temp:  # *所以基于对比来排序的算法都可以通过改变比较运算符来控制输出的是升序还是降序
            li[i] = li[j]  # 把孩子提上去当领导
            i = j  # 如果孩子顺利当上领导，这里就需要把i与j同时向下移动，把i移动到刚才孩子的空位
            j = 2 * i + 1  # j指向空位下的左孩子
        else:  # 对比了下还是退下来的领导temp能力值更大，那就把temp放到i的位置上，调整结束
            break
    li[i] = temp  # 让退下来的领导回到空位，不算这空位是村民还是领导


def topk(li, k):
    heap = li[0:k]  # 切片，切k那么长
    # 1.构建堆
    for i in range((k - 1 - 1) // 2, -1, -1):
        sift(heap, i, k - 1)  # 调整堆
    # 2.遍历列表中所有元素
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:  # 如果列表中剩下的数大于堆顶，覆盖堆顶
            heap[0] = li[i]
            sift(heap, 0, k - 1)  # 调整堆
    # 3.挨个出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap

if __name__ == '__main__':
    li=list(range(1000))
    random.shuffle(li)
    #print(li)
    print(topk(li,10))
