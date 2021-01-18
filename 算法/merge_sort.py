import random
from cal_time import *


# 归并排序
def merge(li, low, mid, high):
    """
    归并/合并 三个参数用来限定住列表的两段
    :param li:
    :param low:指针的位置就是索引
    :param mid:指针的位置就是索引
    :param high:指针的位置就是索引
    :return:
    """
    i, j = low, mid + 1
    ltmp = []
    # while的条件就是只要两边都有数进继续循环
    while i <= mid and j <= high:  # 限制住两个指针不越界
        if li[i] < li[j]:  # 拿两个指针指向的数进行对比，小的到一个新的列表中
            ltmp.append(li[i])
            i += 1  # 移动指针到下一个位置
        else:  # 否则就是列表的另外一半那个数小
            ltmp.append(li[j])
            j += 1
    # 当while执行完后，两部分肯定有一部分没有数了要么是i到mid了，要么是j到high了
    # 看下这两部分哪部分没数了
    while i <= mid:  # 第一部分还有数，就把剩余的数放到列表中
        ltmp.append(li[i])
        i += 1  # 移动指针到下一个位置
    while j <= high:
        ltmp.append(li[j])
        j += 1  # 移动指针到下一个位置

    # 把临时表的数据写回到原表中，可以用循环也可以用切片
    li[low:high + 1] = ltmp


def _merge_sort(li, low, high):  # 分解
    if low < high:  # 至少有两个元素 递归的终止条件
        # 3步走，1步分解左边 2步分解右边 3步合并
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


@cal_time
def merge_sort(li):  # 套了个马甲，为了计算运行时间
    _merge_sort(li, 0, len(li) - 1)


if __name__ == '__main__':
    li = list(range(10000))
    random.shuffle(li)
    merge_sort(li)
    print(li)
