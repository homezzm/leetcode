from cal_time import *


# 插入排序
@cal_time
def insert_sort(li):
    n = len(li)
    # i表示摸到的牌的下标
    for i in range(1, n):  # 初始时手里已经有张牌，所以从1开始，range是前包后不包，所以这里n不用-1
        temp = li[i]  # 这是我摸到的牌
        # 我手里的牌是i-1 下标
        j = i - 1  # j就是手里的牌 下标
        # 这个while是从有序区的最后一张牌开始循环的，如果从第一张开始循环对比，没办法往后串牌
        # 就是要找到找到的牌该插入的位置
        while j >= 0 and li[j] > temp:  # li[j]=当前手里的这张牌比我摸到的牌temp大 且 j>=0
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp  # 把牌插入到j+1的位置


if __name__ == '__main__':
    li = [4, 6, 8, 3, 2, 7, 1, 9, 5]
    insert_sort(li)
    print(li)
