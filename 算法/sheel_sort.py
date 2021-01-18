from cal_time import *
import random


# 就是把插入排序中所有1改成gap就可以了
def insert_sort_gap(li, gap):
    n = len(li)
    # i表示摸到的牌的下标
    for i in range(gap, n):  # 初始时手里已经有张牌，所以从1开始，range是前包后不包，所以这里n不用-1
        temp = li[i]  # 这是我摸到的牌
        # 我手里的牌是i-gap 下标
        j = i - gap  # j就是手里的牌 下标
        # 这个while是从有序区的最后一张牌开始循环的，如果从第一张开始循环对比，没办法往后串牌
        # 就是要找到找到的牌该插入的位置
        while j >= 0 and li[j] > temp:  # li[j]=当前手里的这张牌比我摸到的牌temp大 且 j>=0
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = temp  # 把牌插入到j+gap的位置


@cal_time
def shell_sort(li):  # 希尔排序
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2

if __name__ == '__main__':
    li=list(range(1000))
    random.shuffle(li)
    print(li)
    shell_sort(li)
    print(li)